import time

import timeti


def serializer(sw: timeti.Stopwatch, name: str):
    print(f"[{name}] block {sw.clockface}")


with timeti.timing("My context manager", serializer=serializer) as sw:
    time.sleep(0.1)

# ------------- stdout -------------
# [My context manager] block 105 ms
