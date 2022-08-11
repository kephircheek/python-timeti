import time

import timeti


@timeti.timer()
def wait(t):
    time.sleep(t)


wait(0.5)
