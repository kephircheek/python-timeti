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
    def test_named_default_serialize_message(self):
        with stdout_string() as buffer:
            with timeti.profiler("Test payload"):
                time.sleep(0.01)
        msg = buffer.getvalue()
        self.assertTrue(msg.startswith("Elapsed time of 'Test payload' block:"), msg=msg)

    def test_unnamed_default_serialize_message(self):
        with stdout_string() as buffer:
            with timeti.profiler():
                time.sleep(0.01)
        msg = buffer.getvalue()
        self.assertTrue(msg.startswith("Elapsed time of block:"), msg=msg)

    def test_with_as(self):
        with stdout_string() as buffer:
            with timeti.profiler() as p:
                time.sleep(0.01)
        self.assertLess(p.sw.clockface.milliseconds, 15)

    def test_silent_mode(self):
        with stdout_string() as buffer:
            with timeti.profiler(verbose=False):
                time.sleep(0.01)
        msg = buffer.getvalue()
        self.assertEqual(msg, "")


class TestLoop(unittest.TestCase):
    def test_named_default_serialize_message(self):

        with stdout_string() as buffer:
            for _ in timeti.profiler(range(1), "Test payload"):
                time.sleep(0.01)

        msg_iter, msg_final = buffer.getvalue().rstrip().split("\n")
        self.assertTrue(
            msg_iter.startswith("Elapsed time of 'Test payload' loop iteration 0:"), msg=msg_iter
        )
        self.assertTrue(msg_final.startswith("Elapsed time of 'Test payload' loop:"), msg=msg_final)

    def test_unnamed_default_serialize_message(self):

        with stdout_string() as buffer:
            for _ in timeti.profiler(range(1)):
                time.sleep(0.01)

        msg_iter, msg_final = buffer.getvalue().rstrip().split("\n")
        self.assertTrue(msg_iter.startswith("Elapsed time of loop iteration 0:"), msg=msg_iter)
        self.assertTrue(msg_final.startswith("Elapsed time of loop:"), msg=msg_final)

    def test_default_return_mode(self):
        with stdout_string():
            for inx in timeti.profiler(range(3)):
                time.sleep(inx / 100)

    def test_sw_mode(self):
        with stdout_string():
            for sw, inx in timeti.profiler(range(3), ret_sw=True):
                delay = inx / 100
                time.sleep(delay)
                self.assertLess(sw.clockface.milliseconds, 40)

    def test_silent_mode(self):
        with stdout_string() as buffer:
            with timeti.profiler(verbose=False):
                for inx in timeti.profiler(range(3), verbose=False):
                    time.sleep(inx / 100)
        msg = buffer.getvalue()
        self.assertEqual(msg, "")

    def test_custom_serializer(self):
        def serializer(sw, name, i, verbose):
            if verbose:
                if i is not None:
                    lap = sw.laps[-1]
                    print(f"[{name}] iter={i:03} {lap}")
                else:
                    print(f"[{name}] whole loop {sw.clockface}")

        with stdout_string() as buffer:
            for inx in timeti.profiler(range(1), "My loop", serializer=serializer):
                time.sleep(0.001)

        msg_iter, msg_final = buffer.getvalue().rstrip().split("\n")
        self.assertEqual(msg_iter, "[My loop] iter=000 1 ms")
        self.assertEqual(msg_final, "[My loop] whole loop 1 ms")


class TestDecorator(unittest.TestCase):
    def test_default_serialize_message(self):
        @timeti.profiler()
        def wait():
            time.sleep(0.01)

        with stdout_string() as buffer:
            wait()

        msg = buffer.getvalue()
        self.assertTrue(msg.startswith("Elapsed time of 'wait' function:"), msg=msg)

    def test_decorator_with_custom_name(self):
        @timeti.profiler("Test function")
        def wait():
            time.sleep(0.01)

        with stdout_string() as buffer:
            wait()

        msg = buffer.getvalue()
        self.assertTrue(msg.startswith("Elapsed time of 'Test function' function:"), msg=msg)

    def test_missing_decorator_init(self):
        @timeti.profiler
        def wait(a, b):
            time.sleep(a * 0.001 + b)

        with stdout_string() as buffer:
            wait(1, b=0.001)
            wait(a=2, b=0.001)

        msg1, msg2 = buffer.getvalue().rstrip().split("\n")
        self.assertTrue(msg1.startswith("Elapsed time of 'wait' function:"), msg=msg1)
        self.assertTrue(msg2.startswith("Elapsed time of 'wait' function:"), msg=msg2)

    def test_silent_mode(self):
        @timeti.profiler(verbose=False)
        def wait():
            time.sleep(0.01)

        with stdout_string() as buffer:
            wait()

        msg = buffer.getvalue()
        self.assertEqual(msg, "")
