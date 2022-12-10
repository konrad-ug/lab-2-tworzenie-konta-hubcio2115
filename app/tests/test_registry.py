import unittest
from app.Account import Account
from app.AccountRegistry import AccountRegistry


class TestRegistry(unittest.TestCase):
    name = "Dariusz"
    surname = "Januszewski"
    pesel = "61092909876"

    @classmethod
    def setUpClass(cls):
        user = Account(cls.pesel, cls.name, cls.surname)
        AccountRegistry.addUser(user)

    def test_1_add_first_user(self):
        user = Account(self.name, self.surname, self.pesel)
        user1 = Account(self.name + "ddd", self.surname, self.pesel)
        AccountRegistry.addUser(user)
        AccountRegistry.addUser(user1)
        self.assertEqual(AccountRegistry.usersCount(), 3)

    def test_2_add_second_user(self):
        user = Account(self.name, self.surname, self.pesel)
        AccountRegistry.addUser(user)
        self.assertEqual(AccountRegistry.usersCount(), 4)

    def test_3_search_user(self):
        user = AccountRegistry.searchUser(self.pesel)

        self.assertEqual(user.name, self.name)  # type: ignore
        self.assertEqual(user.surname, self.surname)  # type: ignore
        self.assertEqual(user.pesel, self.pesel)  # type: ignore

    def test_4_search_user(self):
        user = AccountRegistry.searchUser("Stachu")
        self.assertEqual(user, None)

    @classmethod
    def tearDownClass(cls):
        AccountRegistry.users = []
