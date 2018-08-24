"""
    The following items can be interacted:

    class SideBar:

        self.dashboard = None               # button
        self.resources = None               # button
        self.jobs = None                    # button

    class Navigation:

        self.credit = 0                     # input number
        self.head_img = None                # input string
        self.menu_button = None             # button


    class MainWindow:

        self.stack = None                   # stack layout
        self.dashboard = None               # section
        self.resources = None               # section
        self.jobs = None                    # section

    class Mask:

        self.clicked_area                   # button

    class Account:

        self.head_img = None                # image filename string
        self.username = "Martin Li"         # parameter string
        self.credit = 15                    # parameter integer
        self.credit_history = None          # button
        self.notification = None            # button
        self.setting_button = None          # button
        self.logout = None                  # button

"""
from src.api import Api
from src.uix.util import *
from src.main_page import MainPage


class App(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)

        self._init_geometry()

        # component
        self.main_page = MainPage(self)
        self.setCentralWidget(self.main_page)
        self.show()

    def _init_geometry(self):
        # window size
        set_base_geometry(self, 1024, 720, fixed=True)

        # hide title bar
        # self.setWindowFlags(Qt.FramelessWindowHint)
