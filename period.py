class Period(object):
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def overlapping_days(self, budget):
        another_period = Period(budget.first_day(), budget.last_day())
        if self.end < another_period.start or self.start > another_period.end:
            return 0
        overlapping_start = self.start if self.start > another_period.start else another_period.start
        overlapping_end = self.end if self.end < another_period.end else another_period.end
        delta = overlapping_start - overlapping_end
        return delta.days + 1
