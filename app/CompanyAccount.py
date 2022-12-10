from app.Account import Account


class CompanyAccount(Account):
    def __init__(self, nip: str, name: str) -> None:
        self.name = name
        self.balance = 0.0

        self.expressTransferOutCost = 5

        self.history: list[float] = []

        if (len(nip) != 10):
            self.nip = "Niepoprawny NIP!"
        else:
            self.nip = nip

    def takeLoan(self, amount: float):
        isSaldoMoreThanTwoTimesTheAmountOfLoan = amount * 2 <= self.balance

        try:
            self.history.index(-1775)

            if isSaldoMoreThanTwoTimesTheAmountOfLoan:
                self.balance += amount
                return True
            else:
                return False

        except:
            return False
