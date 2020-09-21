from budget_repo import get_budgets
from period import Period


class BudgetService(object):
    def total_amount(self, start, end):
        budgets = get_budgets()
        if len(budgets) > 0:
            period = Period(start, end)
            budget = budgets[0]
            daily_amount = budget.amount / budget.total_days()
            another_period = budget.create_period()
            overlapping_days = period.overlapping_days(another_period)
            return overlapping_days * daily_amount
        return 0
