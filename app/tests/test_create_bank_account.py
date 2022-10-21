import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("12345678901", "Dariusz", "Januszewski")
        self.assertEqual(pierwsze_konto.pesel, "12345678901",
                         "Pesel nie został zapisany!")
        self.assertEqual(pierwsze_konto.imie, "Dariusz",
                         "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski",
                         "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    # tutaj proszę dodawać nowe testy

    def test_when_pesel_is_not_eleven_in_length(self):
        account = Konto("1", "Dariusz", "Januszkiewicz")
        self.assertEqual(account.pesel, "Niepoprawny pesel!",
                         'Pesel nie ma wartości "Niepoprawny pesel", gdy podamy pesel w złym formacie!')
