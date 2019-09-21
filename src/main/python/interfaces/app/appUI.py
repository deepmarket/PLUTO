from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.Qt import QMainWindow

from PyQt5.QtCore import pyqtSignal

from .appSidebarUI import AppSidebarUI
from .appNavigationUI import AppNavigationUI
from .appMainWindowUI import AppMainWindowUI
from .appMaskUI import AppMaskUI
from .appAccountUI import AppAccountUI

from ..widgets import Frame, MoveAnimation

from ..config import SIDEBAR_WIDTH, NAVIGATION_HEIGHT, ACCOUNT_WIDTH

class AppUI(QMainWindow):

    sidebar: AppSidebarUI = None
    navigation: AppNavigationUI = None
    main_window: AppMainWindowUI = None
    mask: AppMaskUI = None
    account: AppAccountUI = None

    def __init__(self, logout_signal:pyqtSignal, cxt:ApplicationContext, *args, **kwargs):
        super(AppUI, self).__init__(*args, **kwargs)

        self.logout_signal = logout_signal

        self.cxt = cxt

        self._init_ui()
        self.setStyleSheet(self.cxt.app_style)

    def on_menu_clicked(self):
        """
        open menu
        """

        mask_action = MoveAnimation(self.mask, self.width(), 0, 0, 0, duration=0)
        menu_action = MoveAnimation(self.account, self.width(), 0, self.width() - ACCOUNT_WIDTH, 0)
        
        mask_action.start()
        menu_action.start()

    def on_mask_clicked(self):
        """
        close menu
        """

        menu_action = MoveAnimation(self.account, self.width()-ACCOUNT_WIDTH, 0, self.width(), 0)
        mask_action = MoveAnimation(self.mask, 0, 0, self.width(), 0, duration=0)

        menu_action.start()
        mask_action.start()

    def _init_ui(self):

        # set window init size
        self.resize(1024, 720)

        # set window resize constrains
        self.setFixedSize(1024, 720)

        window = Frame(self)
        self.setCentralWidget(window)

        # sidebar
        self.sidebar = AppSidebarUI(window, self.cxt, SIDEBAR_WIDTH, self.height())
        self.sidebar.move(0, 0)

        # navigation
        self.navigation = AppNavigationUI(window, self.cxt, self.width() - SIDEBAR_WIDTH, NAVIGATION_HEIGHT)
        self.navigation.move(SIDEBAR_WIDTH, 0)

        # mainwindow
        self.main_window = AppMainWindowUI(window, self.cxt, self.width() - SIDEBAR_WIDTH, self.height() - NAVIGATION_HEIGHT)
        self.main_window.move(SIDEBAR_WIDTH, NAVIGATION_HEIGHT)

        # mask
        self.mask = AppMaskUI(window, self.cxt, self.width(), self.height())
        self.mask.move(self.width(), 0)

        # account
        self.account = AppAccountUI(window, self.cxt, ACCOUNT_WIDTH, self.height())
        self.account.move(self.width(), 0)

        # connect function
        self.navigation.menu_button.clicked.connect(self.on_menu_clicked)
        self.mask.clicked_area.clicked.connect(self.on_mask_clicked)