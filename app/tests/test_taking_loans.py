
import unittest

from app.Konto import Konto


class TestTakingLoansOnConsumerAccounts(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "12345678901"

    def test_consumer_loan_returns_true_when_successful(self):
        account = Konto(self.pesel, self.name, self.surname)

        for _ in range(5):
            account.transferIn(300)

        self.assertTrue(account.takeLoan(100),
                        'takeLoan method does not return true when successful')

    def test_consumer_loan_returns_false_when_unsuccessful(self):
        account = Konto(self.pesel, self.name, self.surname)

        for _ in range(2):
            account.transferIn(200)
            account.transferOut(100)
            account.transferIn(50)

        self.assertFalse(account.takeLoan(
            1000), 'takeLoan method does not return false when unsuccessful')

    def test_consumer_loan_adds_expected_amount_to_the_account_when_it_is_successful(self):
        account = Konto(self.pesel, self.name, self.surname)

        for _ in range(5):
            account.transferIn(300)

        account.takeLoan(100)

        self.assertEqual(account.saldo, 1600,
                         'takeLoan adds expected amount to the account when applicable')

    def test_consumer_loan_does_not_add_expected_amount_to_the_account_when_it_is_unsuccessful(self):
        account = Konto(self.pesel, self.name, self.surname)

        for _ in range(2):
            account.transferIn(200)
            account.transferOut(100)
            account.transferIn(50)

        account.takeLoan(1000)

        self.assertEqual(account.saldo, 300,
                         'takeLoan does not add expected amount to the account when not applicable')
