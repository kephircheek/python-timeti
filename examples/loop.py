import time

import timeti

for inx in timeti.profiler(range(3), "My loop"):
    time.sleep(inx / 10)
