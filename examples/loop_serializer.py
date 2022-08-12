import time

import timeti


def serializer(sw: timeti.Stopwatch, name: str, i: int = None, verbose: bool = True):
    if verbose:
        if i is not None:
            lap = sw.laps[-1]
            print(f"[{name}] iter={i:03} {lap}")
        else:
            print(f"[{name}] whole loop {sw.clockface}")


for inx in timeti.totime(range(12), "My loop", serializer=serializer):
    time.sleep(0.001)


# --------- stdout ---------
# [My loop] iter=000 1 ms
# [My loop] iter=001 1 ms
# [My loop] iter=002 1 ms
# [My loop] iter=003 1 ms
# [My loop] iter=004 1 ms
# [My loop] iter=005 1 ms
# [My loop] iter=006 1 ms
# [My loop] iter=007 1 ms
# [My loop] iter=008 1 ms
# [My loop] iter=009 1 ms
# [My loop] iter=010 1 ms
# [My loop] iter=011 1 ms
# [My loop] whole loop 15 ms
