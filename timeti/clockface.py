class Clockface:

    def __init__(self, timestamp):
        """Clock face for timestamp.

        Args:
            timestamp (float): initial timestamp. Default time.time().

        Examples:
            >>> Clockface(10)
            0d 0h 0m 10s 0ms
        """
        self.__timestamp = timestamp
        self.__minute_span= 60
        self.__hour_span = 60 * self.__minute_span
        self.__day_span = 24 * self.__hour_span

    @property
    def days(self):
        return round(self.__timestamp // self.__day_span)

    @property
    def hours(self):
        return ((self.__timestamp
                 - self.days * self.__day_span)
                // self.__hour_span)

    @property
    def minutes(self):
        return ((self.__timestamp
                 - self.days * self.__day_span
                 - self.hours * self.__hour_span)
                // self.__minute_span)

    @property
    def seconds(self):
        return int(self.__timestamp
                   - self.days * self.__day_span
                   - self.hours * self.__hour_span
                   - self.minutes * self.__minute_span)

    @property
    def miliseconds(self):
        return int(1_000 * (self.__timestamp - int(self.__timestamp)))

    def __str__(self):
        """Short clock fase strign."""
        if self.days > 0:
            return f'{self.days} days {self.hours} hours'

        elif self.hours > 0:
            return  f'{self.hours} hours {self.minutes} min'

        elif self.minutes > 0:
            return f'{self.minutes} min {self.seconds} sec'

        elif self.seconds > 0:
            return f'{self.seconds} sec {self.miliseconds} ms'

        else:
            return f"{self.miliseconds} ms"

    def __repr__(self):
        """Full clock face string."""
        return (f"{self.days}d "
                f"{self.hours}h "
                f"{self.minutes}m "
                f"{self.seconds}s "
                f"{self.miliseconds}ms")

if __name__ == '__main__':
    import doctest;
    print(doctest.testmod())
