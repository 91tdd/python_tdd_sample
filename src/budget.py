from datetime import date


class Budget:
    def __init__(self, year_month, amount) -> None:
        super().__init__()
        self.amount = amount
        self.year_month = year_month

    def first_day(self):
        return date(2020, 4, 1)
