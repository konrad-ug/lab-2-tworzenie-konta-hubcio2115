import unittest

from app.Konto import Konto


class TestChangingSaldo(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "12345678901"

    def test_increases_on_transfer_in(self):
        account = Konto(self.pesel, self.name, self.surname)
        account.transferIn(100)

        self.assertEqual(
            account.saldo, 100, "Saldo nie zmienia się poprawnie przy przelewach przychodzących!")

    def test_decreases_on_transfer_out(self):
        account = Konto(self.pesel, self.name, self.surname)
        account.saldo = 100
        account.transferOut(99)

        self.assertEqual(
            account.saldo, 1, "Saldo nie zmienia się poprawnie przy przelewach przychodzących!")

    def test_transfer_declines_if_transfer_out_is_bigger_than_saldo(self):
        account = Konto(self.pesel, self.name, self.surname)
        account.transferOut(100)

        self.assertEqual(
            account.saldo, 0, "Saldo nie zmienia się poprawnie gdy przelew wychodzący jest większy od aktualnego salda konta!")
