from budget_repo import get_budgets
from period import Period


class BudgetService(object):
    def total_amount(self, start, end):
        period = Period(start, end)
        return sum(budget.overlapping_amount(period) for budget in get_budgets())
        # total_amount = 0
        # for budget in get_budgets():
        #     total_amount += budget.overlapping_amount(period)
        #
        # return total_amount
