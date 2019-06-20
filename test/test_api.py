
import unittest
from src.api import Api
from requests.exceptions import ConnectionError


class ApiTest(unittest.TestCase):

    @staticmethod
    def server_is_up():
        domain = Api().host
        port = Api().port

        from requests import get

        try:
            status_request = str(get(f"http://{domain}:{port}/api/v1/").text.encode('utf-8')).lower()
        except ConnectionError:
            return False
        else:
            # Quasi check for server status
            return all([bool(txt) for txt in ['api', 'is', 'online'] if txt in str(status_request)])
        
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

    def test_api_host(self):
        with Api("/endpoint") as api:
            self.assertEqual(api.endpoint, "/endpoint")

    def test_api_host_environ(self):
        environ_host = "/endpoint"
        from os import environ
        environ["_API_HOST"] = environ_host

        with Api("/another_endpoint") as api:
            self.assertEqual(api.host, environ_host)

        # Unset environment variable
        del environ["_API_HOST"]

    def test_api_port(self):
        with Api("/endpoint", port=1234) as api:
            self.assertEqual(api.port, 1234)

    def test_api_port_environ(self):
        environ_port = "1234"
        from os import environ
        environ["_API_PORT"] = environ_port

        with Api("/endpoint") as api:
            self.assertEqual(api.port, environ_port)

        # Unset environment variable
        del environ["_API_PORT"]

    def test_api_endpoint(self):
        with Api() as basic_endpoint:
            self.assertEqual(basic_endpoint.endpoint, "/")

        with Api("/endpoint") as good_endpoint:
            self.assertEqual(good_endpoint.endpoint, "/endpoint")

        with Api("endpoint") as bad_endpoint:
            self.assertEqual(bad_endpoint.endpoint, "/endpoint")

    def test_api_url(self):
        with Api(host="google.com", port=1234, endpoint="/endpoint") as api:
            self.assertEqual(api.url, f"http://google.com:1234/api/v1/endpoint")

    def test_api_enter(self):
        with Api() as api:
            self.assertIsNotNone(api.store)

    def test_api_get(self):
        # self.assertTrue(self.server_is_up())
        with Api('/', host='thishostdoesnotexist.com') as api:
            self.assertTupleEqual(api.get(), (None, None))

    def test_api_post(self):
        with Api('/', host='thishostdoesnotexist.com') as api:
            self.assertTupleEqual(api.post(), (None, None))

    def test_api_put(self):
        with Api('/', host='thishostdoesnotexist.com') as api:
            self.assertTupleEqual(api.put(), (None, None))

    def test_api_delete(self):
        with Api('/', host='thishostdoesnotexist.com') as api:
            self.assertTupleEqual(api.delete(), (None, None))


if __name__ == '__main__':
    unittest.main()
