from src.clocks.clock import Clock


class WorkTimeClock(Clock):

    def __init__(self, initial_hours: int, initial_minutes: int, initial_seconds: int) -> None:
        super().__init__(initial_hours=initial_hours,
                         initial_minutes=initial_minutes,
                         initial_seconds=initial_seconds)

    def __repr__(self) -> str:
        return f"{self.get_hours():02.0f}:{self.get_minutes():02.0f}:{self.get_seconds():02.0f}"

    def count_time(self) -> None:

        """Main method to count and get information of the work time clock object
        about the work time itself."""

        if self.get_minutes() == 60:
            self.increase_hours_by()
            self.set_minutes_to()

        elif self.get_seconds() + 1 == 60:
            self.increase_minutes_by()
            self.set_seconds_to()

        else:
            self.increase_seconds_by()


