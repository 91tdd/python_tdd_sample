from datetime import date
from typing import List

from src.budget import Budget
from src.period import Period


def get_budgets() -> List[Budget]:
    pass


class BudgetService:
    def total_amount(self, start: date, end: date):
        period = Period(start, end)
        return sum(budget.overlapping_amount(period) for budget in (get_budgets()))
