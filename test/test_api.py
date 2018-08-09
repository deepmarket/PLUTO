
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
        # TODO
        ...

    def test_api_get(self):

        self.assertTrue(self.server_is_up())

        api = Api('/')
        status, res = api.get()

        self.assertEqual(status, 200, "status code should be 200.")

        api = Api('/this/endpoint/should/not/exist')
        status, res = api.get()

        self.assertEqual(status, 404, "endpoint should not exist")


