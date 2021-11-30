from datetime import date
from typing import List

from src.budget import Budget
from src.period import Period


def get_budgets() -> List[Budget]:
    pass


class BudgetService:
    def total_amount(self, start: date, end: date):
        budgets = get_budgets()
        if len(budgets) > 0:
            budget = budgets[0]
            period = Period(start, end)
            return self.get_overlapping_days(budget, period)
        return 0

    def get_overlapping_days(self, budget, period):
        if period.start > budget.last_day() or period.end < budget.first_day():
            return 0
        else:
            overlapping_start = period.start if period.start > budget.first_day() else budget.first_day()
            overlapping_end = period.end if period.end < budget.last_day() else budget.last_day()
            return (overlapping_end - overlapping_start).days + 1
