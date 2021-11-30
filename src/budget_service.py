from datetime import date
from typing import List

from src.budget import Budget


def get_budgets() -> List[Budget]:
    pass


class Period:
    def __init__(self, start, end) -> None:
        super().__init__()
        self.end = end
        self.start = start


class BudgetService:
    def total_amount(self, start: date, end: date):
        budgets = get_budgets()
        if len(budgets) > 0:
            budget = budgets[0]
            return self.get_overlapping_days(budget, start, end)
        return 0

    def get_overlapping_days(self, budget, start, end):
        period = Period(start, end)
        temp_start = period.start
        temp_end = period.end
        if temp_start > budget.last_day() or temp_end < budget.first_day():
            return 0
        else:
            overlapping_start = temp_start if temp_start > budget.first_day() else budget.first_day()
            overlapping_end = temp_end if temp_end < budget.last_day() else budget.last_day()
            return (overlapping_end - overlapping_start).days + 1
