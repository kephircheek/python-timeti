import time
from contextlib import contextmanager
import warnings
from typing import List

from .utils import Clockface


class Stopwatch:
    def __init__(self):
        """Primitive stopwatch."""
        self.__start_time = time.time()
        self.__onpause = False
        self.__laps = []
        self.__pause_time = None

    def pause(self) -> Clockface:
        """Pause stopwatch."""
        if not self.__onpause:
            self.__onpause = True
            self.__pause_time = time.time()
        else:
            warnings.warn("Stopwatch already paused")
        return Clockface(self.__pause_time)

    @contextmanager
    def paused(self):
        """Pause stopwatch."""
        self.pause()
        yield self
        self.play()

    def play(self):
        """Continue stopwatch after a pause."""
        if self.__onpause:
            self.__start_time += time.time() - self.__pause_time
            self.__onpause = False

    def lap(self) -> Clockface:
        """Save time of lap."""
        self.__laps.append(self.timestamp - sum(self.__laps))
        if self.__onpause:
            warnings.warn("Stopwatch paused")
        return Clockface(self.__laps[-1])

    @property
    def laps(self) -> List:
        """List of lap time span."""
        return self.__laps

    def reset(self):
        """Reset stopwatch."""
        self.__init__()

    @property
    def timestamp(self) -> float:
        """Timestamp of stopwatch."""
        if self.__onpause:
            return self.__pause_time - self.__start_time

        return time.time() - self.__start_time

    @property
    def clockface(self) -> Clockface:
        """Clock face of stopwatch."""
        return Clockface(self.timestamp)

    def __str__(self):
        """Clock face as a string."""
        return str(self.clockface)

    def __repr__(self):
        """Summary of stopwatch."""
        return f"Stopwatch on {self.timestamp}"
