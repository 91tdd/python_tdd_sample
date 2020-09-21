import calendar
from datetime import date, datetime

from period import Period


class Budget(object):

    def __init__(self, year_month, amount) -> None:
        self.amount = amount
        self.year_month = year_month

    def first_day(self):
        return datetime.strptime(self.year_month, '%Y%m').date()

    def last_day(self):
        first_day = self.first_day()
        year = first_day.year
        month = first_day.month
        days_in_month = calendar.monthrange(year, month)[1]
        return date(year, month, days_in_month)

    def create_period(self):
        another_period = Period(self.first_day(), self.last_day())
        return another_period

    def total_days(self):
        first_day = self.first_day()
        year = first_day.year
        month = first_day.month
        days_in_month = calendar.monthrange(year, month)[1]
        return days_in_month
