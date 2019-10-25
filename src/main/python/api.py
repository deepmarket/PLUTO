from os import environ, path, curdir, remove
import requests as req

from json import JSONDecodeError
from requests.exceptions import ConnectionError

from fbs_runtime.application_context.PyQt5 import ApplicationContext


class CredentialManager(object):
    # TODO: Consider using something like marshal, shelve, or pickle
    def __init__(self, cxt: ApplicationContext):

        self.store = cxt.credential_store

    def put(self, obj):
        with open(self.store, "w+") as store:
            # store.write(dumps(obj))
            store.write(obj)

    def get(self):
        with open(self.store, "r+") as store:
            # store = loads(store.read())
            return store.read()

    def remove(self):
        from os import remove
        remove(self.store)


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
        self.token = self.store.get()
        self.headers = {"X-access-token": self.token}

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _set_state(self):
        if "logout" in self.endpoint:
            self.store.remove()
        elif self.token:
            self.store.put(self.token)

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
