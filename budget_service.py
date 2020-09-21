from budget_repo import get_budgets


class BudgetService(object):
    def total_amount(self, start, end):
        budgets = get_budgets()
        if len(budgets) > 0:
            delta = start - end
            return delta.days + 1
        return 0
