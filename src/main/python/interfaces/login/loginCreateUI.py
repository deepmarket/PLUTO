from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QSizePolicy, QWidget

from ..widgets import (
    Frame, 
    VerticalLayout,
     HorizontalLayout, 
     Label, 
     LoginInputFrame, 
     VerticalSpacer, 
     HorizontalSpacer,
     Button
)

from ..widgets import (
    Frame, 
    VerticalLayout,
     HorizontalLayout, 
     Label, 
     LoginInputFrame, 
     VerticalSpacer, 
     HorizontalSpacer,
     Button
)

class CreatePageUI(Frame):

    first: str = ""                   # input string
    last: str = ""                    # input string
    username: str = ""                # input string
    pwd: str = ""                     # input string
    confirm_pwd: str = ""             # input string
    create_hint: str = ""             # param string
    create_button: Button = None           # button
    to_login_button: Button = None         # button

    def __init__(self, widget: QWidget, *args, **kwargs):
        super(CreatePageUI, self).__init__(widget)
        self._init_ui()

    def _init_ui(self):
        # set size policy with a fixed height
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Fix size
        self.setFixedSize(580, 580)

        window_layout = VerticalLayout(self)

        self.title_section = Frame(self, name="create_title_section")
        window_layout.addWidget(self.title_section)
        self._init_title_section()

        self.input_section = Frame(self, name="create_input_section")
        window_layout.addWidget(self.input_section)
        self._init_input_section()

        spacer = VerticalSpacer()
        window_layout.addItem(spacer)

        self.button_section = Frame(self, name="create_button_section")
        window_layout.addWidget(self.button_section)
        self._init_button_section()

        self.switch_section = Frame(self, name="switch_section")
        window_layout.addWidget(self.switch_section)
        self._init_switch_section()


    def _init_title_section(self):
        
        section_layout = VerticalLayout(self.title_section, space= 28)
        
        title = Label(
            self.title_section, text="Create An Account.", name="create_title"
        )
        section_layout.addWidget(title)

        prologue = Label(
            self.title_section, text="please enter your information.", name="create_prologue"
        )
        section_layout.addWidget(prologue)

        spacer = VerticalSpacer()
        section_layout.addItem(spacer)

    def _init_input_section(self):

        section_layout = VerticalLayout(self.input_section, space=8)

        name_section = Frame(self.input_section)
        section_layout.addWidget(name_section)

        name_layout = HorizontalLayout(name_section, space=8)

        self.first = LoginInputFrame(
            name_section, title="FIRST NAME", title_width=100, hint="First name..."
        )
        name_layout.addWidget(self.first)

        self.last = LoginInputFrame(
            name_section, title="LAST NAME", title_width=100, hint="Last name..."
        )
        name_layout.addWidget(self.last)

        self.username = LoginInputFrame(
            self.input_section, title="EMAIL", hint="Please enter an email address as your username..."
        )
        section_layout.addWidget(self.username)

        self.pwd = LoginInputFrame(
            self.input_section, title="PASSWORD", hint="Please enter your password...", echo=True
        )
        section_layout.addWidget(self.pwd)

        self.confirm_pwd = LoginInputFrame(
            self.input_section, title="CONFIRM PASSWORD", hint="Please re-enter your password...", echo=True
        )
        section_layout.addWidget(self.confirm_pwd)

    def _init_button_section(self):

        section_layout = VerticalLayout(self.button_section, space=10)

        self.create_hint = Label(self.button_section, text="", name="login_hint")
        section_layout.addWidget(self.create_hint)

        self.create_button = Button(
            self.button_section, text="CREATE ACCOUNT", name="action_button", cursor=True
        )
        section_layout.addWidget(self.create_button)

    def _init_switch_section(self):

        section_layout = HorizontalLayout(self.switch_section)

        label = Label(
            self.switch_section, text="Already a member?", name="switch_label", align=(Qt.AlignRight | Qt.AlignVCenter)
        )
        section_layout.addWidget(label)

        self.to_login_button = Button(
            self.switch_section, text="Login Here.", name="switch_button", cursor=True
        )
        section_layout.addWidget(self.to_login_button)
