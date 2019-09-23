from fbs_runtime.application_context.PyQt5 import ApplicationContext
from api import Api
from uix.util import *
from dashboard import Dashboard
from resources import Resources
from settings import Settings
from jobs import Jobs
from uix.popup import Notification, CreditHistory
from PyQt5.QtCore import pyqtSignal


app_sidebar_button = f"""
    border: None;
    height: 20px;
    padding-left: 16px;
    font-family: "Helvetica Neue";
    font-size: 13px;
    font-weight: 400;
    color: {COLOR_02};
    text-align: left;
"""

app_sidebar_button_active = f"""
    border: None;
    border-left: 2px solid {COLOR_01};
    height: 20px;
    padding-left: 16px;
    font-family: "Helvetica Neue";
    font-size: 13px;
    font-weight: 400;
    color: {COLOR_01};
    text-align: left;
"""

class App(QMainWindow):
    def __init__(self, logout_signal:pyqtSignal, cxt:ApplicationContext, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)

        self.logout_signal = logout_signal

        # component
        self.sidebar = None
        self.navigation = None
        self.main_window = None
        self.mask = None
        self.account = None

        # gui property
        # self.pos = None
        self.animation = None

        self.cxt = cxt

        self._init_geometry()
        self._init_ui()
        self.setStyleSheet(self.cxt.app_style)
        # self.show()

        self.on_dashboard_clicked()

    def _init_geometry(self):
        # window size
        set_base_geometry(self, 1024, 720, fixed=True)

        # hide title bar
        # self.setWindowFlags(Qt.FramelessWindowHint)

    def _init_ui(self):
        self.setObjectName("App")

        sidebar_width = 100
        navigation_height = 45

        window = QFrame(self)
        self.setCentralWidget(window)

        # side bar
        self.sidebar = SideBar(window, self.cxt)
        self.sidebar.setFixedSize(sidebar_width, self.height())
        self.sidebar.move(0, 0)

        # top navigation
        self.navigation = Navigation(window, self.cxt)
        self.navigation.setFixedSize(self.width()-sidebar_width, navigation_height)
        self.navigation.move(sidebar_width, 0)

        self.main_window = MainWindow(window, self.cxt)
        self.main_window.setFixedSize(self.width()-sidebar_width, self.height()-navigation_height)
        self.main_window.move(sidebar_width, navigation_height)

        # mask & right account bar
        self.mask = Mask(window, self.cxt)
        self.mask.setFixedSize(self.width(), self.height())
        self.mask.move(self.width(), 0)
        self.mask.clicked_area.setFixedSize(self.width(), self.height())
        self.mask.clicked_area.move(0, 0)

        self.account = Account(self.mask, self.cxt)
        self.account.setFixedSize(200, self.height())
        self.account.move(self.mask.width()-200, 0)

        # connect function
        self.sidebar.dashboard.clicked.connect(self.on_dashboard_clicked)
        self.sidebar.resources.clicked.connect(self.on_resources_clicked)
        self.sidebar.jobs.clicked.connect(self.on_jobs_clicked)
        self.sidebar.settings.clicked.connect(self.on_settings_clicked)

        self.navigation.menu_button.clicked.connect(self.on_menu_clicked)

        self.mask.clicked_area.clicked.connect(self.on_mask_clicked)

        self.account.credit_history.clicked.connect(self.on_credit_history_clicked)
        self.account.notifications.clicked.connect(self.on_notification_clicked)
        self.account.about.clicked.connect(self.on_about_clicked)
        self.account.logout.clicked.connect(self.on_logout_clicked)

    # # mouse graping and window moves
    # def mousePressEvent(self, event):
    #     self.pos = event.globalPos()
    #
    # # mouse graping and window moves
    # def mouseMoveEvent(self, event):
    #     delta = QPoint(event.globalPos() - self.pos)
    #     self.move(self.x() + delta.x(), self.y() + delta.y())
    #     self.pos = event.globalPos()

    def on_sidebar_widget_updated(self, widget=None):
        """
        This is a helper function that is called *manually* by the `clicked` callback function
        attached to each of the sidebar widgets.

        Its purpose is to reset each sidebar widgets style to default and manage the
        widget stack

        :param widget: The clicked on widget that we want to instantiate
        :return: None
        """

        # Set all widget to base styles and let clicked callback override them
        self.sidebar.dashboard.setStyleSheet(app_sidebar_button)
        self.sidebar.resources.setStyleSheet(app_sidebar_button)
        self.sidebar.jobs.setStyleSheet(app_sidebar_button)
        self.sidebar.settings.setStyleSheet(app_sidebar_button)

        # Deallocate current widget if it exists
        if self.main_window.stack.count():
            self.main_window.stack.currentWidget().setParent(None)

        if widget is not None:
            self.main_window.stack_widget = widget(self.cxt)
            self.main_window.stack.addWidget(self.main_window.stack_widget)
        else:
            # Default to dashboard I guess?
            self.main_window.stack_widget = Dashboard(self.cxt)
            self.main_window.stack.addWidget(self.main_window.stack_widget)

    def on_dashboard_clicked(self):
        self.on_sidebar_widget_updated(Dashboard)
        self.sidebar.dashboard.setStyleSheet(app_sidebar_button_active)

    def on_resources_clicked(self):
        self.on_sidebar_widget_updated(Resources)
        self.sidebar.resources.setStyleSheet(app_sidebar_button_active)

    def on_jobs_clicked(self):
        self.on_sidebar_widget_updated(Jobs)
        self.sidebar.jobs.setStyleSheet(app_sidebar_button_active)

    def on_settings_clicked(self):
        self.on_sidebar_widget_updated(Settings)
        self.sidebar.settings.setStyleSheet(app_sidebar_button_active)

    # open menu
    def on_menu_clicked(self):
        self.animation = QSequentialAnimationGroup()

        mask_action = add_move_animation(self.mask, self.width(), 0, 0, 0, duration=0)
        menu_action = add_move_animation(self.account, self.mask.width(), 0, self.mask.width() - 200, 0)

        self.animation.addAnimation(mask_action)
        self.animation.addAnimation(menu_action)

        self.animation.start()

    # close menu
    def on_mask_clicked(self):
        self.animation = QSequentialAnimationGroup()

        menu_action = add_move_animation(self.account, self.mask.width()-200, 0, self.mask.width(), 0)
        mask_action = add_move_animation(self.mask, 0, 0, self.width(), 0, duration=0)

        self.animation.addAnimation(menu_action)
        self.animation.addAnimation(mask_action)

        self.animation.start()

    # notification popup
    def on_notification_clicked(self):
        popup = Notification(self.cxt)
        popup.exec_()

    # credit history popup
    def on_credit_history_clicked(self):
        popup = CreditHistory(self.cxt)
        popup.exec_()

    @staticmethod
    def on_about_clicked():
        # popup = CreditHistory()
        # popup.exec_()
        ...

    def on_logout_clicked(self):
        with Api("/auth/logout") as account_api:
            status, res = account_api.post()

            if status == 200:
                # Delete file storing token
                account_api.store.remove()

                self.close()
                self.logout_signal.emit()

    def update(self):
        self.main_window.stack_widget.update()


# Pure UI class, no functionality
class SideBar(QFrame):
    def __init__(self, parent, cxt:ApplicationContext, *args, **kwargs):
        super(SideBar, self).__init__(parent, *args, **kwargs)

        # variable
        self.dashboard = None           # button
        self.resources = None           # button
        self.jobs = None                # button

        self._init_ui()

        self.setStyleSheet(cxt.app_style)

    def _init_ui(self):
        self.setObjectName("App_sidebar")

        section_layout = add_layout(self, VERTICAL)

        # title frame: title, logo
        title_frame = QFrame(self)
        title_layout = add_layout(title_frame, VERTICAL, t_m=12)

        title = add_label(title_frame, "PLUTO", name="App_sidebar_title", align=Qt.AlignHCenter)

        title_layout.addWidget(title)

        # button frame: dashboard, resources, jobs
        button_frame_01 = QFrame(self)
        button_layout = add_layout(button_frame_01, VERTICAL, t_m=50, space=18)

        self.dashboard = add_button(button_frame_01, "Dashboard", name="dashboard",  stylesheet=app_sidebar_button_active)

        self.resources = add_button(button_frame_01, "Resources", name="resources", stylesheet=app_sidebar_button)

        self.jobs = add_button(button_frame_01, "Jobs", name="jobs", stylesheet=app_sidebar_button)

        self.settings = add_button(button_frame_01, "Settings", name="settings", stylesheet=app_sidebar_button)

        button_layout.addWidget(self.dashboard)
        button_layout.addWidget(self.resources)
        button_layout.addWidget(self.jobs)
        button_layout.addWidget(self.settings)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        section_layout.addWidget(title_frame)
        section_layout.addWidget(button_frame_01)
        section_layout.addItem(spacer)


# Pure UI class, no functionality
class Navigation(QFrame):
    def __init__(self, parent, cxt:ApplicationContext, *args, **kwargs):
        super(Navigation, self).__init__(parent, *args, **kwargs)

        with Api("/account") as account:
            status, res = account.get()

            if status == 200:
                self.credits = round(res['account']['credits'], 4)

            # TODO: This fails if the api returns a token expired error
            # (or anything that isn't a customer object response). Also see Account class with same problem
            # TODO: This should never happen and if it does we should report a fatal error
            else:
                self.credits = 0.0

        self.head_img = None
        self.menu_button = None
        self._init_ui()

        self.setStyleSheet(cxt.app_style)

    def _init_ui(self):
        self.setObjectName("App_navigation")

        section_layout = add_layout(self, HORIZONTAL, align=Qt.AlignVCenter, space=16)

        credit = add_label(self, f"CREDITS: {self.credits}", name="App_navigation_credit")

        self.menu_button = add_button(self, name="App_navigation_button")

        width = 17

        self.menu_button.setIcon(add_menu_icon(width))
        self.menu_button.setIconSize(QSize(width, width))

        spacer_01 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        spacer_02 = QSpacerItem(18, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        section_layout.addItem(spacer_01)
        section_layout.addWidget(credit)
        section_layout.addWidget(self.menu_button)
        section_layout.addItem(spacer_02)


# Pure UI class, no functionality
class MainWindow(QFrame):
    def __init__(self, parent, cxt:ApplicationContext, *args, **kwargs):
        super(MainWindow, self).__init__(parent, *args, **kwargs)

        # variable
        self.stack = None               # stack layout
        self.stack_widget = None        # current widget

        self._init_ui()
        self.setStyleSheet(cxt.app_style)

    def _init_ui(self):
        self.setObjectName("App_main_window")

        self.stack = add_layout(self, STACK)


# Pure UI class, no functionality
class Mask(QFrame):
    def __init__(self, parent, cxt:ApplicationContext, *args, **kwargs):
        super(Mask, self).__init__(parent, *args, **kwargs)

        self.setStyleSheet(cxt.app_style)
        self.setObjectName("App_mask")

        self.clicked_area = add_button(self, name="App_mask_clicked_area", change_cursor=False)


# Pure UI class, no functionality
class Account(QFrame):
    def __init__(self, parent, cxt:ApplicationContext, *args, **kwargs):
        super(Account, self).__init__(parent, *args, **kwargs)

        self.head_img = None                # image filename string

        with Api("/account") as account_api:
            status, res = account_api.get()

            if status == 200:
                # Insert comma here so we can default to nameless greeting if api fails.
                self.username = f"{res['account']['firstname'].capitalize()}"
                self.credits = round(res['account']['credits'], 4)
            # TODO: This should never happen and if it does we should report a fatal error
            else:
                self.username = "New User"
                self.credits = 0.0

        self.credit = 15                    # parameter integer
        self.credit_history = None          # button
        self.notification = None            # button
        self.setting_button = None          # button
        self.logout = None                  # button

        self._init_ui()
        self.setStyleSheet(cxt.app_style)

    def _init_ui(self):
        self.setObjectName("App_account")

        # shadow
        effect = QGraphicsDropShadowEffect()
        effect.setBlurRadius(20)
        effect.setXOffset(0)
        effect.setYOffset(0)
        effect.setColor(QColor(COLOR_02))

        self.setGraphicsEffect(effect)

        section_layout = add_layout(self, VERTICAL, l_m=15, r_m=15, t_m=20, b_m=20)

        # title frame
        title_frame = QFrame(self)
        title_frame.setObjectName("App_title_frame")
        title_layout = add_layout(title_frame, HORIZONTAL, b_m=15)

        username = add_label(title_frame, f"{self.username}", name="App_account_username", align=Qt.AlignVCenter)
        credit = add_label(title_frame, f"Credits: {self.credits}", name="App_account_credit", align=Qt.AlignVCenter)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        title_layout.addWidget(username)
        title_layout.addItem(spacer)
        title_layout.addWidget(credit)

        # button frame
        button_frame = QFrame(self)
        button_layout = add_layout(button_frame, VERTICAL, t_m=42, l_m=7, r_m=7, space=18)

        self.credit_history = add_button(button_frame, "Credit History", name="App_account_button")
        self.notifications = add_button(button_frame, "Notifications", name="App_account_button")
        self.about = add_button(button_frame, "About", name="App_account_button")

        button_layout.addWidget(self.notifications)
        button_layout.addWidget(self.credit_history)
        button_layout.addWidget(self.about)

        # bottom frame
        bottom_frame = QFrame(self)
        bottom_layout = add_layout(bottom_frame, HORIZONTAL)

        self.logout = add_button(bottom_frame, "Logout", name="App_account_logout")

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        bottom_layout.addItem(spacer)
        bottom_layout.addWidget(self.logout)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        section_layout.addWidget(title_frame)
        section_layout.addWidget(button_frame)
        section_layout.addItem(spacer)
        section_layout.addWidget(bottom_frame)
