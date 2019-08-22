
import unittest
import os
from src.main.python.api import Api
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
            with Api('/account') as apiInstance:

                self.assertTrue(path.exists(apiInstance.store_path), True)

    def test_api_host(self):
        with Api("/endpoint") as apiInstance:
            self.assertEqual(apiInstance.endpoint, "/endpoint")

    def test_api_host_environ(self):
        environ_host = "/endpoint"
        os.environ["_API_HOST"] = environ_host

        with Api("/another_endpoint") as apiInstance:
            self.assertEqual(apiInstance.host, environ_host)

        # Unset environment variable
        del os.environ["_API_HOST"]

    def test_api_port(self):
        with Api("/endpoint", port=1234) as apiInstance:
            self.assertEqual(apiInstance.port, 1234)

    def test_api_port_environ(self):
        environ_port = "1234"
        os.environ["_API_PORT"] = environ_port

        with Api("/endpoint") as apiInstance:
            self.assertEqual(apiInstance.port, environ_port)

        # Unset environment variable
        del os.environ["_API_PORT"]

    def test_api_endpoint(self):
        with Api() as basic_endpoint:
            self.assertEqual(basic_endpoint.endpoint, "/")

        with Api("/endpoint") as good_endpoint:
            self.assertEqual(good_endpoint.endpoint, "/endpoint")

        with Api("endpoint") as bad_endpoint:
            self.assertEqual(bad_endpoint.endpoint, "/endpoint")

    def test_api_url(self):
        with Api(host="google.com", port=1234, endpoint="/endpoint") as apiInstance:
            self.assertEqual(apiInstance.url, "http://google.com:1234/api/v1/endpoint")

    def test_api_enter(self):
        with Api() as apiInstance:
            self.assertIsNotNone(apiInstance.store)

    def test_api_get(self):
        # self.assertTrue(self.server_is_up())
        with Api('/', host='thishostdoesnotexist.com') as apiInstance:
            self.assertTupleEqual(apiInstance.get(), (None, None))

    def test_api_post(self):
        with Api('/', host='thishostdoesnotexist.com') as apiInstance:
            self.assertTupleEqual(apiInstance.post(), (None, None))

    def test_api_put(self):
        with Api('/', host='thishostdoesnotexist.com') as apiInstance:
            self.assertTupleEqual(apiInstance.put(), (None, None))

    def test_api_delete(self):
        with Api('/', host='thishostdoesnotexist.com') as apiInstance:
            self.assertTupleEqual(apiInstance.delete(), (None, None))


if __name__ == '__main__':
    unittest.main()
