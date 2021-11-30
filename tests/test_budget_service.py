import unittest
from datetime import date


class BudgetService:
    def total_amount(self, start: date, end: date):
        return 0


class BudgetServiceTests(unittest.TestCase):
    def test_no_budgets(self):
        budget_service = BudgetService()
        self.assertEqual(0, budget_service.total_amount(
            date(2020, 4, 1),
            date(2020, 4, 1),
        ))


if __name__ == '__main__':
    unittest.main()
