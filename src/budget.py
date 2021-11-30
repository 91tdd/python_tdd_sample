from datetime import date, datetime


class Budget:
    def __init__(self, year_month, amount) -> None:
        super().__init__()
        self.amount = amount
        self.year_month = year_month

    def first_day(self):
        return datetime.strptime(self.year_month, '%Y%m').date()
