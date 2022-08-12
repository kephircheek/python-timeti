import time

import timeti

with timeti.profiler("My context manager") as p:
    time.sleep(0.1)
    print(p.sw.clockface.milliseconds)
    time.sleep(0.1)
    print(p.sw.clockface.milliseconds)
