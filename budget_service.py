from budget_repo import get_budgets
from period import Period


class BudgetService(object):
    def total_amount(self, start, end):
        period = Period(start, end)
        budgets = get_budgets()
        total_amount = 0
        for budget in budgets:
            total_amount += budget.overlapping_amount(period)

        return total_amount
        # if len(budgets) > 0:
        #     period = Period(start, end)
        #     budget = budgets[0]
        #     return budget.overlapping_amount(period)
        # return 0
