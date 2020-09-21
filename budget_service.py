from budget_repo import get_budgets


class BudgetService(object):
    def total_amount(self, start, end):
        budgets = get_budgets()
        if len(budgets) > 0:
            return 1
        return 0
