
import unittest
from sys import path as sys_path
from os import path as os_path
sys_path.append(os_path.join("src", "main", "python"))
    
from os import environ
from requests.exceptions import ConnectionError
from api import Api
from main import AppContext



class ApiTest(unittest.TestCase):

    @staticmethod
    def server_is_up():
        environ_host = "atlantic.cs.pdx.edu"
        environ_port = "8080"

        environ["_API_HOST"] = environ_host
        environ["_API_PORT"] = environ_port

        cxt = AppContext()
        domain = Api(cxt).host
        port = Api(cxt).port

        from requests import get
        
        try:
            status_request = str(get(f"http://{domain}:{port}/api/v1/").text.encode('utf-8')).lower()
        except ConnectionError:
            return False
        else:
            # Quasi check for server status
            return all([bool(txt) for txt in ['api', 'is', 'online'] if txt in str(status_request)])

    def test_credential_store(self):
        cxt = AppContext()

        from os import path
        if self.server_is_up():
            with Api(cxt, '/account') as api_instance:

                self.assertTrue(path.exists(api_instance.store_path), True)

    def test_api_host(self):
        cxt = AppContext()

        with Api(cxt, "/endpoint") as api_instance:
            self.assertEqual(api_instance.endpoint, "/endpoint")

    def test_api_host_environ(self):
        cxt = AppContext()

        environ_host = "/endpoint"
        environ["_API_HOST"] = environ_host

        with Api(cxt, "/another_endpoint") as api_instance:
            self.assertEqual(api_instance.host, environ_host)

        # Unset environment variable
        del environ["_API_HOST"]

    def test_api_port(self):
        cxt = AppContext()

        testPort = environ.get("_API_PORT", 1234) # TODO - stupid patch for functionality
        with Api(cxt, "/endpoint", port=testPort) as api_instance:
            self.assertEqual(api_instance.port, testPort)

    def test_api_port_environ(self):
        cxt = AppContext()

        environ_port = "1234"
        environ["_API_PORT"] = environ_port

        with Api(cxt, "/endpoint") as api_instance:
            self.assertEqual(api_instance.port, environ_port)

        # Unset environment variable
        del environ["_API_PORT"]

    def test_api_endpoint(self):
        cxt = AppContext()

        with Api(cxt) as basic_endpoint:
            self.assertEqual(basic_endpoint.endpoint, "/")

        with Api(cxt, "/endpoint") as good_endpoint:
            self.assertEqual(good_endpoint.endpoint, "/endpoint")

        with Api(cxt, "endpoint") as bad_endpoint:
            self.assertEqual(bad_endpoint.endpoint, "/endpoint")

    def test_api_url(self):
        cxt = AppContext()

        with Api(cxt, host="google.com", port=1234, endpoint="/endpoint") as api_instance:
            self.assertEqual(api_instance.url, "http://google.com:1234/api/v1/endpoint")

    def test_api_enter(self):
        cxt = AppContext()

        with Api(cxt) as api_instance:
            self.assertIsNotNone(api_instance.store)

    def test_api_get(self):
        cxt = AppContext()

        # self.assertTrue(self.server_is_up())
        with Api(cxt, '/', host='thishostdoesnotexist.com') as api_instance:
            self.assertTupleEqual(api_instance.get(), (None, None))

    def test_api_post(self):
        cxt = AppContext()

        with Api(cxt, '/', host='thishostdoesnotexist.com') as api_instance:
            self.assertTupleEqual(api_instance.post(), (None, None))

    def test_api_put(self):
        cxt = AppContext()

        with Api(cxt, '/', host='thishostdoesnotexist.com') as api_instance:
            self.assertTupleEqual(api_instance.put(), (None, None))

    def test_api_delete(self):
        cxt = AppContext()

        with Api(cxt, '/', host='thishostdoesnotexist.com') as api_instance:
            self.assertTupleEqual(api_instance.delete(), (None, None))


if __name__ == '__main__':
    
    unittest.main()
