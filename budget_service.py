from budget_repo import get_budgets
from period import Period


class BudgetService(object):
    def total_amount(self, start, end):
        budgets = get_budgets()
        if len(budgets) > 0:
            period = Period(start, end)
            if period.end < budgets[0].first_day():
                return 0
            return self.interval_days(period)
        return 0

    @staticmethod
    def interval_days(period):
        delta = period.start - period.end
        return delta.days + 1
