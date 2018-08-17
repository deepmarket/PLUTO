
import unittest
from src.api import Api


class ApiTest(unittest.TestCase):

    @staticmethod
    def server_is_up():
        domain = Api().domain
        port = Api().port

        from requests import get
        status_request = str(get(f"http://{domain}:{port}/api/v1/").text.encode('utf-8')).lower()
        
        # All of 
        if all([bool(txt) for txt in ['api', 'is', 'online'] if txt in str(status_request)]):
            return true
        
        return false
        
    def test_credential_store(self):
        from os import path
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

                self.assertTrue(path.exists(Api.store_path), True)
                # Clean up
                api.delete()

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


if __name__ == '__main__':
    unittest.main()
