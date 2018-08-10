
import unittest
from src.api import Api


class ApiTest(unittest.TestCase):

    @staticmethod
    def server_is_up():
        from os import system
        from sys import platform

        domain = Api().domain

        # Using Linux or OSX
        if platform == 'linux' or platform == 'darwin':
            can_ping = system(f"ping -c 1 {domain} 2>&1 > /dev/null")

        else:
            can_ping = system(f"ping /n 1 {domain} 2>&1")

        if can_ping is 0:
            return True

        return False

    def test_credential_store(self):
        if self.server_is_up():
            with Api('/account', auth=True) as api:
                new_user = {
                    'firstname': 'firstname',
                    'lastname': 'lastname',
                    'email': 'email@email.com',
                    'password': 'password'
                    }
                status, res = api.post(new_user)
                self.assertEqual(status, 200)

    def test_api_get(self):
        # self.assertTrue(self.server_is_up())
        with Api('/', domain='255.255.255.256') as api:
            self.assertTupleEqual(api.get(), (None, None))

    def test_api_post(self):
        with Api('/', domain='255.255.255.256') as api:
            self.assertTupleEqual(api.post(), (None, None))

    def test_api_put(self):
        with Api('/', domain='255.255.255.256') as api:
            self.assertTupleEqual(api.put(), (None, None))

    def test_api_delete(self):
        with Api('/', domain='255.255.255.256') as api:
            self.assertTupleEqual(api.delete(), (None, None))

