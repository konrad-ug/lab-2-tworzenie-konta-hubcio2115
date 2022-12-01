
import unittest
from parameterized import parameterized
from app.KontoFirmowe import KontoFirmowe


class TestCompanyLoan(unittest.TestCase):

    def setUp(self):
        self.konto = KontoFirmowe("Tesla", "1234567890")

    @parameterized.expand([
        ([5000, -1775, 1000], 1000, 500, True, 1500),
        ([500, 100], 1000, 500, False, 1000),
        ([-1775], 999, 500, False, 999),
        ([500, 200], 2000, 500, False, 2000),
        ([-1775], 400, 1000, False, 400),
        ([-1775, 1000, 1775], 500, 250, True, 750)
    ])
    def test_company_loan(self, history, saldo, loan, output, balance):

        self.konto.history = history
        self.konto.saldo = saldo
        test = self.konto.takeLoan(loan)
        self.assertEqual(test, output)
        self.assertEqual(self.konto.saldo, balance)
