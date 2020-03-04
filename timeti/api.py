import logging
from functools import wraps
from contextlib import contextmanager

from timeti.stopwatch import Stopwatch

@contextmanager
def timing(name=None):
    """Logging elapsed time of code block (context manager)."""
    logger = logging.getLogger(name or __name__)

    stopwatch = Stopwatch()
    yield stopwatch
    logger.debug(f"Elapsed time: {stopwatch.clockface}")


def totime(iterable, name=None):
    """Logging elapsed time of iteration (generator)."""
    logger = logging.getLogger(name or __name__)

    stopwatch = Stopwatch()

    for indx, obj in enumerate(iterable):
        yield Stopwatch(), obj
        logger.debug(f"Elapsed time of loop {indx}: {stopwatch.lap()}")

    logger.debug(f"Elapsed time: {stopwatch.clockface}")

def timer(func):
    """Logging elapsed time of funciton (decorator)."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        with timing(func.__name__):
            return func(*args, **kwargs)

    return wrapper

