import sys; sys.path.append('../') # umcomment to execute example here
import time
import logging
logging.basicConfig(format='[%(levelname)s] [%(name)s] %(message)s', level=logging.DEBUG)

from timeti import timing, timer, totime

# contextmanager
with timing('contexmanager') as sw:
    time.sleep(1.4)
    print('Elapsed time:', sw.clockface.seconds, 'sec')
    time.sleep(1.8)
    print('Elapsed time:', sw.clockface.seconds, 'sec')


# generator
for sw, inx in totime(range(3), 'cycle'):
    time.sleep(inx)
    #print(f"sleeptime: {sw.clockface.seconds} sec")


# decorator
@timer
def wait(t):
    time.sleep(t)

wait(0.5)

