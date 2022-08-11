import time

import timeti

with timeti.timing("My context manager") as sw:
    time.sleep(0.1)
    print(sw.clockface.milliseconds)
    time.sleep(0.1)
    print(sw.clockface.milliseconds)
