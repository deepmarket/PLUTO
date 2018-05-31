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
        self.agree_click = None
        self.agreement = None
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
        set_base_geometry(self, 300, 520, fixed=True)

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
        self.clean_login_hint()

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

        # join api later
        # self.accept()
        # self.close()

        api: Api = Api("/auth/login")

        status, res = api.post({
            "email": username,
            "password": pwd
        })

        if status == 200:

            # customer_id_endpoint = Api(f"/account/{pwd}")
            # customer_id = customer_id_endpoint.get()

            token = res['token']

            self.credential_store = os.path.join(os.path.abspath("./"), ".credential_store")
            if os.path.exists(self.credential_store):
                os.remove(self.credential_store)

            with open(self.credential_store, "w+") as store:
                store.write(token)

            self.accept()
            self.close()
        else:
            self.login.login_hint.setText("The email or password you entered is invalid.")

    # pre-check user input before access db
    def create_action(self):
        # clear error hint
        self.clean_create_hint()

        first = self.create.first.text()
        last = self.create.last.text()
        email = self.create.username.text()
        pwd = self.create.pwd.text()

        # First name empty
        if not first:
            self.create.create_hint.setText("Must enter a first name.")

        # Last name empty
        elif not last:
            self.create.create_hint.setText("Must enter a last name.")

        elif not re.match(self.email_verification_regex, email):
            self.create.create_hint.setText("Please enter a valid Email address.")

        # should be confirmed password check here

        # otherwise, check pass
        else:
            print(f"Creating account with:\n\tFirst name: '{first}'\n\tLast name: '{last}'\n"
                  f"\tEmail:'{email}'\n\tPassword: '{pwd}''")
            self.attempt_create(first, last, email, pwd)

    # verified user input and load into db
    def attempt_create(self, first, last, username, pwd):
        api: Api = Api("/account")

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
                # customer_id_endpoint = Api(f"/account/{username}")
                # customer_id = customer_id_endpoint.get()
                # token = res['token']

                # with open(self.credential_store, "w+") as store:
                #     store.write(token)

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
    def clean_login_hint(self):
        self.login.login_hint.setText("")

    # gui interact function
    def clean_login_page(self):
        self.login.username.setText("")
        self.login.pwd.setText("")
        self.clean_login_hint()

    def clean_create_hint(self):
        self.create.create_hint.setText("")

    # gui interact function
    def clean_create_page(self):
        self.create.first.setText("")
        self.create.last.setText("")
        self.create.username.setText("")
        self.create.pwd.setText("")
        self.create.agree_click.setChecked(True)
        self.clean_create_hint()


# Pure UI class, no functionality
class LoginPage(QFrame):
    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # sections
        self.login_section = None
        self.to_create_section = None

        # variable
        self.username = None
        self.pwd = None
        self.login_button = None
        self.login_hint = None
        self.remember_check = None
        self.to_forget_pwd = None
        self.to_create_button = None

        self._init_geometry()
        self._init_ui()

        self.setStyleSheet(login_style)

    def _init_geometry(self):

        # set size policy with a fixed height
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Fix width to 200px
        self.setFixedSize(300, 520)

    def _init_ui(self):

        self.setObjectName("Login")
        window_layout = add_layout(self, VERTICAL)

        self.login_section = QFrame(self)
        self._init_login()

        self.to_create_section = QFrame(self)
        self._init_to_create()

        # spacer
        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        window_layout.addWidget(self.login_section)
        window_layout.addItem(spacer)
        window_layout.addWidget(self.to_create_section)

    def _init_login(self):
        self.login_section.setObjectName("Login_page_section")

        section_layout = add_layout(self.login_section, VERTICAL)

        # title frame: logo, title
        title_frame = QFrame(self.login_section)
        title_layout = add_layout(title_frame, VERTICAL, t_m=85, b_m=95, space=20)

        logo = add_image(title_frame, "logo", PNG, height=35, align=Qt.AlignHCenter)
        title = add_label(title_frame, "Welcome to Share Source",
                          name="Login_title", align=Qt.AlignHCenter)

        title_layout.addWidget(logo)
        title_layout.addWidget(title)

        # input frame: username, pwd, login_button
        input_frame = QFrame(self.login_section)
        input_layout = add_layout(input_frame, VERTICAL, l_m=45, r_m=45, space=23)

        username_box, self.username = add_input_box_01(input_frame, "U S E R N A M E", hint="Enter email address...")
        pwd_box, self.pwd = add_input_box_01(input_frame, "P A S S W O R D", hint="Enter a password...", echo=True)

        input_layout.addWidget(username_box)
        input_layout.addWidget(pwd_box)

        # login frame: login_button, login_hint
        login_frame = QFrame(self.login_section)
        login_layout = add_layout(login_frame, VERTICAL, l_m=45, r_m=45, t_m=10, space=5)

        self.login_button = add_button(login_frame, "LOG  IN", name="Login_big_button")

        self.login_hint = add_label(login_frame, "", name="Login_hint")
        login_layout.addWidget(self.login_hint)
        login_layout.addWidget(self.login_button)

        # option frame: remember checkbox, forget pwd
        option_frame = QFrame(self.login_section)
        option_layout = add_layout(option_frame, HORIZONTAL, l_m=45, r_m=45, t_m=10)

        remember_box, self.remember_check = add_checkbox(option_frame, "Remember Account", align=Qt.AlignLeft)
        self.to_forget_pwd = add_button(option_frame, "Forget Password?", name="Login_forget_pwd")

        option_layout.addWidget(remember_box)
        option_layout.addWidget(self.to_forget_pwd)

        section_layout.addWidget(title_frame)
        section_layout.addWidget(input_frame)
        section_layout.addWidget(login_frame)
        section_layout.addWidget(option_frame)

    def _init_to_create(self):
        self.to_create_section.setObjectName("Login_switch_section")

        # set size policy with a fixed height
        self.to_create_section.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)

        # Fix width to 200px
        self.to_create_section.setFixedHeight(45)

        section_layout = add_layout(self.to_create_section, HORIZONTAL, space=7)

        description = add_label(self.to_create_section, "Not a Member?",
                                name="Login_switch_description",
                                align=(Qt.AlignRight | Qt.AlignVCenter))

        self.to_create_button = add_button(self.to_create_section, "Create a Account",
                                           name="Login_switch_button")

        section_layout.addWidget(description)
        section_layout.addWidget(self.to_create_button)


# Pure UI class, no functionality
class CreatePage(QFrame):
    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # sections
        self.create_section = None
        self.to_login_section = None

        # variable
        self.first = None
        self.last = None
        self.username = None
        self.pwd = None
        self.create_hint = None
        self.create_button = None
        self.agree_click = None
        self.agreement = None
        self.to_login_button = None

        self._init_geometry()
        self._init_ui()

        self.setStyleSheet(login_style)

    def _init_geometry(self):

        # set size policy with a fixed height
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Fix width to 200px
        self.setFixedSize(300, 520)

    def _init_ui(self):

        self.setObjectName("Login")
        window_layout = add_layout(self, VERTICAL)

        self.create_section = QFrame(self)
        self._init_create()

        self.to_login_section = QFrame(self)
        self._init_to_login()

        # spacer
        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        window_layout.addWidget(self.create_section)
        window_layout.addItem(spacer)
        window_layout.addWidget(self.to_login_section)

    def _init_create(self):
        self.create_section.setObjectName("Login_page_section")

        section_layout = add_layout(self.create_section, VERTICAL)

        # title frame: title, prologue
        title_frame = QFrame(self.create_section)
        title_layout = add_layout(title_frame, VERTICAL, t_m=50, b_m=70, l_m=40, r_m=40, space=15)

        title = add_label(title_frame, "Thanks for Registration",
                          name="Login_title", align=Qt.AlignLeft)

        paragraph = ["In the following section,",
                     "Please enter the correct information,",
                     "And, enjoy..."]

        prologue = add_paragraph(title_frame, paragraph, name="Login_prologue", space=7)

        title_layout.addWidget(title)
        title_layout.addWidget(prologue)

        # input frame: first_name, last_name, user_name, pwd
        input_frame = QFrame(self.create_section)
        input_layout = add_layout(input_frame, VERTICAL, l_m=40, r_m=40, space=22)

        # horizontal name frame
        name_frame = QFrame(input_frame)
        name_layout = add_layout(name_frame, HORIZONTAL, space=20)

        f_box, self.first = add_input_box_01(name_frame, "F I R S T N A M E", hint="First name...")
        l_box, self.last = add_input_box_01(name_frame, "L A S T N A M E", hint="Last name...")

        name_layout.addWidget(f_box)
        name_layout.addWidget(l_box)

        username_box, self.username = add_input_box_01(input_frame, "U S E R N A M E", hint="Enter email address...")
        pwd_box, self.pwd = add_input_box_01(input_frame, "P A S S W O R D", hint="Enter a password...", echo=True)

        input_layout.addWidget(name_frame)
        input_layout.addWidget(username_box)
        input_layout.addWidget(pwd_box)

        # create frame: create_button, create_hint
        create_frame = QFrame(self.create_section)
        create_layout = add_layout(create_frame, VERTICAL, l_m=40, r_m=40, t_m=8, space=5)

        self.create_hint = add_label(create_frame, "", name="Login_hint")
        self.create_button = add_button(create_frame, "CREATE ACCOUNT", name="Login_big_button")

        create_layout.addWidget(self.create_hint)
        create_layout.addWidget(self.create_button)

        # option frame: agreement checkbox
        option_frame = QFrame(self.create_section)
        option_layout = add_layout(option_frame, VERTICAL, l_m=40, r_m=40, t_m=10)

        agree_box, self.agree_click, self.agreement \
            = add_checkbox(option_frame, "I read and accept the Terms and Conditions.",
                           title_type=QPUSHBUTTON, align=Qt.AlignLeft, check=True)

        option_layout.addWidget(agree_box)

        section_layout.addWidget(title_frame)
        section_layout.addWidget(input_frame)
        section_layout.addWidget(create_frame)
        section_layout.addWidget(option_frame)

    def _init_to_login(self):
        self.to_login_section.setObjectName("Login_switch_section")

        # set size policy with a fixed height
        self.to_login_section.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)

        # Fix width to 200px
        self.to_login_section.setFixedHeight(45)

        section_layout = add_layout(self.to_login_section, HORIZONTAL, space=10, l_m=10, r_m=10)

        description = add_label(self.to_login_section, "Already a Member?",
                                name="Login_switch_description",
                                align=Qt.AlignRight | Qt.AlignVCenter)

        self.to_login_button = add_button(self.to_login_section, "Login Here",
                                          name="Login_switch_button")

        section_layout.addWidget(description)
        section_layout.addWidget(self.to_login_button)
