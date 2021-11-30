import unittest
from datetime import date
from unittest.mock import patch

from src.budget import Budget
from src.budget_service import BudgetService


class BudgetServiceTests(unittest.TestCase):
    def setUp(self):
        self.budget_service = BudgetService()
        get_budgets_patcher = patch('src.budget_service.get_budgets')
        self.fake_get_budgets = get_budgets_patcher.start()

    def test_no_budgets(self):
        self.total_amount_should_be(
            date(2020, 4, 1),
            date(2020, 4, 1),
            0)

    def test_query_single_budget_month(self):
        self.fake_get_budgets.return_value = [Budget('202004', 30)]
        self.total_amount_should_be(
            date(2020, 4, 1),
            date(2020, 4, 30),
            30)

    def test_query_single_day_of_budget(self):
        self.fake_get_budgets.return_value = [Budget('202004', 30)]
        self.total_amount_should_be(
            date(2020, 4, 1),
            date(2020, 4, 1),
            1)

    def test_period_no_overlap_before_budget_first_day(self):
        self.fake_get_budgets.return_value = [Budget('202004', 30)]
        self.total_amount_should_be(
            date(2020, 3, 31),
            date(2020, 3, 31),
            0)

    def total_amount_should_be(self, start, end, expected):
        self.assertEqual(expected, self.budget_service.total_amount(
            start,
            end,
        ))


if __name__ == '__main__':
    unittest.main()
