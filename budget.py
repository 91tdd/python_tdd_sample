from datetime import date


class Budget(object):

    def __init__(self, year_month, amount) -> None:
        self.amount = amount
        self.year_month = year_month

    def first_day(self):
        return date(2020, 4, 1)
