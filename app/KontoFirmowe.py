from app.Konto import Konto


class KontoFirmowe(Konto):
    def __init__(self, nip: str, name: str) -> None:
        self.name = name
        self.saldo = 0.0

        self.expressTransferOutCost = 5

        self.history = []

        if (len(nip) != 10):
            self.nip = "Niepoprawny NIP!"
        else:
            self.nip = nip

    def takeLoan(self, amount):
        isSaldoMoreThanTwoTimesTheAmountOfLoan = amount * 2 <= self.saldo

        try:
            self.history.index(-1775)

            if isSaldoMoreThanTwoTimesTheAmountOfLoan:
                self.saldo += amount
                return True
            else:
                return False

        except:
            return False
