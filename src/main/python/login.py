from enum import Enum, auto
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtCore import pyqtSignal

from src.main.python.api import Api
from src.main.python.util import email_verification_check

from src.main.python.interfaces.login import LoginUI, LoginPageUI, CreatePageUI


class Login(LoginUI):
    def __init__(
        self, login_signal: pyqtSignal, cxt: ApplicationContext, *args, **kwargs
    ):
        super(Login, self).__init__(cxt, *args, **kwargs)

        self.cxt = cxt
        self.login_signal = login_signal

    # pre-check user input before access db
    def login_action(self):

        # class Res(Enum):
        #     INVALID_ERROR = "Please enter a valid Email address."
        #     SUCCESS = auto()

        # clear error hint
        self.login.login_hint.setText("")

        username = self.login.username.text()
        pwd = self.login.pwd.text()

        # email_res = email_verification_check(username, Res)

        # Both empty
        if not username and not pwd:
            self.login.login_hint.setText("Please enter your email and password.")

        # Empty username
        elif not username and pwd:
            self.login.login_hint.setText("Please enter your email.")

        # elif email_res != Res.SUCCESS:
        # self.login.login_hint.setText(email_res)

        # Empty password
        elif not pwd and username:
            self.login.login_hint.setText("Please enter your password.")

        # otherwise, input check pass
        else:
            self.attempt_login(username, pwd)

    # pre-check user input before access db
    def create_action(self):

        # clear error hint
        self.create.create_hint.setText("")

        first = self.create.first.text()
        last = self.create.last.text()
        email = self.create.username.text()
        pwd = self.create.pwd.text()
        confirm_pwd = self.create.confirm_pwd.text()

        class Res(Enum):
            INVALID_ERROR = "Please enter a valid Email address."
            SUCCESS = auto()

        email_res = email_verification_check(email, Res)

        # First name empty
        if not first:
            self.create.create_hint.setText("Must enter a first name.")

        # Last name empty
        elif not last:
            self.create.create_hint.setText("Must enter a last name.")

        elif email_res != Res.SUCCESS:
            self.create.create_hint.setText(email_res)

        elif not pwd:
            self.create.create_hint.setText("Must enter a password")

        elif pwd != confirm_pwd:
            self.create.create_hint.setText("Passwords do not match.")

        # otherwise, check pass
        else:
            print(
                f"Creating account with:\n\tFirst name: '{first}'\n\tLast name: '{last}'\n"
                f"\tEmail:'{email}'\n\tPassword: '{pwd}''"
            )
            self.attempt_create(first, last, email, pwd)

    def attempt_login(self, username, pwd):

        with Api(self.cxt, "/auth/login") as api:
            status, res = api.post({"email": username, "password": pwd})

            if (res or status) is None:
                """
                    App can't connect to server.
                """
                self.login.login_hint.setText(
                    "There was an error connecting to the authentication servers. "
                    "Please try again in a little while."
                )
            elif res.get("auth"):
                """
                    Username and password both correct.
                """
                self.accept()
                self.login_signal.emit()
            elif status == 200 and res.get("auth") == False:
                """
                    Username correct but password incorrect.
                    # TODO: return message weird. In this case, it should return
                    # 401 as the case below.
                """
                self.login.login_hint.setText("Password incorrect, please try again.")
            elif status == 401:
                """
                    Username incorrect.
                """
                self.login.login_hint.setText(
                    "No account exists for this email."
                )
            # Only other status API will return is an error, so let the user know
            else:
                """
                    unexpected error.
                """
                self.login.login_hint.setText(
                    "There was an unknown error while trying to log in. Please try again."
                )

    def attempt_create(self, first, last, username, pwd):

        with Api(self.cxt, "/account") as api:

            auth_dict = {
                "firstname": first,
                "lastname": last,
                "email": username,
                "password": pwd,
            }

            status, res = api.post(auth_dict)
            if (res or status) is None:
                self.create.create_hint.setText("Could not connect to the server")
            elif status == 200:
                # timer = QTimer()
                # timer.timeout.connect(self.cancel_action)
                # timer.start(900)

                # if timer:
                # Accept and close parent window
                self.attempt_login(username, pwd)
            else:
                self.create.create_hint.setText(
                    "That email and password combination is already in use"
                )
