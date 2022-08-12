import io
import sys
import time
import unittest
from contextlib import contextmanager

import timeti


@contextmanager
def stdout_string():
    stdout_ = sys.stdout
    sys.stdout = buffer = io.StringIO()
    yield buffer
    sys.stdout = stdout_


class TestContextmanager(unittest.TestCase):
    def test_unnamed_default_serialize_message(self):
        with stdout_string() as buffer:
            with timeti.timing():
                time.sleep(0.01)
        msg = buffer.getvalue()
        self.assertTrue(msg.startswith("Elapsed time of block:"), msg=msg)


class TestLoop(unittest.TestCase):
    def test_unnamed_default_serialize_message(self):

        with stdout_string() as buffer:
            for _ in timeti.totime(range(1)):
                time.sleep(0.01)

        msg = buffer.getvalue().rstrip().split("\n")
        msg_iter, msg_final = msg
        self.assertTrue(msg_iter.startswith("Elapsed time of loop iteration 0:"), msg=msg_iter)
        self.assertTrue(msg_final.startswith("Elapsed time of loop:"), msg=msg_final)

    def test_default_return_mode(self):
        with stdout_string():
            for inx in timeti.totime(range(3)):
                time.sleep(inx / 100)

    def test_sw_mode(self):
        with stdout_string():
            for sw, inx in timeti.totime(range(3), ret_sw=True):
                delay = inx / 100
                time.sleep(delay)
                self.assertLess(sw.clockface.milliseconds, 40)


class TestDecorator(unittest.TestCase):
    def test_unnamed_default_serialize_message(self):
        @timeti.timer()
        def wait():
            time.sleep(0.01)

        with stdout_string() as buffer:
            wait()

        msg = buffer.getvalue()
        self.assertTrue(msg.startswith("Elapsed time of 'wait' function:"), msg=msg)
