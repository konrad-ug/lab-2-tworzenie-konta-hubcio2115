import unittest
import requests


class TestApi(unittest.TestCase):
    account = {
        "account": "Dariusz",
        "surname": "Januszewski",
        "pesel": "61092909876"
    }

    def test_1_1_create_user(self):
        r = requests.post(
            "http://localhost:5000/accounts/createAccount", json=self.account)
        self.assertEqual(r.status_code, 201)

    def test_1_2_create_user_again(self):
        r = requests.post(
            "http://localhost:5000/accounts/createAccount", json=self.account)
        self.assertEqual(r.status_code, 400)

    def test_2_check_created_user(self):
        response = requests.get(
            "http://localhost:5000/accounts/account/"+self.account['pesel'])
        self.assertEqual(response.status_code, 200)
        res_body = response.json()
        self.assertEqual(res_body['name'], self.account['name'])
        self.assertEqual(res_body['surname'], self.account['surname'])
        self.assertEqual(res_body['pesel'], self.account['pesel'])

    def test_3_update_user(self):
        r = requests.put(
            "http://localhost:5000/acounts/account/"+self.account['pesel'], json={"surname": "Stachu"})
        self.assertEqual(r.status_code, 200)

    def test_4_delete_user(self):
        r = requests.delete(
            "http://localhost:5000/accounts/account/"+self.account['pesel'])
        self.assertEqual(r.status_code, 200)

    def test_5_check_deleted_user(self):
        response = requests.get(
            "http://localhost:5000/accounts/account/"+self.account['pesel'])
        self.assertEqual(response.status_code, 404)

    def test_6_update_deleted_user(self):
        r = requests.put(
            "http://localhost:5000/accounts/account/"+self.account['pesel'], json={"surname": "Stachu"})
        self.assertEqual(r.status_code, 404)
