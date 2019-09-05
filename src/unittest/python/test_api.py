
import unittest
from os import environ
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
            with Api('/account') as api_instance:

                self.assertTrue(path.exists(api_instance.store_path), True)

    def test_api_host(self):
        with Api("/endpoint") as api_instance:
            self.assertEqual(api_instance.endpoint, "/endpoint")

    def test_api_host_environ(self):
        environ_host = "/endpoint"
        environ["_API_HOST"] = environ_host

        with Api("/another_endpoint") as api_instance:
            self.assertEqual(api_instance.host, environ_host)

        # Unset environment variable
        del environ["_API_HOST"]

    def test_api_port(self):
        testPort = environ.get("_API_PORT", 1234) # TODO - stupid patch for functionality
        with Api("/endpoint", port=testPort) as api_instance:
            self.assertEqual(api_instance.port, testPort)

    def test_api_port_environ(self):
        environ_port = "1234"
        environ["_API_PORT"] = environ_port

        with Api("/endpoint") as api_instance:
            self.assertEqual(api_instance.port, environ_port)

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
        with Api(host="google.com", port=1234, endpoint="/endpoint") as api_instance:
            self.assertEqual(api_instance.url, "http://google.com:1234/api/v1/endpoint")

    def test_api_enter(self):
        with Api() as api_instance:
            self.assertIsNotNone(api_instance.store)

    def test_api_get(self):
        # self.assertTrue(self.server_is_up())
        with Api('/', host='thishostdoesnotexist.com') as api_instance:
            self.assertTupleEqual(api_instance.get(), (None, None))

    def test_api_post(self):
        with Api('/', host='thishostdoesnotexist.com') as api_instance:
            self.assertTupleEqual(api_instance.post(), (None, None))

    def test_api_put(self):
        with Api('/', host='thishostdoesnotexist.com') as api_instance:
            self.assertTupleEqual(api_instance.put(), (None, None))

    def test_api_delete(self):
        with Api('/', host='thishostdoesnotexist.com') as api_instance:
            self.assertTupleEqual(api_instance.delete(), (None, None))


if __name__ == '__main__':
    unittest.main()
