"""
    The following items can be interacted:

    LoginPage:
        self.username = None
        self.pwd = None
        self.login_button = None
        self.login_hint = None
        self.remember_check = None
        self.to_forget_pwd = None
        self.to_create_button = None

    CreatePage:
        self.first = None
        self.last = None
        self.username = None
        self.pwd = None
        self.create_hint = None
        self.create_button = None
        self.to_login_button = None
"""

from src.api import Api
from src.uix.util import *


class LoginPage(QFrame):

    signal = pyqtSignal(bool)

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # component
        self.login = None
        self.create = None

        # gui property
        # self.pos = None
        self.fade_widget = None
        self.login_move = None
        self.create_move = None

        # functional property
        self.email_verification_regex = None

        self._init_property()
        self._init_ui()
        self.setStyleSheet(login_style)

    def _init_property(self):
        # Graciously borrowed from http://emailregex.com/
        self.email_verification_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", re.IGNORECASE)

        # add more on later build...

    def _init_ui(self):
        self.setObjectName("LoginPage")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        widget_width = 720
        widget_height = 720

        window = QFrame(self)
        window.setFixedSize(widget_width, widget_height)
        window.move((WINDOW_WIDTH-widget_width)/2, (WINDOW_HEIGHT-widget_height)/2)
        self.stack = add_layout(window, STACK)

        # login page
        self.login = Login(self, widget_width, widget_height)
        self.stack.addWidget(self.login)

        # create page
        self.create = CreateAccount(self, widget_width, widget_height)
        self.stack.addWidget(self.create)

        # connect function
        self.login.log_in_button.clicked.connect(self.login_action)
        self.login.username.returnPressed.connect(self.login_action)
        self.login.pwd.returnPressed.connect(self.login_action)
        self.login.sign_up_button.clicked.connect(self.to_create)
        self.create.to_login_button.clicked.connect(self.to_login)
        self.create.create_button.clicked.connect(self.create_action)

    # pre-check user input before access db
    def login_action(self):
        # clear error hint
        self.login.login_hint.setText("")

        username = self.login.username.text()
        pwd = self.login.pwd.text()

        # Both empty
        if not username and not pwd:
            self.login.login_hint.setText("Please enter email / password.")

        # Empty username
        elif not username and pwd:
            self.login.login_hint.setText("Please enter your email.")

        # Empty password
        elif not pwd and username:
            self.login.login_hint.setText("Please enter your password.")

        elif not re.match(self.email_verification_regex, username):
            self.login.login_hint.setText("Invalid username. Please login with email address.")

        # otherwise, input check pass
        else:
            self.attempt_login(username, pwd)

    # verified user input on db
    def attempt_login(self, username, pwd):

        with Api("/auth/login") as api:
            status, res = api.post({
                "email": username,
                "password": pwd
            })

            if status == 200:
                # success
                with Api("/account") as account:
                    status, res = account.get()
                    print(status, res)
                self.signal.emit(True)
            elif status == 401:
                self.login.login_hint.setText("The email or password you entered is invalid.")
            # Only other status API will return is an error, so let the user know
            else:
                self.login.login_hint.setText("There was an error while trying to log in. Please try again.")
                # print(status)

    # pre-check user input before access db
    def create_action(self):
        # clear error hint
        self.create.create_hint.setText("")

        first = self.create.first.text()
        last = self.create.last.text()
        email = self.create.username.text()
        pwd = self.create.pwd.text()
        confirm_pwd = self.create.confirm_pwd.text()

        # First name empty
        if not first:
            self.create.create_hint.setText("Must enter a first name.")

        # Last name empty
        elif not last:
            self.create.create_hint.setText("Must enter a last name.")

        elif not re.match(self.email_verification_regex, email):
            self.create.create_hint.setText("Please enter a valid Email address.")

        elif pwd != confirm_pwd:
            self.create.create_hint.setText("Passwords do not match.")

        # otherwise, check pass
        else:
            # print(f"Creating account with:\n\tFirst name: '{first}'\n\tLast name: '{last}'\n"
            #       f"\tEmail:'{email}'\n\tPassword: '{pwd}''")
            self.attempt_create(first, last, email, pwd)

    # verified user input and load into db
    def attempt_create(self, first, last, username, pwd):

        with Api("/account") as api:

            auth_dict = {
                "firstname": first,
                "lastname": last,
                "email": username,
                "password": pwd
            }

            # try:
            #     status, res = api.post(auth_dict)
            # except ConnectionRefusedError:
            #     self.create.create_hint.setText("Connection refused, please contact your system administrator")
            # except ConnectionError:  # From requests library
            #     self.create.create_hint.setText("Could not connect to the share resources server")
            # finally:

            status, res = api.post(auth_dict)
            if (status, res) == (None, None):
                self.create.create_hint.setText("Could not connect to the share resources server")
            else:
                if status == 200:
                    # timer = QTimer()
                    # timer.timeout.connect(self.cancel_action)
                    # timer.start(900)

                    # if timer:
                        # Accept and close parent window
                    self.attempt_login(username, pwd)
                else:
                    self.create.create_hint.setText("Email/password combination already in use")

    # gui interact function
    def to_create(self):
        self.clean_create_page()
        self.stack.setCurrentIndex(1)

    # gui interact function
    def to_login(self):
        self.clean_login_page()
        self.stack.setCurrentIndex(0)

    # gui interact function
    def clean_login_page(self):
        self.login.username.setText("")
        self.login.pwd.setText("")
        self.login.login_hint.setText("")

    # gui interact function
    def clean_create_page(self):
        self.create.first.setText("")
        self.create.last.setText("")
        self.create.username.setText("")
        self.create.pwd.setText("")
        self.create.confirm_pwd.setText("")
        self.create.create_hint.setText("")

    def init_login_page(self):
        # clean both page
        self.clean_login_page()
        self.clean_create_page()
        self.stack.setCurrentIndex(0)


# Pure UI class, no functionality
class Login(QFrame):
    def __init__(self, parent, width, height, *args, **kwargs):
        super(QFrame, self).__init__(parent, width=width, height=height, *args, **kwargs)

        # variable
        self.username = None                # input string
        self.pwd = None                     # input string
        self.log_in_button = None            # button
        self.sign_up_button = None          # button
        self.login_hint = None              # param string

        self.width = width
        self.height = height

        self._init_ui()
        self.setStyleSheet(login_style)

    def _init_ui(self):
        title = "PLUTO"
        subtitle = "Shared Resources Manager"

        self.setObjectName("Login")
        self.setFixedSize(self.width, self.height)
        window_layout = add_layout(self, VERTICAL, t_m=200, b_m=205)

        # --------- title_frame: title, spacer, sub_title ------------
        title_frame = QFrame(self)
        title_frame.setFixedHeight(105)
        title_layout = add_layout(title_frame, VERTICAL)
        window_layout.addWidget(title_frame)

        title = add_label(title_frame, title, name="Login_login_title", align=Qt.AlignHCenter)
        title_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        title_layout.addItem(spacer)

        subtitle = add_label(title_frame, subtitle, name="Login_login_subtitle", align=Qt.AlignHCenter)
        title_layout.addWidget(subtitle)

        # --------- spacer ------------

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        window_layout.addItem(spacer)

        # --------- login_frame: username, pwd ------------

        login_frame = QFrame(self)
        login_layout = add_layout(login_frame, VERTICAL, space=11, b_m=5, align=Qt.AlignHCenter)
        window_layout.addWidget(login_frame)

        box, self.username = add_login_input_box(login_frame, "E M A I L", title_width=100, height=40,
                                                 fix_width=True)
        login_layout.addWidget(box)

        box, self.pwd = add_login_input_box(login_frame, "P A S S W O R D", title_width=100, height=40,
                                            echo=True, fix_width=True)
        login_layout.addWidget(box)

        # --------- self.login_hint ------------

        self.login_hint = add_label(self, "", name="Login_hint", align=Qt.AlignHCenter)
        window_layout.addWidget(self.login_hint)

        # --------- button_frame: log_in, sign_up ------------

        button_frame = QFrame(self)
        button_layout = add_layout(button_frame, HORIZONTAL, space=10, t_m=7, align=Qt.AlignHCenter)
        window_layout.addWidget(button_frame)

        self.log_in_button = add_button(button_frame, "LOG IN", name="Login_button")
        button_layout.addWidget(self.log_in_button)

        self.sign_up_button = add_button(button_frame, "SIGN UP", name="Login_button")
        button_layout.addWidget(self.sign_up_button)


# Pure UI class, no functionality
class CreateAccount(QFrame):
    def __init__(self, parent, width, height, *args, **kwargs):
        super(QFrame, self).__init__(parent, width=width, height=height, *args, **kwargs)

        # variable
        self.first = None                   # input string
        self.last = None                    # input string
        self.username = None                # input string
        self.pwd = None                     # input string
        self.confirm_pwd = None             # input string
        self.create_hint = None             # param string
        self.create_button = None           # button
        self.to_login_button = None         # button

        self.width = width
        self.height = height

        self._init_ui()
        self.setStyleSheet(login_style)

    def _init_ui(self):
        self.setFixedSize(self.width, self.height)
        window_layout = add_layout(self, VERTICAL, t_m=74, b_m=135, l_m=110, r_m=110)

        # --------- title_frame: title, spacer, prologue------------
        title_frame = QFrame(self)
        title_layout = add_layout(title_frame, VERTICAL, t_m=17, b_m=45)
        window_layout.addWidget(title_frame)

        title = add_label(title_frame, "Create An Account.", name="Login_create_title")
        title_layout.addWidget(title)

        spacer = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        title_layout.addItem(spacer)

        prologue = "In the following section,\nPlease enter your information.\nAnd, enjoy..."
        prologue = add_label(title_frame, prologue, name="Login_prologue")
        title_layout.addWidget(prologue)

        # --------- input_frame: first name, last name, email, password, confirm password------------
        input_frame = QFrame(self)
        input_layout = add_layout(input_frame, VERTICAL, space=8, b_m=15)
        window_layout.addWidget(input_frame)

        input_sub_frame = QFrame(input_frame)
        input_sub_layout = add_layout(input_sub_frame, HORIZONTAL, space=8)
        input_layout.addWidget(input_sub_frame)

        box, self.first = add_login_input_box(input_sub_frame, "FIRST NAME", title_width=80, hint="First name...")
        input_sub_layout.addWidget(box)

        box, self.last = add_login_input_box(input_sub_frame, "LAST NAME", title_width=80, hint="Last name...")
        input_sub_layout.addWidget(box)

        box, self.username = add_login_input_box(input_frame, "EMAIL",
                                                 hint="Please enter an email address as your username...")
        input_layout.addWidget(box)

        box, self.pwd = add_login_input_box(input_frame, "PASSWORD", hint="Please enter your password...", echo=True)
        input_layout.addWidget(box)

        box, self.confirm_pwd = add_login_input_box(input_frame, "CONFIRM PASSWORD",
                                                    hint="Please re-enter your password...", echo=True)
        input_layout.addWidget(box)

        # --------- self.login_hint ------------

        self.create_hint = add_label(self, "", name="Login_hint")
        window_layout.addWidget(self.create_hint)

        # --------- spacer ------------

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        window_layout.addItem(spacer)

        # --------- create_button, to_login ------------
        # button_frame: hint, create_button
        button_frame = QFrame(self)
        window_layout.addWidget(button_frame)
        button_layout = add_layout(button_frame, HORIZONTAL)

        self.create_button = add_button(button_frame, "CREATE ACCOUNT", name="Login_large_button")
        button_layout.addWidget(self.create_button)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_layout.addItem(spacer)

        # to_login_frame: to_create_button
        to_login_frame = QFrame(self)
        button_layout.addWidget(to_login_frame)
        to_login_layout = add_layout(to_login_frame, HORIZONTAL, space=7)

        label = add_label(to_login_frame, "Already a member?", name="Login_switch_description")
        to_login_layout.addWidget(label)

        self.to_login_button = add_button(to_login_frame, "Login Here.", name="Login_switch_button")
        to_login_layout.addWidget(self.to_login_button)
