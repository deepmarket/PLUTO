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
        self.fade_widget = None

        self._init_geometry()
        self._init_ui()

        self.show()

    def _init_geometry(self):
        # window size
        set_base_geometry(self, WINDOW_WIDTH, WINDOW_HEIGHT, fixed=True)

        # hide title bar
        # self.setWindowFlags(Qt.FramelessWindowHint)

    def _init_ui(self):
        window = QFrame(self)
        self.setCentralWidget(window)
        self.stack = add_layout(window, STACK)

        # login page
        self.login_page = LoginPage(self)
        self.stack.addWidget(self.login_page)

        # main page
        self.main_page = MainPage(self)
        self.stack.addWidget(self.main_page)

        self.login_page.to_main_page_signal.connect(self.to_main_page)
        self.main_page.to_login_page_signal.connect(self.to_login_page)

    def to_main_page(self):
        self.main_page.init_main_page()
        self.fade_widget = FadeWidget(self.login_page, self.main_page)
        self.stack.setCurrentIndex(1)

    def to_login_page(self):
        self.login_page.init_login_page()
        self.fade_widget = FadeWidget(self.main_page, self.login_page)
        self.stack.setCurrentIndex(0)
