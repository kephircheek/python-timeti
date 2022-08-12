import time

import timeti


def serializer(sw: timeti.Stopwatch, name: str, i: int = None, verbose: bool = True):
    if verbose:
        if i is not None:
            lap = sw.laps[-1]
            print(f"[{name}] iter={i:02} {lap}")
        else:
            print(f"[{name}] whole loop {sw.clockface}")


for inx in timeti.profiler(range(12), "My loop", serializer=serializer):
    time.sleep(0.001)


# --------- stdout ---------
# [My loop] iter=00 1 ms
# [My loop] iter=01 1 ms
# [My loop] iter=02 1 ms
# [My loop] iter=03 1 ms
# [My loop] iter=04 1 ms
# [My loop] iter=05 1 ms
# [My loop] iter=06 1 ms
# [My loop] iter=07 1 ms
# [My loop] iter=08 1 ms
# [My loop] iter=09 1 ms
# [My loop] iter=10 1 ms
# [My loop] iter=11 1 ms
# [My loop] whole loop 15 ms
