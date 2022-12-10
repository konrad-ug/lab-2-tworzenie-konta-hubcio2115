
import unittest

from parameterized import parameterized  # type: ignore
from app.CompanyAccount import CompanyAccount


class TestCompanyLoan(unittest.TestCase):

    def setUp(self):
        self.konto = CompanyAccount("Tesla", "1234567890")

    @parameterized.expand([  # type: ignore
        ([5000, -1775, 1000], 1000, 500, True, 1500),
        ([500, 100], 1000, 500, False, 1000),
        ([-1775], 999, 500, False, 999),
        ([500, 200], 2000, 500, False, 2000),
        ([-1775], 400, 1000, False, 400),
        ([-1775, 1000, 1775], 500, 250, True, 750)
    ])  # type: ignore
    def test_company_loan(self, history: list[float], accountBalance: float, loan: float, output: bool, balance: float):

        self.konto.history = history
        self.konto.balance = accountBalance
        test = self.konto.takeLoan(loan)
        self.assertEqual(test, output)
        self.assertEqual(self.konto.balance, balance)
