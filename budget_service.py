from budget_repo import get_budgets
from period import Period


class BudgetService(object):
    def total_amount(self, start, end):
        budgets = get_budgets()
        if len(budgets) > 0:
            period = Period(start, end)
            budget = budgets[0]
            return self.overlapping_days(budget, period)
        return 0

    def overlapping_days(self, budget, period):
        if period.end < budget.first_day() or period.start > budget.last_day():
            return 0
        return self.interval_days(period)

    @staticmethod
    def interval_days(period):
        delta = period.start - period.end
        return delta.days + 1
