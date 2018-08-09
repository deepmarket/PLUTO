import requests as req
from json import loads, dumps
from os import path, remove

from requests.exceptions import ConnectionError


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
    def __init__(self, endpoint: str="/", domain: str="131.252.209.102", port: int=8080, auth: bool=False):

        self.domain = domain
        self.port = port

        self.endpoint = endpoint
        if not self.endpoint.startswith("/"):
            self.endpoint = f"/{self.endpoint}"

        self.url: str = f"http://{self.domain}:{self.port}/api/v1{self.endpoint}"
        self.store = CredentialManager()
        self.auth = auth
        self.token = None

    def get(self, attr: str="text", url: str=None):
        val: str = None
        token: str = self.store.get("token")

        if not url:
            url = self.url

        if token:
            headers = {"x-access-token": token}
            try:
                res: req.Response = req.get(url, headers=headers)
            except ConnectionError:
                return None, None
        else:
            try:
                res: req.Response = req.get(url)
            except ConnectionError:
                return None, None
        try:
            val = res.__getattribute__(attr)
            val = loads(val)
        except AttributeError:
            val = res
        finally:
            if self.auth and token:
                self.store.put(token)
            return res.status_code, val

    def post(self, payload: dict={}, attr: str="text", url: str=None):
        val: dict = None
        token: str = self.store.get("token")

        if not url:
            url = self.url

        if token:
            headers = {"x-access-token": token}
            try:
                res = req.post(url, payload, headers=headers)
            except ConnectionError:
                return None, None
        else:
            try:
                res: req.Response = req.post(url, payload)
            except ConnectionError:
                return None, None
        try:
            val = res.__getattribute__(attr)
            val = loads(val)
            token = val['token']
        except AttributeError:
            val = res
        finally:
            if self.auth and token:
                self.store.put(token)
            return res.status_code, val

    def put(self, payload: dict={}, attr: str="text", url: str=None):

        if not url:
            url = self.url

        try:
            res: req.Response = req.put(url, payload)
        except ConnectionError:
            return None

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
        val: dict = None

        if not url:
            url = self.url

        token: str = self.store.get("token")

        if token:
            headers = {"x-access-token": token}
            res = req.delete(url, headers=headers)
        else:
            try:
                res: req.Response = req.delete(url)
            except ConnectionError:
                return None, None
        try:
            val = res.__getattribute__(attr)
            val = loads(val)
        except AttributeError:
            val = res
        finally:
            if self.auth and token:
                self.store.put(token)
            return res.status_code, val


if __name__ == "__main__":
    DEFAULT_URL = "http://localhost:8080"
    api = Api("/resources/resources")
    get = api.get()

    print(f"get: {get}")
