import unittest

from app.Konto import Konto
from app.KontoFirmowe import KontoFirmowe


class TestChangingSaldo(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "12345678901"

    companyName = "Firma"
    nip = "1234567890"

    def test_transactions_are_appended_to_history_in_personal_account(self):
        account = Konto(self.pesel, self.name, self.surname)
        account.saldo = 1000

        account.transferOut(300)
        account.transferIn(500)
        account.expressTransferOut(200)

        self.assertEqual(account.history, [-300, 500, -201],
                         "Transfery nie są poprawnie dodawane do historii transakcji")

    def test_transactions_are_appended_to_history_in_company_account(self):
        account = KontoFirmowe(self.nip, self.companyName)
        account.saldo = 1000

        account.transferOut(200)
        account.expressTransferOut(300)
        account.transferIn(500)

        self.assertEqual(account.history, [-200, -305, 500])
