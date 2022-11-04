import unittest

from app.KontoFirmowe import KontoFirmowe


class TestCreateCompanyBankAccount(unittest.TestCase):
    nip = "1234567890"
    name = "firma"
    initialSaldo = 0.0

    def test_creating_company_bank_account(self):
        account = KontoFirmowe(self.nip, self.name)

        self.assertEqual(account.name, self.name,
                         "Na koncie firmowym brakuje wartości name!")
        self.assertEqual(account.nip, self.nip,
                         "Na koncie firmowym brakuje wartości nip!")
        self.assertEqual(account.saldo, self.initialSaldo,
                         "Saldo konta firmowego nie jest równe 0 przy jego stworzeniu!")

    # def test_when_nip_is_not_ten_in_length(self):
    #     account = KontoFirmowe("1", self.name)

    #     self.assertEqual(account.nip, "Niepoprawny NIP!",
    #                      'Pesel nie ma wartości "Niepoprawny pesel", gdy podamy pesel w złym formacie!')
