class Period:
    def __init__(self, start, end) -> None:
        super().__init__()
        self.end = end
        self.start = start

    def get_overlapping_days(self, budget):
        if self.start > budget.last_day() or self.end < budget.first_day():
            return 0
        else:
            overlapping_start = self.start if self.start > budget.first_day() else budget.first_day()
            overlapping_end = self.end if self.end < budget.last_day() else budget.last_day()
            return (overlapping_end - overlapping_start).days + 1
