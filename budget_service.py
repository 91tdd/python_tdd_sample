from budget_repo import get_budgets
from period import Period


class BudgetService(object):
    def total_amount(self, start, end):
        budgets = get_budgets()
        if len(budgets) > 0:
            period = Period(start, end)
            budget = budgets[0]
            return self.overlapping_amount(budget, period)
        return 0

    @staticmethod
    def overlapping_amount(budget, period):
        return period.overlapping_days(budget.create_period()) * budget.daily_amount()
