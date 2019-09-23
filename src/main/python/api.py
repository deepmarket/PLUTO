import requests as req

from json import JSONDecodeError
from os import environ, path, curdir, remove

from requests.exceptions import ConnectionError


class CredentialManager(object):
    # TODO: Consider using something like marshal, shelve, or pickle
    def __init__(self, file_path="./"):

        self.file_path = file_path
        if not path.exists(
            path.join(path.abspath(self.file_path), ".credential_store")
        ):
            self.credential_store = path.join(
                path.abspath(self.file_path), ".credential_store"
            )

            # Create file
            with open(self.credential_store, "w+"):
                pass

        else:
            self.credential_store = path.join(
                path.abspath(self.file_path), ".credential_store"
            )

    def put(self, obj):
        with open(self.credential_store, "w+") as store:
            # store.write(dumps(obj))
            store.write(obj)

    def get(self):
        with open(self.credential_store, "r+") as store:
            # store = loads(store.read())
            return store.read()


class Api(object):
    # Set store path globally
    store_path = path.abspath(curdir)

    def __init__(
        self, endpoint: str = "/", host: str = "atlantic.cs.pdx.edu", port: int = 8080
    ):

        # Override given domain name/port if defined in the environment
        # These are intended to be used for development/testing
        self.host: str = environ.get("_API_HOST", False) or host
        self.port: int = environ.get("_API_PORT", False) or port

        self.endpoint: str = endpoint if endpoint.startswith("/") else f"/{endpoint}"

        self.url: str = f"http://{self.host}:{self.port}/api/v1{self.endpoint}"

        # self.auth: bool = auth
        self.auth: bool = ("auth" in self.endpoint)
        self.store: CredentialManager = None
        self.token: str = None
        self.headers: dict = {}

    def __enter__(self):
        self.store = CredentialManager(self.store_path)
        self.token = self.store.get()
        self.headers = {"X-access-token": self.token}

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.auth and self.token:
            self.store.put(self.token)

    def get(self):

        try:
            res: req.Response = req.get(self.url, headers=self.headers)
            return res.status_code, res.json()
        except (ConnectionError, JSONDecodeError) as err:

            return None, None

    def post(self, payload: dict = {}):

        try:
            res: req.Response = req.post(self.url, payload, headers=self.headers)
            res_json: dict = res.json()
            if res_json.get('token'):
                self.auth = True
                self.token = res_json.get('token')
                if 'login' in res_json.get('message', '').lower():
                    self.store.put(self.token)

            return res.status_code, res_json
        except (ConnectionError, JSONDecodeError) as err:

            return None, None

    def put(self, payload: dict = {}):

        try:
            res: req.Response = req.put(self.url, payload, headers=self.headers)
            return res.status_code, res.json()

        except (ConnectionError, JSONDecodeError) as err:

            return None, None

    def delete(self):

        try:
            res: req.Response = req.delete(self.url, headers=self.headers)
            return res.status_code, res.json()

        except (ConnectionError, JSONDecodeError) as err:

            return None, None
