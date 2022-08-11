from functools import wraps
from contextlib import contextmanager
from typing import Callable

from timeti.stopwatch import Stopwatch


@contextmanager
def timing(name: str = None, serialize: Callable = None):
    """Serialize elapsed time of code block."""
    mention = f" '{name}' "
    sw = Stopwatch()
    yield sw
    sw.pause()
    if serialize is not None:
        serialize(sw, name)
    else:
        print(f"Elapsed time of{mention}block: {sw.clockface}")


def totime(items, name: str = None, serialize: Callable = None):
    """Serialize elapsed time of iteration."""
    mention = f" '{name}' "
    sw = Stopwatch()
    for i, item in enumerate(items):
        yield sw, item
        lap = sw.lap()
        with sw.paused():
            if serialize is not None:
                serialize(sw, name, indx)
            else:
                lap = sw.laps[-1]
                print(f"Elapsed time of{mention}loop iteration {i}: {lap}")

    sw.pause()
    if serialize is not None:
        serialize(sw, name, indx)
    else:
        print(f"Elapsed time of{mention}loop: {sw.clockface}")



def timer(serialize: Callable = None):
    def decorator(func):
        """Logging elapsed time of funciton (decorator)."""

        @wraps(func)
        def wrapper(*args, **kwargs):
            with timing(func.__name__):
                return func(*args, **kwargs)

        return wrapper

    return decorator
