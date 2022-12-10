from parameterized import parameterized  # type: ignore
import unittest

from app.Account import Account


class TestTakingLoansOnConsumerAccounts(unittest.TestCase):
    def setUp(self):
        self.account = Account("Mariusz", "Pudzianowski", "01321007158")

    @parameterized.expand([  # type: ignore
        ([100, 100, 100, 400, 500], 500, True, 500),
        ([-100, 100, 100, -100], 500, False, 0),
        ([100, -100, 100, 200, 500], 500, True, 500),
        ([-1000], 20, False, 0),
        ([-50, -100, 100, 150, -300], 500, False, 0),
        ([500, 200], 500, False, 0),
    ])  # type: ignore
    def test_loans(self, history: list[float], loan: float, output: bool, balance: bool):
        self.account.history = history

        test = self.account.takeLoan(loan)

        self.assertEqual(test, output)
        self.assertEqual(self.account.balance, balance)
