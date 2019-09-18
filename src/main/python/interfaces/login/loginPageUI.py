from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtWidgets import QSizePolicy, QWidget

from ..widgets import (
    Frame,
    VerticalLayout,
    HorizontalLayout,
    Label,
    LoginInputFrame,
    VerticalSpacer,
    HorizontalSpacer,
    Button,
)


class LoginPageUI(Frame):

    title_section: Frame = None
    login_section: Frame = None
    button_section: Frame = None

    username: str = ""  # input string
    pwd: str = ""  # input string
    login_button: Button = ""  # button
    login_hint: str = ""  # param string
    remember_check = None  # checkbox
    to_forget_pwd = None  # button
    to_create_button: Button = None  # button

    def __init__(self, widget: QWidget, *args, **kwargs):
        super(LoginPageUI, self).__init__(widget)
        self._init_ui()

    def _init_ui(self):
        # set size policy with a fixed height
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Fix size
        self.setFixedSize(580, 580)

        window_layout = VerticalLayout(self)

        self.title_section = Frame(self, name="login_title_section")
        window_layout.addWidget(self.title_section)
        self._init_title_section()

        self.input_section = Frame(self, name="login_input_section")
        window_layout.addWidget(self.input_section)
        self._init_input_section()

        spacer = VerticalSpacer()
        window_layout.addItem(spacer)

        self.button_section = Frame(self, name="login_button_section")
        window_layout.addWidget(self.button_section)
        self._init_button_section()

        self.switch_section = Frame(self, name="switch_section")
        window_layout.addWidget(self.switch_section)
        self._init_switch_section()

    def _init_title_section(self):

        """
        section_layout = VerticalLayout(self.title_section)

        label = Label(
            self.title_section, text="Welcome.", name="login_title", align=Qt.AlignCenter
        )
        
        section_layout.addWidget(label)
        """
        self.login_kindly()

    def login_kindly(self):
        def update_title(title_text: str = "Please Sign In."):
            section_layout = VerticalLayout(self.title_section)

            label = Label(
                self.title_section,
                text=title_text,
                name="login_title",
                align=Qt.AlignCenter,
            )

            section_layout.addWidget(label)

        update_title("Welcome.")

        timer = QTimer()
        timer.timeout.connect(update_title)
        timer.start(3500)

    def _init_input_section(self):

        section_layout = VerticalLayout(self.input_section, space=20)

        self.username = LoginInputFrame(
            self.input_section,
            title="U S E R N A M E",
            hint="Enter your email address...",
        )

        section_layout.addWidget(self.username)

        self.pwd = LoginInputFrame(
            self.input_section,
            title="P A S S W O R D",
            hint="Enter your password...",
            echo=True,
        )
        section_layout.addWidget(self.pwd)

    def _init_button_section(self):

        section_layout = VerticalLayout(self.button_section, space=10)

        self.login_hint = Label(self.button_section, text="", name="login_hint")
        section_layout.addWidget(self.login_hint)

        self.login_button = Button(
            self.button_section, text="LOG IN", name="action_button", cursor=True
        )
        section_layout.addWidget(self.login_button)

    def _init_switch_section(self):

        section_layout = HorizontalLayout(self.switch_section)

        label = Label(
            self.switch_section,
            text="Not a Member?",
            name="switch_label",
            align=(Qt.AlignRight | Qt.AlignVCenter),
        )
        section_layout.addWidget(label)

        self.to_create_button = Button(
            self.switch_section,
            text="Create An Account.",
            name="switch_button",
            cursor=True,
        )
        section_layout.addWidget(self.to_create_button)
