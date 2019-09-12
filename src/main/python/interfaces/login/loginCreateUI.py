from api import Api
from uix.stylesheet import *
from uix.util import *
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QSizePolicy, QWidget


class CreatePageUI(QFrame):
    def __init__(self, widget: QWidget, signal: pyqtSignal, cxt:ApplicationContext, *args, **kwargs):
        super(CreatePageUI, self).__init__(widget)

        self.cxt = cxt
        self.signal = signal

"""
class CreatePage(QFrame):
    def __init__(self, parent, cxt:ApplicationContext, *args, **kwargs):
        super(QFrame, self).__init__(parent, *args, **kwargs)

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

        self.setStyleSheet(cxt.login_style)

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

        title = add_label(title_frame, "Create An Account.", name="Login_create_title")
        title_layout.addWidget(title)

        prologue = "please enter your information."
        prologue = add_label(title_frame, prologue, name="Login_prologue")
        title_layout.addWidget(prologue)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        title_layout.addItem(spacer)

        input_frame = QFrame(self)
        input_layout = add_layout(input_frame, VERTICAL, l_m=8, r_m=8, space=8)

        input_sub_frame = QFrame(input_frame)
        input_sub_layout = add_layout(input_sub_frame, HORIZONTAL, space=8)

        box, self.first = add_login_input_box(input_sub_frame, "FIRST NAME", title_width=100, hint="First name...")
        input_sub_layout.addWidget(box)

        box, self.last = add_login_input_box(input_sub_frame, "LAST NAME", title_width=100, hint="Last name...")
        input_sub_layout.addWidget(box)
        input_layout.addWidget(input_sub_frame)

        box, self.username = add_login_input_box(input_frame, "EMAIL",
                                                 hint="Please enter an email address as your username...")
        input_layout.addWidget(box)

        box, self.pwd = add_login_input_box(input_frame, "PASSWORD", hint="Please enter your password...", echo=True)
        input_layout.addWidget(box)

        box, self.confirm_pwd = add_login_input_box(input_frame, "CONFIRM PASSWORD",
                                                    hint="Please re-enter your password...", echo=True)
        input_layout.addWidget(box)

        # button_frame: hint, create_button
        button_frame = QFrame(self)
        button_layout = add_layout(button_frame, VERTICAL, l_m=8, r_m=8, space=10)

        self.create_hint = add_label(button_frame, "", name="Login_hint")
        button_layout.addWidget(self.create_hint)

        self.create_button = add_button(button_frame, "CREATE ACCOUNT", name="Login_large_button")
        button_layout.addWidget(self.create_button)

        # to_create_frame: to_create_button
        to_login_frame = QFrame(self)
        to_login_frame.setFixedHeight(63)
        to_login_layout = add_layout(to_login_frame, HORIZONTAL, l_m=8, r_m=8, b_m=8, t_m=8)

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
        
"""