from flask import Flask, request, jsonify
from app.AccountRegistry import AccountRegistry
from app.Account import Account
app = Flask(__name__)


@app.route("/accounts/createAccount", methods=['POST'])
def createAccount():
    dane = request.get_json()
    if (AccountRegistry.searchUser(dane.get('pesel')) != None):  # type: ignore
        return "Konto o podanym numerze PESEL już istnieje", 400
    if (dane.get('name') and dane.get('surname') and dane.get('pesel')):  # type: ignore
        print(f"Request o stworzenie konta z danymi: {dane}")
        konto = Account(dane["name"], dane["surname"],  # type: ignore
                        dane["pesel"])  # type: ignore
        AccountRegistry.addUser(konto)
        return jsonify("Konto stworzone"), 201
    return "Niepoprawne dane!", 400


@app.route("/accounts/countAccounts", methods=['GET'])
def countAccounts():
    return jsonify(AccountRegistry.usersCount()), 200


@app.route("/accounts/account/<pesel>", methods=['GET'])
def searchAccountByPesel(pesel: str):
    if (AccountRegistry.searchUser(pesel) == None):
        return jsonify("Nie znaleziono konta!"), 404

    else:
        return jsonify(AccountRegistry.searchUser(pesel).__dict__), 200


@app.route("/konta/konto/<pesel>", methods=['PUT'])
def update_account(pesel: str):
    if (AccountRegistry.searchUser(pesel) == None):
        return jsonify("Nie znaleziono konta!"), 404
    else:
        dane = request.get_json()
        print(dane)
        AccountRegistry.updateUser(pesel, dane)  # type: ignore
        return jsonify("Konto zaktualizowane"), 200


@app.route("/konta/konto/<pesel>", methods=['DELETE'])
def delete_account(pesel: str):
    if (AccountRegistry.searchUser(pesel) == None):
        return jsonify("Nie znaleziono konta!"), 404

    else:
        AccountRegistry.deleteUser(pesel)
        return jsonify("Konto usunięte"), 200
