import unittest
from datetime import date


class BudgetService(object):
    def total_amount(self, start, end):
        pass


class BudgetServiceTests(unittest.TestCase):
    def test_no_budgets(self):
        budget_service = BudgetService()
        start = date(2020, 4, 1)
        end = date(2020, 4, 1)
        total_amount = budget_service.total_amount(start, end)
        self.assertEqual(0, total_amount)


if __name__ == '__main__':
    unittest.main()
