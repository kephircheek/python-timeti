import time

import timeti

for sw, inx in timeti.totime(range(3), "My loop"):
    time.sleep(inx)
