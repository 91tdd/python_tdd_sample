class Period(object):
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def overlapping_days(self, budget):
        if self.end < budget.first_day() or self.start > budget.last_day():
            return 0
        return self.interval_days(self)

    @staticmethod
    def interval_days(period):
        delta = period.start - period.end
        return delta.days + 1
