from os import path
from src.uix.util import *


class MainView(QFrame):
    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        self.num_regex = re.compile(r"(?<![-.])\b[0-9]+\b(?!\.[0-9])")

        self.api_endpoint = None

        self.credential_store = path.join(path.abspath("./"), ".credential_store")
        if path.exists(self.credential_store):
            with open(self.credential_store, "r") as credentials:
                self.customer_id: str = credentials.readline()
