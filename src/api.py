import requests as req
from json import loads, dumps
# import dsktp.ping


class Api:
    def __init__(self, endpoint: str="/"):

        self.domain = "localhost"  # Used for testing
        # self.domain = "172.20.10.6"  # ip of lab intranet
        self.port = 8080
        self.endpoint = endpoint
        if not self.endpoint.startswith("/"):
            self.endpoint = f"/{self.endpoint}"

        self.url: str = f"http://{self.domain}:{self.port}/api/v1{self.endpoint}"
        self.token = None

    def get(self, attr: str="text", url: str=None):
        if not url:
            url = self.url
        res: req.Response = req.get(url)
        val: str = None
        try:
            val = res.__getattribute__(attr)
            val = loads(val)
        except AttributeError:
            # TODO: Add logging
            val = res
        finally:
            return val

    def post(self, payload: dict={}, attr: str="text", url: str=None):
        if not url:
            url = self.url
        res: req.Response = req.post(url, payload)
        val: dict = None
        try:
            val = res.__getattribute__(attr)
            val = loads(val)
        except AttributeError:
            val = res
        except req.exceptions.ConnectionError:
            pass
        finally:
            return res.status_code, val

    def put(self, payload: dict={}, attr: str="text", url: str=None):

        res: req.Response = req.put(url, payload)
        val: str = None
        try:
            val = res.__getattribute__(attr)
            val = loads(val)
        except AttributeError:
            # TODO: Add logging
            val = res
        finally:
            return val

    def delete(self, attr: str="text", url: str=None):
        if not url:
            url = self.url
        res: req.Response = req.delete(url)
        val: str = None
        try:
            val = res.__getattribute__(attr)
            val = loads(val)
        except AttributeError:
            # TODO: Add logging
            val = res
        finally:
            return val


if __name__ == "__main__":
    DEFAULT_URL = "http://localhost:8080"
    api = Api("/resources/resources")
    get = api.get()

    print(f"get: {get}")
