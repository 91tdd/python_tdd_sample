class Period(object):
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def overlapping_days(self, budget):
        if self.end < budget.first_day() or self.start > budget.last_day():
            return 0
        overlapping_start = self.start if self.start > budget.first_day() else budget.first_day()
        overlapping_end = self.end if self.end < budget.last_day() else budget.last_day()
        delta = overlapping_start - overlapping_end
        return delta.days + 1
