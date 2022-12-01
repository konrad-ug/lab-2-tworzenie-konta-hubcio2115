import unittest
from ..Konto import Konto
from .. RejestrKont import RejestrKont


class TestRegister(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "61092909876"

    @classmethod
    def setUpClass(cls):
        user = Konto(cls.imie, cls.nazwisko, cls.pesel)
        RejestrKont.addUser(user)

    def test_add_first_user(self):
        user = Konto(self.imie, self.nazwisko, self.pesel)
        user1 = Konto(self.imie + "ddd", self.nazwisko, self.pesel)
        RejestrKont.addUser(user)
        RejestrKont.addUser(user1)
        self.assertEqual(RejestrKont.usersCount(), 3)

    def test_add_second_user(self):
        user = Konto(self.imie, self.nazwisko, self.pesel)
        RejestrKont.addUser(user)
        self.assertEqual(RejestrKont.usersCount(), 4)

    def test_search_user(self):
        user = RejestrKont.searchUser(self.pesel)
        self.assertEqual(user.imie, self.imie)
        self.assertEqual(user.nazwisko, self.nazwisko)
        self.assertEqual(user.pesel, self.pesel)

    def test_search_user(self):
        user = RejestrKont.searchUser("Stachu")
        self.assertEqual(user, None)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.users = []
