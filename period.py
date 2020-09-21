class Period(object):
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def overlapping_days(self, another_period):
        if self.start > self.end or self.without_overlapping(another_period):
            return 0

        overlapping_start = self.start if self.start > another_period.start else another_period.start
        overlapping_end = self.end if self.end < another_period.end else another_period.end
        delta = overlapping_end - overlapping_start
        return delta.days + 1

    def without_overlapping(self, another_period):
        return self.end < another_period.start or self.start > another_period.end
