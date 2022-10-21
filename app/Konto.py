class Konto:
    def __init__(self, pesel, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0

        if (len(pesel) == 11):
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"
