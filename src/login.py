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
from src.uix.stylesheet import *
from src.uix.util import *


class Login(QDialog):
    def __init__(self, *args, **kwargs):
        super(QDialog, self).__init__(*args, **kwargs)

        self.login = None
        self.create = None

        # gui property
        self.pos = None
        self.login_move = None
        self.create_move = None

        # functional property
        self.username_regex = None

        self._init_geometry()
        self._init_ui()
        self._init_property()

    def _init_geometry(self):
        set_base_geometry(self, 580, 580, fixed=True)

        # set title name
        self.setWindowTitle("Login")

        # hide title bar
        # self.setWindowFlags(Qt.FramelessWindowHint)

    def _init_ui(self):
        # login page
        self.login = LoginPage(self)

        # set initial position
        self.login.move(0, 0)

        # connect function
        self.login.login_button.clicked.connect(self.login_action)
        self.login.to_create_button.clicked.connect(self.to_create)

        # to_create page
        self.create = CreatePage(self)

        # set initial position
        self.create.move(0-self.width(), 0)

        # connect function
        self.create.create_button.clicked.connect(self.create_action)
        self.create.to_login_button.clicked.connect(self.to_login)

    def _init_property(self):
        # Graciously borrowed from http://emailregex.com/
        self.email_verification_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", re.IGNORECASE)

        # add more on later build...

    # mouse graping and window moves
    def mousePressEvent(self, event):
        self.pos = event.globalPos()

    # mouse graping and window moves
    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.pos = event.globalPos()

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

        # elif not re.match(self.username_regex, username):
        #     self.login.login_hint.setText("Invalid username. Please login with email address.")

        # otherwise, input check pass
        else:
            print(f"Logging in with:\n\tEmail: '{username}'\n\tPassword: '{pwd}'")
            self.attempt_login(username, pwd)

    # verified user input on db
    def attempt_login(self, username, pwd):

        api: Api = Api("/auth/login", True)

        status, res = api.post({
            "email": username,
            "password": pwd
        })

        if status == 200:
            self.accept()
            self.close()
        else:
            self.login.login_hint.setText("The email or password you entered is invalid.")

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

        elif pwd is not confirm_pwd:
            self.create.create_hint.setText("Passwords do not match.")

        # otherwise, check pass
        else:
            print(f"Creating account with:\n\tFirst name: '{first}'\n\tLast name: '{last}'\n"
                  f"\tEmail:'{email}'\n\tPassword: '{pwd}''")
            self.attempt_create(first, last, email, pwd)

    # verified user input and load into db
    def attempt_create(self, first, last, username, pwd):
        api: Api = Api("/account", True)

        auth_dict = {
            "firstname": first,
            "lastname": last,
            "email": username,
            "password": pwd
        }

        try:
            status, res = api.post(auth_dict)
        except ConnectionRefusedError:
            self.create.create_hint.setText("Connection refused, please contact your system administrator")
        except ConnectionError:  # From requests library
            self.create.create_hint.setText("Could not connect to the share resources server")
        finally:
            print(res['message'])

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

        self.login_move = add_move_animation(self.login, 0, 0, self.width(), 0)
        self.create_move = add_move_animation(self.create, 0-self.width(), 0, 0, 0)

        self.login_move.start()
        self.create_move.start()

    # gui interact function
    def to_login(self):
        self.clean_login_page()

        self.login_move = add_move_animation(self.login, self.width(), 0, 0, 0)
        self.create_move = add_move_animation(self.create, 0, 0, 0 - self.width(), 0)

        self.login_move.start()
        self.create_move.start()

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
        self.create.create_hint.setText("")


# Pure UI class, no functionality
class LoginPage(QFrame):
    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.username = None                # input string
        self.pwd = None                     # input string
        self.login_button = None            # button
        self.login_hint = None              # param string
        self.remember_check = None          # checkbox
        self.to_forget_pwd = None           # button
        self.to_create_button = None        # button

        self._init_geometry()
        self._init_ui()

        self.setStyleSheet(login_style)

    def _init_geometry(self):

        # set size policy with a fixed height
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Fix size
        self.setFixedSize(580, 580)

    def _init_ui(self):

        self.setObjectName("Login")
        window_layout = add_layout(self, VERTICAL)

        # title_frame: title
        title_frame = QFrame(self)
        title_frame.setFixedHeight(285)
        title_layout = add_layout(title_frame, VERTICAL, l_m=8, r_m=8, t_m=8)

        title = add_label(title_frame, "Welcome to Pluto", name="Login_login_title", align=Qt.AlignCenter)
        title_layout.addWidget(title)

        # login_frame: username, pwd, login_button
        login_frame = QFrame(self)
        login_layout = add_layout(login_frame, VERTICAL, t_m=20, space=20)

        box, self.username = add_login_input_box_01(login_frame, "U S E R N A M E",
                                                    hint="Enter an email address here...")
        login_layout.addWidget(box)

        box, self.pwd = add_login_input_box_01(login_frame, "P A S S W O R D",
                                               hint="Enter a password here...", echo=True)
        login_layout.addWidget(box)

        button_frame = QFrame(self)
        button_layout = add_layout(button_frame, VERTICAL, l_m=3, r_m=3, space=10)

        self.login_hint = add_label(button_frame, "", name="Login_hint")
        button_layout.addWidget(self.login_hint)

        self.login_button = add_button(button_frame, "LOG IN", name="Login_large_button")
        button_layout.addWidget(self.login_button)

        # to_create_frame: to_create_button
        to_create_frame = QFrame(self)
        to_create_frame.setFixedHeight(63)
        to_create_layout = add_layout(to_create_frame, HORIZONTAL, l_m=3, r_m=3, b_m=8, t_m=8)

        label = add_label(to_create_frame, "Not a Member?", name="Login_switch_description",
                          align=(Qt.AlignRight | Qt.AlignVCenter))
        to_create_layout.addWidget(label)

        self.to_create_button = add_button(to_create_frame, "Create Account", name="Login_switch_button")
        to_create_layout.addWidget(self.to_create_button)

        # spacer
        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        window_layout.addWidget(title_frame)
        window_layout.addWidget(login_frame)
        window_layout.addItem(spacer)
        window_layout.addWidget(button_frame)
        window_layout.addWidget(to_create_frame)


# Pure UI class, no functionality
class CreatePage(QFrame):
    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.first = None                   # input string
        self.last = None                    # input string
        self.username = None                # input string
        self.pwd = None                     # input string
        self.confirm_pwd = None             # input string
        self.create_hint = None             # param string
        self.create_button = None           # button
        self.to_login_button = None         # button

        self._init_geometry()
        self._init_ui()

        self.setStyleSheet(login_style)

    def _init_geometry(self):

        # set size policy with a fixed height
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Fix size
        self.setFixedSize(580, 580)

    def _init_ui(self):

        self.setObjectName("Login")
        window_layout = add_layout(self, VERTICAL)

        # title_frame: title, prologue
        title_frame = QFrame(self)
        title_frame.setFixedHeight(208)
        title_layout = add_layout(title_frame, VERTICAL, t_m=39, l_m=31, r_m=8, space=28)

        title = add_label(title_frame, "Thank you for registering.", name="Login_create_title")
        title_layout.addWidget(title)

        prologue = "In the following section,\nlease enter the correct information,\nAnd, enjoy…"
        prologue = add_label(title_frame, prologue, name="Login_prologue")
        title_layout.addWidget(prologue)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        title_layout.addItem(spacer)

        input_frame = QFrame(self)
        input_layout = add_layout(input_frame, VERTICAL, l_m=3, r_m=3, space=3)

        input_sub_frame = QFrame(input_frame)
        input_sub_layout = add_layout(input_sub_frame, HORIZONTAL, space=4)

        box, self.first = add_login_input_box_02(input_sub_frame, "FIRST NAME", title_width=100, hint="First name...")
        input_sub_layout.addWidget(box)

        box, self.last = add_login_input_box_02(input_sub_frame, "LAST NAME", title_width=100, hint="Last name...")
        input_sub_layout.addWidget(box)
        input_layout.addWidget(input_sub_frame)

        box, self.username = add_login_input_box_02(input_frame, "EMAIL",
                                                    hint="Please enter your email address...")
        input_layout.addWidget(box)

        box, self.pwd = add_login_input_box_02(input_frame, "PASSWORD",
                                               hint="Please enter your password...")
        input_layout.addWidget(box)

        box, self.confirm_pwd = add_login_input_box_02(input_frame, "CONFIRM PASSWORD",
                                               hint="Please re-enter your password...")
        input_layout.addWidget(box)

        # button_frame: hint, create_button
        button_frame = QFrame(self)
        button_layout = add_layout(button_frame, VERTICAL, l_m=3, r_m=3, space=10)

        self.create_hint = add_label(button_frame, "", name="Login_hint")
        button_layout.addWidget(self.create_hint)

        self.create_button = add_button(button_frame, "CREATE ACCOUNT", name="Login_large_button")
        button_layout.addWidget(self.create_button)

        # to_create_frame: to_create_button
        to_login_frame = QFrame(self)
        to_login_frame.setFixedHeight(63)
        to_login_layout = add_layout(to_login_frame, HORIZONTAL, l_m=3, r_m=3, b_m=8, t_m=8)

        label = add_label(to_login_frame, "Already a member?", name="Login_switch_description",
                          align=(Qt.AlignRight | Qt.AlignVCenter))
        to_login_layout.addWidget(label)

        self.to_login_button = add_button(to_login_frame, "Login Here.", name="Login_switch_button")
        to_login_layout.addWidget(self.to_login_button)

        # spacer
        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        window_layout.addWidget(title_frame)
        window_layout.addWidget(input_frame)
        window_layout.addItem(spacer)
        window_layout.addWidget(button_frame)
        window_layout.addWidget(to_login_frame)
