from app.Account import Account


class AccountRegistry():
    users: list[Account] = []

    @classmethod
    def addUser(cls, user: Account):
        cls.users.append(user)

    @classmethod
    def searchUser(cls, pesel: str):
        for user in cls.users:
            if user.pesel == pesel:
                return user
        return None

    @classmethod
    def updateUser(cls, pesel: str, data):  # type: ignore
        user = cls.searchUser(pesel)

        if data.get('name'):  # type: ignore
            user.name = data['name']  # type: ignore
        if data.get('surname'):  # type: ignore
            user.surname = data['surname']  # type: ignore
        if data.get('pesel'):  # type: ignore
            user.pesel = data['pesel']  # type: ignore
        if data.get('balance'):  # type: ignore
            user.balance = data['balance']  # type: ignore

        return user, 200

    @classmethod
    def usersCount(cls):
        return len(cls.users)

    @classmethod
    def deleteUser(cls, pesel: str):
        for user in cls.users:
            if user.pesel == pesel:
                cls.users.remove(user)
                return "user deleted"
        return None
