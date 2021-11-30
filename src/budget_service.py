from datetime import date
from typing import List

from src.budget import Budget


def get_budgets() -> List[Budget]:
    pass


class BudgetService:
    def total_amount(self, start: date, end: date):
        budgets = get_budgets()
        if len(budgets) > 0:
            budget = budgets[0]
            overlapping_days = 0
            if start > budget.last_day() or end < budget.first_day():
                pass
            else:
                overlapping_start = start if start > budget.first_day() else budget.first_day()
                overlapping_end = end if end < budget.last_day() else budget.last_day()
                overlapping_days = (overlapping_end - overlapping_start).days + 1
            return overlapping_days
        return 0
