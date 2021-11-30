from datetime import date
from typing import List

from src.budget import Budget
from src.period import Period


def get_budgets() -> List[Budget]:
    pass


class BudgetService:
    def total_amount(self, start: date, end: date):
        budgets = get_budgets()
        period = Period(start, end)
        return sum(budget.overlapping_amount(period) for budget in budgets)
        # if len(budgets) > 0:
        #     budget = budgets[0]
        #     period = Period(start, end)
        #     return budget.overlapping_amount(period)
        # return 0
