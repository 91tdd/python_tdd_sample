from budget_repo import get_budgets
from period import Period


class BudgetService(object):
    def total_amount(self, start, end):
        budgets = get_budgets()
        if len(budgets) > 0:
            period = Period(start, end)
            budget = budgets[0]
            another_period = Period(budget.first_day(), budget.last_day())
            return period.overlapping_days(another_period)
        return 0
