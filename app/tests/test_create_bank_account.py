import unittest

from app.Konto import Konto


class TestCreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "12345678901"
    initialSaldo = 0
    coupon = "PROM_XYZ"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.pesel, self.name, self.surname)
        self.assertEqual(pierwsze_konto.pesel, self.pesel,
                         "Pesel nie został zapisany!")
        self.assertEqual(pierwsze_konto.imie, self.name,
                         "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.surname,
                         "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, self.initialSaldo,
                         "Saldo nie jest zerowe!")

    # tutaj proszę dodawać nowe testy

    def test_when_pesel_is_not_eleven_in_length(self):
        badPesel = "1"
        account = Konto(badPesel, self.name, self.surname)
        self.assertEqual(account.pesel, "Niepoprawny pesel!",
                         'Pesel nie ma wartości "Niepoprawny pesel", gdy podamy pesel w złym formacie!')

    def test_saldo_equals_to_fifty_when_coupon_applied(self):
        account = Konto(self.pesel, self.name, self.surname, self.coupon)
        self.assertEqual(account.saldo, 50,
                         "Saldo nie równa się 50 po zaaplikowaniu kuponu!")
