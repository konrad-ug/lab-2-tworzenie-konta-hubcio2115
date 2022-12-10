import unittest

from app.CompanyAccount import CompanyAccount


class TestCreateCompanyBankAccount(unittest.TestCase):
    nip = "1234567890"
    name = "firma"
    initialSaldo = 0.0

    def test_creating_company_bank_account(self):
        account = CompanyAccount(self.nip, self.name)

        self.assertEqual(account.name, self.name,
                         "Na koncie firmowym brakuje wartości name!")
        self.assertEqual(account.nip, self.nip,
                         "Na koncie firmowym brakuje wartości nip!")
        self.assertEqual(account.balance, self.initialSaldo,
                         "Saldo konta firmowego nie jest równe 0 przy jego stworzeniu!")

    def test_when_nip_is_not_ten_in_length(self):
        account = CompanyAccount("1", self.name)

        self.assertEqual(account.nip, "Niepoprawny NIP!",
                         'Pesel nie ma wartości "Niepoprawny pesel", gdy podamy pesel w złym formacie!')
