from parameterized import parameterized
import unittest

from app.Konto import Konto


class TestTakingLoansOnConsumerAccounts(unittest.TestCase):
    def setUp(self):
        self.account = Konto("Mariusz", "Pudzianowski", "01321007158")

    @parameterized.expand([
        ([100, 100, 100, 400, 500], 500, True, 500),
        ([-100, 100, 100, -100], 500, False, 0),
        ([100, -100, 100, 200, 500], 500, True, 500),
        ([-1000], 20, False, 0),
        ([-50, -100, 100, 150, -300], 500, False, 0),
        ([500, 200], 500, False, 0),
    ])
    def test_loans(self, history, loan, output, balance):
        self.account.history = history

        test = self.account.takeLoan(loan)

        self.assertEqual(test, output)
        self.assertEqual(self.account.saldo, balance)
