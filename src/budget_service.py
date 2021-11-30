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
            daily_amount = budget.daily_amount()
            period = Period(start, end)
            return period.get_overlapping_days(budget.create_period()) * daily_amount
        return 0
