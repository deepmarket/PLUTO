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


class Api(object):
    def __init__(self, endpoint: str="/", domain: str="131.252.209.102", port: int=8080, auth: bool=False):

        self.domain = domain
        self.port = port

        self.endpoint = endpoint
        if not self.endpoint.startswith("/"):
            self.endpoint = f"/{self.endpoint}"

        self.url: str = f"http://{self.domain}:{self.port}/api/v1{self.endpoint}"
        self.auth: bool = auth
        self.token: str = None

    def __enter__(self):
        self.store = CredentialManager()
        self.token = self.store.get("token")

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.auth and self.token:
            self.store.put(self.token)

    def get(self, attr: str="text"):
        val: str = None

        headers = {"x-access-token": self.token}
        try:
            res: req.Response = req.get(self.url, headers=headers)
        except ConnectionError:
            return None, None

        try:
            val = loads(res.__getattribute__(attr))
        except AttributeError:
            val = res
        finally:
            return res.status_code, val

    def post(self, payload: dict={}, attr: str="text"):
        val: dict = None

        headers = {"x-access-token": self.token}
        try:
            res = req.post(self.url, payload, headers=headers)
        except ConnectionError:
            return None, None

        try:
            val = res.__getattribute__(attr)
            val = loads(val)
            self.token = val['token']
        except AttributeError:
            val = res
        finally:
            # if self.auth and token:
            #     self.store.put(token)
            return res.status_code, val

    def put(self, payload: dict={}, attr: str="text"):
        val: str = None

        headers = {"x-access-token": self.token}
        try:
            res = req.put(self.url, payload, headers=headers)
        except ConnectionError:
            return None, None

        try:
            val = res.__getattribute__(attr)
            val = loads(val)
        except AttributeError:
            val = res
        finally:
            return val

    def delete(self, attr: str="text"):
        val: dict = None

        headers = {"x-access-token": self.token}
        try:
            res = req.delete(self.url, headers=headers)
        except ConnectionError:
            return None, None

        try:
            val = res.__getattribute__(attr)
            val = loads(val)
        except AttributeError:
            val = res
        finally:
            return res.status_code, val
