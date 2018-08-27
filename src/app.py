from src.api import Api
from src.uix.util import *
from src.main_page import MainPage
from src.login_page import LoginPage


class App(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)

        # variable
        self.login_page = None
        self.main_page = None
        self.stack = None
        self.stack_widget = None
        self.fade_widget = None

        self._init_geometry()
        self._init_ui()

        self.to_login_page()
        self.show()

    def _init_geometry(self):
        # window size
        set_base_geometry(self, WINDOW_WIDTH, WINDOW_HEIGHT, fixed=True)

        # hide title bar
        # self.setWindowFlags(Qt.FramelessWindowHint)

    def _init_ui(self):
        self.window = QFrame(self)
        self.setCentralWidget(self.window)
        self.stack = add_layout(self.window, STACK)

    def to_main_page(self):
        if self.stack_widget:
            self.stack_widget.signal.disconnect()
            self.stack_widget.setParent(None)
            self.stack_widget = None

        self.stack_widget = MainPage()
        self.stack.addWidget(self.stack_widget)
        self.stack_widget.signal.connect(self.to_login_page)

    def to_login_page(self):
        if self.stack_widget:
            self.stack_widget.signal.disconnect()
            self.stack_widget.setParent(None)
            self.stack_widget = None

        self.stack_widget = LoginPage()
        self.stack.addWidget(self.stack_widget)
        self.stack_widget.signal.connect(self.to_main_page)
