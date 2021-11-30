class Period:
    def __init__(self, start, end) -> None:
        super().__init__()
        self.end = end
        self.start = start

    def get_overlapping_days(self, another):
        if self.start > another.end or self.end < another.start:
            return 0
        overlapping_start = self.start if self.start > another.start else another.start
        overlapping_end = self.end if self.end < another.end else another.end
        return (overlapping_end - overlapping_start).days + 1
