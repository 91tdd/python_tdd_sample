from budget_repo import get_budgets
from period import Period


class BudgetService(object):
    def total_amount(self, start, end):
        budgets = get_budgets()
        if len(budgets) > 0:
            period = Period(start, end)
            budget = budgets[0]
            daily_amount = self.daily_amount(budget)
            overlapping_days = period.overlapping_days(budget.create_period())
            return overlapping_days * daily_amount
        return 0

    @staticmethod
    def daily_amount(budget):
        daily_amount = budget.amount / budget.total_days()
        return daily_amount
