import time
import unittest
import warnings
from time import sleep

from timeti.stopwatch import Stopwatch


class TestStopwatch(unittest.TestCase):
    def test_timestamp(self):
        sw = Stopwatch()
        sleep(0.01)
        self.assertGreaterEqual(round(sw.timestamp, 3), 0.01)
        self.assertLess(round(sw.timestamp, 3), 0.015)

    def test_pause_play(self):
        sw = Stopwatch()
        sleep(0.01)
        sw.pause()
        sleep(0.02)
        sw.play()
        sleep(0.01)
        self.assertLess(round(sw.timestamp, 3), 0.03)

    def test_laps(self):
        sw = Stopwatch()
        sw.lap()
        sleep(0.01)
        sw.lap()
        sleep(0.02)
        sw.lap()
        self.assertEqual(len(sw.laps), 3)
        self.assertLess(round(sum(sw.laps).timestamp, 3), 0.04)

    def test_reset(self):
        sw = Stopwatch()
        sleep(0.01)
        sw.lap()
        sleep(0.01)
        sw.lap()
        sw.reset()
        sleep(0.02)
        sw.lap()
        self.assertLess(round(sw.timestamp, 3), 0.03)
        self.assertLess(round(sum(sw.laps).timestamp, 3), 0.03)

    def test_double_pause(self):
        sw = Stopwatch()
        sw.pause()
        with warnings.catch_warnings(record=True) as w:
            sw.pause()
            self.assertEqual(len(w), 1)
            self.assertTrue(issubclass(w[-1].category, UserWarning))
            self.assertEqual(str(w[-1].message), "Stopwatch already paused")

    def test_pause_play_laps(self):
        sw = Stopwatch()
        sw.lap()
        sleep(0.01)
        sw.pause()
        with warnings.catch_warnings(record=True) as w:
            sw.lap()
            self.assertEqual(len(w), 1)
            self.assertTrue(issubclass(w[-1].category, UserWarning))
            self.assertEqual(str(w[-1].message), "Stopwatch paused")
        sw.play()
        sw.lap()
        sw.lap()
        self.assertEqual(len(sw.laps), 4)
        self.assertLess(round(sum(sw.laps).timestamp, 3), 0.02)

    def test_clockface(self):
        sw = Stopwatch()
        sw._start_time = time.time() - 67.7
        self.assertEqual(
            f"{int(sw.clockface.minutes)} m "
            f"{int(sw.clockface.seconds)} s "
            f"{int(round(sw.clockface.milliseconds, -2))} ms",
            "1 m 7 s 700 ms",
        )
