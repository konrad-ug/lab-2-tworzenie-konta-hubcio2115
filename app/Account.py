class Account:
    def __init__(self, pesel: str, name: str, surname: str, coupon: str = "") -> None:
        self.name = name
        self.surname = surname

        self.checkIfPeselIsValid(pesel)
        self.checkIfPromoIsApplicable(coupon)

        self.history: list[float] = []

        self.expressTransferOutCost = 1

    def checkIfPeselIsValid(self, pesel: str) -> None:
        if (len(pesel) == 11):
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

    def checkIfPromoIsApplicable(self, coupon: str) -> None:
        isApplicable = coupon[0:5] == "PROM_" and len(
            coupon) == 8 and (int(self.pesel[2:4]) > 20 or int(self.pesel[0:2]) > 60)

        if (isApplicable):
            self.balance = 50.0
        else:
            self.balance = 0.0

    def transferIn(self, amount: float) -> None:
        self.balance += amount
        self.history.append(amount)

    def transferOut(self, amount: float) -> None:
        if (self.balance >= amount):
            self.balance -= amount

        self.history.append(-amount)

    def expressTransferOut(self, amount: float) -> None:
        calculatedAmount = amount + self.expressTransferOutCost

        if (self.balance >= amount):
            self.balance -= calculatedAmount

        self.history.append(-calculatedAmount)

    def takeLoan(self, amount: float):
        lastFiveTransactions = self.history[-5:]

        isHistoryLongEnough = len(lastFiveTransactions) >= 5
        isSumOfLastTransactionsGreaterThanAmountOfTheLoan = sum(
            lastFiveTransactions) > amount
        areThreeLastTransactionsTransferIns = all(
            elem > 0 for elem in lastFiveTransactions[-3:])

        isApplicableForLoan = isHistoryLongEnough and isSumOfLastTransactionsGreaterThanAmountOfTheLoan and areThreeLastTransactionsTransferIns
        if isApplicableForLoan:
            self.balance += amount
            return True
        return False
