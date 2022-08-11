import unittest
from time import sleep

from timeti.stopwatch import Stopwatch

class TestStopwatch(unittest.TestCase):

    def test_timestamp(self):
        sw = Stopwatch()
        sleep(1)
        return self.assertEqual(round(sw.timestamp), 1)

    def test_pause_play(self):
        sw = Stopwatch()
        sleep(1)
        sw.pause()
        sleep(3)
        sw.play()
        sleep(1)
        return self.assertEqual(round(sw.timestamp), 2)

    def test_laps(self):
        sw = Stopwatch()
        sw.lap()
        sleep(1)
        sw.lap()
        sleep(2)
        sw.lap()
        return self.assertListEqual(
            [len(sw.laps), sum(list(map(round, sw.laps)))],
            [3, 3]
        )

    def test_reset(self):
        sw = Stopwatch()
        sleep(1)
        sw.lap()
        sleep(1)
        sw.lap()
        sw.reset()
        sleep(2)
        sw.lap()
        return self.assertListEqual(
            [round(sw.timestamp), sum(list(map(round, sw.laps)))],
            [2, 2]
        )

    def test_pause_play_laps(self):
        sw = Stopwatch()
        sw.lap()
        sleep(1)
        sw.pause()
        sw.lap()
        sw.play()
        sw.lap()
        sw.lap()
        return self.assertListEqual(
            [len(sw.laps), sum(list(map(round, sw.laps)))],
            [3, 1]
        )

    def test_clockface(self):
        sw = Stopwatch()
        sleep(66.6)
        return self.assertEqual(
            f'{int(sw.clockface.minutes)} m '
            f'{int(sw.clockface.seconds)} s '
            f'{int(round(sw.clockface.miliseconds, -2))} ms',
            '1 m 6 s 600 ms'
        )
