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
        return date(first_day.year, first_day.month, self.total_days())

    def create_period(self):
        return Period(self.first_day(), self.last_day())

    def total_days(self):
        first_day = self.first_day()
        return calendar.monthrange(first_day.year, first_day.month)[1]

    def daily_amount(self):
        return self.amount / self.total_days()
