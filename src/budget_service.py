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
            return self.get_overlapping_days(budget, start, end)
        return 0

    def get_overlapping_days(self, budget, start, end):
        if start > budget.last_day() or end < budget.first_day():
            return 0
        else:
            overlapping_start = start if start > budget.first_day() else budget.first_day()
            overlapping_end = end if end < budget.last_day() else budget.last_day()
            return (overlapping_end - overlapping_start).days + 1
