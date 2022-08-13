import time

import timeti


@timeti.profiler()
def wait(t):
    time.sleep(t)


wait(0.1)
