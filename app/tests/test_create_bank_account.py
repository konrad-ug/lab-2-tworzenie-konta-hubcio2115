import unittest

from app.Account import Account


class TestCreateBankAccount(unittest.TestCase):
    elderlyPesel = "59013456789"

    name = "Dariusz"
    surname = "Januszewski"
    pesel = "12345678901"
    initialSaldo = 0

    coupon = "PROM_XYZ"

    def test_creating_account(self):
        firstAccount = Account(self.pesel, self.name, self.surname)
        self.assertEqual(firstAccount.pesel, self.pesel,
                         "Pesel nie został zapisany!")
        self.assertEqual(firstAccount.name, self.name,
                         "Imie nie zostało zapisane!")
        self.assertEqual(firstAccount.surname, self.surname,
                         "Nazwisko nie zostało zapisane!")
        self.assertEqual(firstAccount.balance, self.initialSaldo,
                         "Saldo nie jest zerowe!")

    # tutaj proszę dodawać nowe testy

    def test_when_pesel_is_not_eleven_in_length(self):
        badPesel = "1"
        account = Account(badPesel, self.name, self.surname)
        self.assertEqual(account.pesel, "Niepoprawny pesel!",
                         'Pesel nie ma wartości "Niepoprawny pesel", gdy podamy pesel w złym formacie!')

    def test_balance_equals_to_fifty_when_coupon_applied(self):
        account = Account(self.pesel, self.name, self.surname, self.coupon)
        self.assertEqual(account.balance, 50,
                         "Saldo nie równa się 50 po zaaplikowaniu kuponu!")

    def test_balance_equals_to_zero_when_coupon_is_invalid(self):
        invalidMessage = "Saldo nie równa się 0 po zaaplikowaniu błędnego lub pustego kuponu!"

        account = Account(self.pesel, self.name,
                          self.surname, "PORM_XYZ")
        self.assertEqual(
            account.balance, 0, invalidMessage)

        account = Account(self.pesel, self.name,
                          self.surname)
        self.assertEqual(account.balance, 0, invalidMessage)

    def test_coupon_is_not_applied_for_people_elderly(self):
        account = Account(self.elderlyPesel, self.name,
                          self.surname, self.coupon)

        self.assertEqual(account.balance, 0,
                         "Kupon nie powinien być ważny dla osób urodzonych po 1960!")
