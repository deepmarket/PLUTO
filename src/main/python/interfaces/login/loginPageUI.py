from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtCore import Qt, pyqtSignal
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

class LoginPageUI(Frame):

    title_section: Frame = None
    login_section: Frame = None
    button_section: Frame = None

    username = None                # input string
    pwd = None                     # input string
    login_button = None            # button
    login_hint = None              # param string
    remember_check = None          # checkbox
    to_forget_pwd = None           # button
    to_create_button = None        # button

    def __init__(self, widget: QWidget, login_signal: pyqtSignal, cxt:ApplicationContext, *args, **kwargs):
        super(LoginPageUI, self).__init__(widget)

        self.cxt = cxt    
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

        section_layout = VerticalLayout(self.title_section)
        label = Label(
            self.title_section, text="Welcome.", name="login_title", align=Qt.AlignCenter
        )
        section_layout.addWidget(label)

    def _init_input_section(self):

        section_layout = VerticalLayout(self.input_section, space=20)
        
        self.username = LoginInputFrame(
            self.input_section, title="U S E R N A M E", hint="Enter your email address..."
        )

        section_layout.addWidget(self.username)
        
        self.pwd = LoginInputFrame(
            self.input_section, title="P A S S W O R D", hint="Enter your password...", echo=True
        )
        section_layout.addWidget(self.pwd)

    def _init_button_section(self):

        section_layout = VerticalLayout(self.button_section, space=10)

        self.login_hint = Label(self.button_section, text="test", name="login_hint")
        section_layout.addWidget(self.login_hint)

        self.login_button = Button(self.button_section, text="LOG IN", name="action_button")
        section_layout.addWidget(self.login_button)

    def _init_switch_section(self):

        section_layout = HorizontalLayout(self.switch_section)

        label = Label(
            self.switch_section, text="Not a Member?", name="switch_label", align=(Qt.AlignRight | Qt.AlignVCenter)
        )
        section_layout.addWidget(label)

        self.to_create_button = Button(
            self.switch_section, text="Create An Account.", name="switch_button", cursor=True
        )
        section_layout.addWidget(self.to_create_button)

"""
class LoginPage(QFrame):
    def __init__(self, parent, cxt:ApplicationContext, *args, **kwargs):
        super(QFrame, self).__init__(parent, *args, **kwargs)

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

        self.setStyleSheet(cxt.login_style)

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

        # title = add_label(title_frame, "Welcome.", name="Login_login_title", align=Qt.AlignCenter)
        # title_layout.addWidget(title)

        # Broken
        def login_kindly():
            def update_title(title_text: str="Please Sign In."):
                title = add_label(title_frame, title_text, name="Login_login_title", align=Qt.AlignCenter)
                title_layout.addWidget(title)

            update_title("Welcome.")

            timer = QTimer()
            timer.timeout.connect(update_title)
            timer.start(3500)

        login_kindly()

        # login_frame: username, pwd, login_button
        login_frame = QFrame(self)
        login_layout = add_layout(login_frame, VERTICAL, t_m=20, space=20)

        box, self.username = add_login_input_box(login_frame, "U S E R N A M E", title_width=150,
                                                 hint="Enter your email address...")
        login_layout.addWidget(box)

        box, self.pwd = add_login_input_box(login_frame, "P A S S W O R D", title_width=150,
                                            hint="Enter your password...", echo=True)
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

        self.to_create_button = add_button(to_create_frame, "Create An Account.", name="Login_switch_button")
        to_create_layout.addWidget(self.to_create_button)

        # spacer
        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        window_layout.addWidget(title_frame)
        window_layout.addWidget(login_frame)
        window_layout.addItem(spacer)
        window_layout.addWidget(button_frame)
        window_layout.addWidget(to_create_frame)
"""