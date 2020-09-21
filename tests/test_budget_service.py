import unittest
from datetime import date
from unittest.mock import patch

from budget import Budget
from budget_service import BudgetService


class BudgetServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = BudgetService()
        budget_repo_patcher = patch('budget_service.get_budgets')
        self.fake_get_budgets = budget_repo_patcher.start()

    def tearDown(self) -> None:
        patch.stopall()

    def test_no_budgets(self):
        start = date(2020, 4, 1)
        end = date(2020, 4, 1)
        self.total_amount_should_be(0, start, end)

    def test_period_inside_budget_month(self):
        self.fake_get_budgets.return_value = [
            Budget('202004', 30),
        ]

        start = date(2020, 4, 1)
        end = date(2020, 4, 1)
        self.total_amount_should_be(1, start, end)

    def test_period_without_overlap_before_budget_first_day(self):
        self.fake_get_budgets.return_value = [
            Budget('202004', 30),
        ]

        start = date(2020, 3, 31)
        end = date(2020, 3, 31)
        self.total_amount_should_be(0, start, end)

    def test_period_without_overlap_after_budget_last_day(self):
        self.fake_get_budgets.return_value = [
            Budget('202004', 30),
        ]

        start = date(2020, 5, 1)
        end = date(2020, 5, 1)
        self.total_amount_should_be(0, start, end)

    def test_period_overlap_budget_first_day(self):
        self.fake_get_budgets.return_value = [
            Budget('202004', 30),
        ]

        start = date(2020, 3, 31)
        end = date(2020, 4, 1)
        self.total_amount_should_be(1, start, end)

    def total_amount_should_be(self, expected, start, end):
        total_amount = self.service.total_amount(start, end)
        self.assertEqual(expected, total_amount)


if __name__ == '__main__':
    unittest.main()
