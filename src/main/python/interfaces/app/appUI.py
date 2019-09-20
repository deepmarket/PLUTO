from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.Qt import QMainWindow

from PyQt5.QtCore import pyqtSignal

from .appSidebarUI import AppSidebarUI
from .appNavigationUI import AppNavigationUI
from .appMainWindowUI import AppMainWindowUI
from .appMaskUI import AppMaskUI
from .appAccountUI import AppAccountUI

from ..widgets import Frame

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
        self.account.move(self.width() - ACCOUNT_WIDTH, 0)