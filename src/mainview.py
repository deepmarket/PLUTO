from os import path
from src.uix.util import *


class MainView(QFrame):
    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        self.num_regex = re.compile(r"(\d+)")
        #  self.num_regex = re.compile(r"(?<![-.])\b[0-9]+\b(?!\.[0-9])")

        # reference by: https://stackoverflow.com/questions/10086572/ip-address-validation-in-python-using-regex
        # self.ip_regex = re.compile(r"(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}" +
        #                            "(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))")

        self.ip_regex = re.compile(r"^(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(\.(?!$)|$)){4}$")

        self.api_endpoint = None

        self.credential_store = path.join(path.abspath("./"), ".credential_store")
        if path.exists(self.credential_store):
            with open(self.credential_store, "r") as credentials:
                self.customer_id: str = credentials.readline()
