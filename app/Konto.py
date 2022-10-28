import re


class Konto:
    def __init__(self, pesel: str, imie: str, nazwisko: str, coupon: str = ""):
        self.imie: str = imie
        self.nazwisko: str = nazwisko

        self.checkIfPeselIsValid(pesel)
        self.checkIfPromoIsApplicable(coupon)

    def checkIfPeselIsValid(self, pesel: str):
        if (len(pesel) == 11):
            self.pesel: str = pesel
        else:
            self.pesel: str = "Niepoprawny pesel!"

    def checkIfPromoIsApplicable(self, coupon):
        isApplicable = re.search("PROM_", coupon) != None and len(
            coupon) == 8 and (int(self.pesel[2:4]) > 20 or int(self.pesel[0:2]) > 60)

        if (isApplicable):
            self.saldo: float = 50
        else:
            self.saldo: float = 0

    def transferIn(self, amount: float):
        self.saldo += amount

    def transferOut(self, amount: float):
        if (self.saldo >= amount):
            self.saldo -= amount
