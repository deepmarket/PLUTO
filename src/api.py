import requests as req
from json import loads, dumps
from os import path, remove


class CredentialManager(object):
    # TODO: Consider using something like marshal, shelve, or pickle
    def __init__(self, file_path="./"):
        self.file_path = file_path
        if not path.exists(path.join(path.abspath(self.file_path), ".credential_store")):
            credential_store_path = path.join(path.abspath(self.file_path), ".credential_store")
            self.credential_store = open(credential_store_path, "w+")
            self.credential_store.close()
        else:
            self.credential_store = path.join(path.abspath(self.file_path), ".credential_store")

    def put(self, obj):
        with open(self.credential_store, "w+") as store:
            # store.write(dumps(obj))
            store.write(obj)

    def get(self, attr: str):
        with open(self.credential_store, "r+") as store:
            # store = loads(store.read())
            store = store.read()
        return store


class Api:
    def __init__(self, endpoint: str="/", auth=False):

        # self.domain = "localhost"  # Used for testing
        self.domain = "131.252.209.102"  # ip of lab machine
        self.port = 8080
        self.endpoint = endpoint
        if not self.endpoint.startswith("/"):
            self.endpoint = f"/{self.endpoint}"

        self.url: str = f"http://{self.domain}:{self.port}/api/v1{self.endpoint}"
        self.store = CredentialManager()
        self.auth = auth
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
            val = res
        finally:
            return val

    def post(self, payload: dict={}, attr: str="text", url: str=None):
        val: dict = None
        token: str = self.store.get("token")

        if not url:
            url = self.url
        if token:
            headers = {"x-access-token": token}
            res = req.post(url, payload, headers=headers)
        else:
            res: req.Response = req.post(url, payload)

        try:
            val = res.__getattribute__(attr)
            val = loads(val)
            token = val['token']
        except AttributeError:
            val = res
        # except req.exceptions.ConnectionError:
        #     pass
        finally:
            if self.auth:
                self.store.put(token)
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
