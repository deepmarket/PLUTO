from abc import ABCMeta, abstractmethod
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

from .app_sidebar_ui import AppSidebarUI
from .app_navigation_ui import AppNavigationUI
from .app_main_window_ui import AppMainWindowUI
from .app_mask_ui import AppMaskUI
from .app_account_ui import AppAccountUI

from ..widgets import Frame, MoveAnimation
from ..config import SIDEBAR_WIDTH, NAVIGATION_HEIGHT, ACCOUNT_WIDTH


class AppUI(QMainWindow):

    # metaclass for defining abstract base classes
    __metaclass__ = ABCMeta

    sidebar: AppSidebarUI = None
    navigation: AppNavigationUI = None
    main_window: AppMainWindowUI = None
    mask: AppMaskUI = None
    account: AppAccountUI = None

    def __init__(self, cxt: ApplicationContext, *args, **kwargs):
        super(AppUI, self).__init__(*args, **kwargs)

        self.cxt = cxt

        self._init_ui()
        self.setStyleSheet(self.cxt.app_style)

    def on_menu_clicked(self):
        """
        This function loads Accounts UI.
        """

        mask_action = MoveAnimation(self.mask, self.width(), 0, 0, 0, duration=0)
        menu_action = MoveAnimation(
            self.account, self.width(), 0, self.width() - ACCOUNT_WIDTH, 0
        )

        mask_action.start()
        menu_action.start()

    def on_mask_clicked(self):
        """
        This function closes menu.
        """

        menu_action = MoveAnimation(
            self.account, self.width() - ACCOUNT_WIDTH, 0, self.width(), 0
        )
        mask_action = MoveAnimation(self.mask, 0, 0, self.width(), 0, duration=0)

        menu_action.start()
        mask_action.start()

    @abstractmethod
    def on_dashboard_clicked(self):
        pass

    @abstractmethod
    def on_resources_clicked(self):
        pass

    @abstractmethod
    def on_jobs_clicked(self):
        pass

    @abstractmethod
    def on_settings_clicked(self):
        pass

    @abstractmethod
    def on_credit_history_clicked(self):
        pass

    @abstractmethod
    def on_notification_clicked(self):
        pass

    @abstractmethod
    def on_about_clicked(self):
        pass

    @abstractmethod
    def on_logout_clicked(self):
        pass

    def _init_ui(self):
        """
        This function initializes the UI for
        application.
        In turn initializes the UI for Sidebar, Navigation,
        Main Window, Account.
        :return:
        """

        # set window init size
        self.resize(1024, 720)

        # set window resize constrains
        self.setFixedSize(1024, 720)

        # centralize window
        dw = QDesktopWidget()
        self.move(
            dw.availableGeometry().center().x() - self.width() * 0.5,
            dw.availableGeometry().center().y() - self.height() * 0.5,
        )

        window = Frame(self)
        self.setCentralWidget(window)

        # sidebar
        self.sidebar = AppSidebarUI(window, self.cxt, SIDEBAR_WIDTH, self.height())
        self.sidebar.move(0, 0)

        # navigation
        self.navigation = AppNavigationUI(
            window, self.cxt, self.width() - SIDEBAR_WIDTH, NAVIGATION_HEIGHT
        )
        self.navigation.move(SIDEBAR_WIDTH, 0)

        # main window
        self.main_window = AppMainWindowUI(
            window,
            self.cxt,
            self.width() - SIDEBAR_WIDTH,
            self.height() - NAVIGATION_HEIGHT,
        )
        self.main_window.move(SIDEBAR_WIDTH, NAVIGATION_HEIGHT)

        # mask
        self.mask = AppMaskUI(window, self.cxt, self.width(), self.height())
        self.mask.move(self.width(), 0)

        # account
        self.account = AppAccountUI(window, self.cxt, ACCOUNT_WIDTH, self.height())
        self.account.move(self.width(), 0)

        # connect function
        self.sidebar.dashboard.clicked.connect(self.on_dashboard_clicked)
        self.sidebar.resources.clicked.connect(self.on_resources_clicked)
        self.sidebar.jobs.clicked.connect(self.on_jobs_clicked)
        self.sidebar.settings.clicked.connect(self.on_settings_clicked)

        self.navigation.menu_button.clicked.connect(self.on_menu_clicked)

        self.mask.clicked_area.clicked.connect(self.on_mask_clicked)

        self.account.credit_history.clicked.connect(self.on_credit_history_clicked)
        self.account.notifications.clicked.connect(self.on_notification_clicked)
        # self.account.about.clicked.connect(self.on_about_clicked)
        self.account.logout.clicked.connect(self.on_logout_clicked)
