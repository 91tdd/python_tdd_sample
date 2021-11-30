import unittest
from datetime import date

from src.budget_service import BudgetService


class BudgetServiceTests(unittest.TestCase):
    def setUp(self):
        self.budget_service = BudgetService()

    def test_no_budgets(self):
        self.total_amount_should_be(
            date(2020, 4, 1),
            date(2020, 4, 1),
            0)

    def total_amount_should_be(self, start, end, expected):
        self.assertEqual(expected, self.budget_service.total_amount(
            start,
            end,
        ))


if __name__ == '__main__':
    unittest.main()
