import unittest
from datetime import date

from budget_service import BudgetService


class BudgetServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = BudgetService()

    def test_no_budgets(self):
        start = date(2020, 4, 1)
        end = date(2020, 4, 1)
        self.total_amount_should_be(0, start, end)

    def total_amount_should_be(self, expected, start, end):
        total_amount = self.service.total_amount(start, end)
        self.assertEqual(expected, total_amount)


if __name__ == '__main__':
    unittest.main()
