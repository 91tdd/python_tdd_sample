class Period(object):
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def overlapping_days(self, budget):
        another_period = Period(budget.first_day(), budget.last_day())
        first_day = another_period.start
        last_day = another_period.end
        if self.end < first_day or self.start > last_day:
            return 0
        overlapping_start = self.start if self.start > first_day else first_day
        overlapping_end = self.end if self.end < last_day else last_day
        delta = overlapping_start - overlapping_end
        return delta.days + 1
