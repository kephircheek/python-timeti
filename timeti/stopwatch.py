import time

from timeti.utils import Clockface


class Stopwatch:

    def __init__(self):
        """Simple stopwatch."""
        self.__start_time = time.time()
        self.__onpause = False
        self.__laps = []

    def pause(self):
        """Pause stopwatch."""
        if not self.__onpause:
            self.__onpause = True
            self.__pause_time = time.time()
            return Clockface(self.__pause_time)

    def play(self):
        """Continue stopwatch after a pause."""
        if self.__onpause:
            self.__start_time += (time.time() - self.__pause_time)
            self.__onpause = False

    def lap(self):
        """Save time of lap."""
        if not self.__onpause:
            self.__laps.append(self.timestamp - sum(self.__laps))
            return Clockface(self.__laps[-1])

    @property
    def laps(self):
        """List of lap time span."""
        return self.__laps

    def reset(self):
        """Reset stopwatch."""
        self.__init__()

    @property
    def timestamp(self):
        """Timestamp of stopwatch."""
        if self.__onpause:
            return self.__paused_time - self.__start_time

        return time.time() - self.__start_time

    @property
    def clockface(self):
        """Clock face of stopwatch."""
        return Clockface(self.timestamp)

    def __str__(self):
        """Clock face as a string."""
        return str(self.clockface)

    def __repr__(self):
        """Summary of stopwatch."""
        return f"Stopwatch on {self.timestamp}"

