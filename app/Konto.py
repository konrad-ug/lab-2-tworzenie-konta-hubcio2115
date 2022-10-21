import re


class Konto:
    def __init__(self, pesel, imie, nazwisko, coupon=""):
        self.imie = imie
        self.nazwisko = nazwisko

        if (len(pesel) == 11):
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

        if (re.search("PROM_", coupon) != None and len(coupon) == 8):
            self.saldo = 50
        else:
            self.saldo = 0
