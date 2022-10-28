import re


class Konto:
    def __init__(self, pesel, imie, nazwisko, coupon=""):
        self.imie = imie
        self.nazwisko = nazwisko

        self.checkIfPeselIsValid(pesel)
        self.checkIfPromoIsApplicable(coupon)

    def checkIfPeselIsValid(self, pesel):
        if (len(pesel) == 11):
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

    def checkIfPromoIsApplicable(self, coupon):
        isApplicable = re.search("PROM_", coupon) != None and len(
            coupon) == 8 and (int(self.pesel[2:4]) > 20 or int(self.pesel[0:2]) > 60)

        if (isApplicable):
            self.saldo = 50
        else:
            self.saldo = 0
