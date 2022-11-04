import unittest

from app.Konto import Konto
from app.KontoFirmowe import KontoFirmowe


class TestChangingSaldo(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "12345678901"

    companyName = "Firma"
    nip = "1234567890"

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

    def test_express_transfer_properly_withdraws_money_from_personal_account(self):
        account = Konto(self.pesel, self.name, self.surname)
        account.saldo = 100
        account.expressTransferOut(50)

        self.assertEqual(
            account.saldo, 49, "Ekspres ekspresowy nie poprawnie pobiera opłatę za wykonanie operacji na koncie konsumenckim!")

    def test_express_transfer_properly_withdraws_money_from_company_account(self):
        account = KontoFirmowe(self.nip, self.name)
        account.saldo = 100
        account.expressTransferOut(50)

        self.assertEqual(
            account.saldo, 45, "Ekspres ekspresowy nie poprawnie pobiera opłatę za wykonanie operacji na koncie firmowym!")

    def test_express_transfer_properly_sets_the_deficit_when_payment_fee_exceeds_personal_account_balance(self):
        account = Konto(self.pesel, self.name, self.surname)
        account.saldo = 100
        account.expressTransferOut(100)

        self.assertEqual(
            account.saldo, -1, "Opłata za transfer ekspresowy na koncie konsumenckim nie nalicza odpowiedniego deficytu gdy opłata jest większa niż saldo!")

    def test_express_transfer_properly_sets_the_deficit_when_payment_fee_exceeds_company_account_balance(self):
        account = KontoFirmowe(self.nip, self.name)
        account.saldo = 100
        account.expressTransferOut(100)

        self.assertEqual(
            account.saldo, -5, "Opłata za transfer ekspresowy na koncie firmowym nie nalicza odpowiedniego deficytu gdy opłata jest większa niż saldo!")
