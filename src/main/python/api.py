from os import environ, path, curdir, remove
import requests as req

from json import loads, dumps, JSONDecodeError
from requests.exceptions import ConnectionError

from fbs_runtime.application_context.PyQt5 import ApplicationContext


class CredentialManager(object):
    # TODO: Consider using something like marshal, shelve, or pickle
    def __init__(self, cxt: ApplicationContext):

        self.store_path = cxt.credential_store
        with open(self.store_path, "r") as store:
            self.store = loads(dumps(store.read()))

    def put(self, obj: dict):
        self.store.update(**obj)
        with open(self.store_path, "w+") as store:
            store.write(
                dumps(self.store)
            )

    def get(self, attr: str = ""):
        with open(self.store_path, "r") as store:
            self.store = loads(store.read())

        if attr:
            return self.store.get(attr)
        else:
            return self.store

    def cleanup_token(self):
        self.store.update({"token": ""})
        with open(self.store_path, "w+") as store:
            store.write(
                dumps(self.store)
            )


class Api(object):

    def __init__(
        self, cxt: ApplicationContext, endpoint: str = "/", host: str = "atlantic.cs.pdx.edu", port: int = 8080
    ):

        # Override given domain name/port if defined in the environment
        # These are intended to be used for development/testing
        self.host: str = environ.get("_API_HOST", False) or host
        self.port: int = environ.get("_API_PORT", False) or port

        self.endpoint: str = endpoint if endpoint.startswith("/") else f"/{endpoint}"

        self.url: str = f"http://{self.host}:{self.port}/api/v1{self.endpoint}"

        self.cxt = cxt
        # self.auth: bool = auth
        self.auth: bool = (self.endpoint in ("auth/login", "auth/refresh"))
        self.store: CredentialManager = None
        self.token: str = None
        self.headers: dict = {}

    def __enter__(self):
        self.store = CredentialManager(self.cxt)
        self.token = self.store.get("token")
        self.headers = {"X-access-token": self.token}

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if "logout" in self.endpoint:
            self.store.cleanup_token()

    def _set_state(self):
        if self.token:
            self.store.put({
                "token": self.token
            })

    def get(self):
        try:
            res: req.Response = req.get(self.url, headers=self.headers)
            self._set_state()
            return res.status_code, res.json()
        except (ConnectionError, JSONDecodeError) as err:

            return None, None

    def post(self, payload=None):

        if payload is None:
            payload = {}
        try:
            res: req.Response = req.post(self.url, payload, headers=self.headers)
            res_json: dict = res.json()
            if res_json.get('token'):
                self.auth = True
                self.token = res_json.get('token')
            self._set_state()

            return res.status_code, res_json
        except (ConnectionError, JSONDecodeError) as err:

            return None, None

    def put(self, payload=None):

        if payload is None:
            payload = {}
        try:
            res: req.Response = req.put(self.url, payload, headers=self.headers)
            self._set_state()
            return res.status_code, res.json()

        except (ConnectionError, JSONDecodeError) as err:

            return None, None

    def delete(self):

        try:
            res: req.Response = req.delete(self.url, headers=self.headers)
            self._set_state()
            return res.status_code, res.json()

        except (ConnectionError, JSONDecodeError) as err:

            return None, None
