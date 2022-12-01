class Konto:
    def __init__(self, pesel: str, imie: str, nazwisko: str, coupon: str = "") -> None:
        self.imie = imie
        self.nazwisko = nazwisko

        self.checkIfPeselIsValid(pesel)
        self.checkIfPromoIsApplicable(coupon)

        self.history = []

        self.expressTransferOutCost = 1

    def checkIfPeselIsValid(self, pesel: str) -> None:
        if (len(pesel) == 11):
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

    def checkIfPromoIsApplicable(self, coupon) -> None:
        isApplicable = coupon[0:5] == "PROM_" != None and len(
            coupon) == 8 and (int(self.pesel[2:4]) > 20 or int(self.pesel[0:2]) > 60)

        if (isApplicable):
            self.saldo = 50.0
        else:
            self.saldo = 0.0

    def transferIn(self, amount: float) -> None:
        self.saldo += amount
        self.history.append(amount)

    def transferOut(self, amount: float) -> None:
        if (self.saldo >= amount):
            self.saldo -= amount

        self.history.append(-amount)

    def expressTransferOut(self, amount: float) -> None:
        calculatedAmount = amount + self.expressTransferOutCost

        if (self.saldo >= amount):
            self.saldo -= calculatedAmount

        self.history.append(-calculatedAmount)

    def takeLoan(self, amount):
        lastFiveTransactions = self.history[-5:]

        if len(lastFiveTransactions) >= 5 and sum(lastFiveTransactions) > amount and all(elem > 0 for elem in lastFiveTransactions[-3:]):
            self.saldo += amount
            return True
        return False
