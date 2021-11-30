import calendar
from datetime import date, datetime

from src.period import Period


class Budget:
    def __init__(self, year_month, amount) -> None:
        super().__init__()
        self.amount = amount
        self.year_month = year_month

    def first_day(self):
        return datetime.strptime(self.year_month, '%Y%m').date()

    def last_day(self):
        year = self.first_day().year
        month = self.first_day().month
        days_in_month = calendar.monthrange(year, month)[1]
        return date(year, month, days_in_month)

    def create_period(self):
        return Period(self.first_day(), self.last_day())

    def days(self):
        return calendar.monthrange(self.first_day().year, self.first_day().month)[1]
