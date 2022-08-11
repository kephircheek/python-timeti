import time

import timeti

with timeti.timing("My context manager") as sw:
    time.sleep(0.6)
    print(sw.clockface.seconds)
    time.sleep(0.4)
    print(sw.clockface.seconds)
