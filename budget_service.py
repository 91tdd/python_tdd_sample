from budget_repo import get_budgets
from period import Period


class BudgetService(object):
    def total_amount(self, start, end):
        budgets = get_budgets()
        if len(budgets) > 0:
            period = Period(start, end)
            budget = budgets[0]
            another_period = self.create_period(budget)
            return period.overlapping_days(another_period)
        return 0

    def create_period(self, budget):
        another_period = Period(budget.first_day(), budget.last_day())
        return another_period
