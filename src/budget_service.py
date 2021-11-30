from datetime import date
from typing import List

from src.budget import Budget


def get_budgets() -> List[Budget]:
    pass


class BudgetService:
    def total_amount(self, start: date, end: date):
        budgets = get_budgets()
        if len(budgets) > 0:
            if end < budgets[0].first_day():
                return 0
            delta = end - start
            return delta.days + 1
        return 0
