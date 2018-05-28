from os import path
from src.uix.util import *


class MainView(QFrame):
    def __init__(self, parent: QFrame=None, *args, **kwargs):
        super(MainView, self).__init__(parent, *args, **kwargs)

        self.NUM_TABLE_ROWS = 0  # Legacy support?
        self.NUM_TABLE_COLUMNS = 6

        self.api_endpoint = None

        self.credential_store = path.join(path.abspath("./"), ".credential_store")
        if path.exists(self.credential_store):
            with open(self.credential_store, "r") as credentials:
                self.customer_id: str = credentials.readline()
