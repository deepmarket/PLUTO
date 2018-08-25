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
from src.interfaces.dashboard import Dashboard
from src.interfaces.resources import Resources
from src.interfaces.jobs import Jobs
from src.uix.popup import Notification, CreditHistory


class MainPage(QFrame):

    to_login_page_signal = pyqtSignal(bool)

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # component
        self.sidebar = None
        self.navigation = None
        self.interface = None
        self.mask = None
        self.account = None

        # gui property
        self.animation = None
        self.sidebar_width = 100
        self.navigation_height = 45
        self.account_width = 200

        self._init_ui()
        self.setStyleSheet(main_style)

        self.on_dashboard_clicked()

    def _init_ui(self):
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        # side bar
        self.sidebar = SideBar(self)
        self.sidebar.setFixedSize(self.sidebar_width, WINDOW_HEIGHT)

        # top navigation
        self.navigation = Navigation(self)
        self.navigation.setFixedSize(WINDOW_WIDTH-self.sidebar_width, self.navigation_height)

        self.interface = CurrentInterface(self)
        self.interface.setFixedSize(WINDOW_WIDTH-self.sidebar_width, WINDOW_HEIGHT-self.navigation_height)

        # mask & right account bar
        self.mask = Mask(self)
        self.mask.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.mask.clicked_area.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.account = Account(self.mask)
        self.account.setFixedSize(self.account_width, WINDOW_HEIGHT)

        self._set_component_loc()

        # connect function
        self.sidebar.dashboard.clicked.connect(self.on_dashboard_clicked)
        self.sidebar.resources.clicked.connect(self.on_resources_clicked)
        self.sidebar.jobs.clicked.connect(self.on_jobs_clicked)
        self.navigation.menu_button.clicked.connect(self.on_menu_clicked)
        self.mask.clicked_area.clicked.connect(self.on_mask_clicked)
        self.account.credit_history.clicked.connect(self.on_credit_history_clicked)
        self.account.notification.clicked.connect(self.on_notification_clicked)
        self.account.logout.clicked.connect(self.on_logout_clicked)

    def _set_component_loc(self):
        self.sidebar.move(0, 0)
        self.navigation.move(self.sidebar_width, 0)
        self.interface.move(self.sidebar_width, self.navigation_height)
        self.mask.move(WINDOW_WIDTH, 0)
        self.mask.clicked_area.move(0, 0)
        self.account.move(self.mask.width() - self.account_width, 0)

    # switch tab to dashboard
    def on_dashboard_clicked(self):
        # active button
        self.sidebar.dashboard.setStyleSheet(main_sidebar_button_active)
        self.sidebar.resources.setStyleSheet(main_sidebar_button)
        self.sidebar.jobs.setStyleSheet(main_sidebar_button)

        # deallocate current widget if they exist
        if self.interface.stack.count():
            self.interface.stack.currentWidget().setParent(None)

        # allocate dashboard object
        self.interface.stack_widget = Dashboard()
        self.interface.stack.addWidget(self.interface.stack_widget)

    # switch tab to resources
    def on_resources_clicked(self):
        self.sidebar.dashboard.setStyleSheet(main_sidebar_button)
        self.sidebar.resources.setStyleSheet(main_sidebar_button_active)
        self.sidebar.jobs.setStyleSheet(main_sidebar_button)

        # deallocate current widget if they exist
        if self.interface.stack.count():
            self.interface.stack.currentWidget().setParent(None)

        # allocate resources object
        self.interface.stack_widget = Resources()
        self.interface.stack.addWidget(self.interface.stack_widget)

    # switch tab to jobs
    def on_jobs_clicked(self):
        self.sidebar.dashboard.setStyleSheet(main_sidebar_button)
        self.sidebar.resources.setStyleSheet(main_sidebar_button)
        self.sidebar.jobs.setStyleSheet(main_sidebar_button_active)

        # deallocate current widget if they exist
        if self.interface.stack.count():
            self.interface.stack.currentWidget().setParent(None)

        self.interface.stack_widget = Jobs()
        self.interface.stack.addWidget(self.interface.stack_widget)

    # open menu
    def on_menu_clicked(self):
        self.animation = QSequentialAnimationGroup()

        mask_action = add_move_animation(self.mask, WINDOW_WIDTH, 0, 0, 0, duration=0)
        menu_action = add_move_animation(self.account, self.mask.width(), 0, self.mask.width() - 200, 0)

        self.animation.addAnimation(mask_action)
        self.animation.addAnimation(menu_action)

        self.animation.start()

    # close menu
    def on_mask_clicked(self):
        self.animation = QSequentialAnimationGroup()

        menu_action = add_move_animation(self.account, self.mask.width()-200, 0, self.mask.width(), 0)
        mask_action = add_move_animation(self.mask, 0, 0, WINDOW_WIDTH, 0, duration=0)

        self.animation.addAnimation(menu_action)
        self.animation.addAnimation(mask_action)

        self.animation.start()

    # notification popup
    @staticmethod
    def on_notification_clicked():
        popup = Notification()
        popup.exec_()

    # credit history popup
    @staticmethod
    def on_credit_history_clicked():
        popup = CreditHistory()
        popup.exec_()

    def on_logout_clicked(self):
        self.to_login_page_signal.emit(True)

    def update(self):
        self.interface.stack_widget.update()

    def init_main_page(self):
        self._set_component_loc()
        self.on_dashboard_clicked()


# Pure UI class, no functionality
class SideBar(QFrame):
    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.dashboard = None           # button
        self.resources = None           # button
        self.jobs = None                # button

        self._init_ui()

        self.setStyleSheet(main_style)

    def _init_ui(self):
        self.setObjectName("Main_sidebar")

        section_layout = add_layout(self, VERTICAL)

        # title frame: title, logo
        title_frame = QFrame(self)
        title_layout = add_layout(title_frame, VERTICAL, t_m=12)

        title = add_label(title_frame, "PLUTO", name="Main_sidebar_title", align=Qt.AlignHCenter)

        title_layout.addWidget(title)

        # button frame: dashboard, resources, jobs
        button_frame_01 = QFrame(self)
        button_layout = add_layout(button_frame_01, VERTICAL, t_m=50, space=18)

        self.dashboard = add_button(button_frame_01, "Dashboard", stylesheet=main_sidebar_button)

        self.resources = add_button(button_frame_01, "Resources", stylesheet=main_sidebar_button)

        self.jobs = add_button(button_frame_01, "Jobs", stylesheet=main_sidebar_button)

        button_layout.addWidget(self.dashboard)
        button_layout.addWidget(self.resources)
        button_layout.addWidget(self.jobs)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        section_layout.addWidget(title_frame)
        section_layout.addWidget(button_frame_01)
        section_layout.addItem(spacer)


# Pure UI class, no functionality
class Navigation(QFrame):
    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        with Api("/account") as account:
            status, res = account.get()

            if status == 200:
                self.credits = round(res['customer']['credits'], 4)

        self.head_img = None
        self.menu_button = None
        self._init_ui()

        self.setStyleSheet(main_style)

    def _init_ui(self):
        self.setObjectName("Main_navigation")

        section_layout = add_layout(self, HORIZONTAL, align=Qt.AlignVCenter, space=16)

        credit = add_label(self, f"CREDITS: {self.credits}", name="Main_navigation_credit")

        self.menu_button = add_button(self, name="Main_navigation_button")

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
class CurrentInterface(QFrame):
    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.stack = None               # stack layout
        self.stack_widget = None        # current widget

        self._init_ui()
        self.setStyleSheet(main_style)

    def _init_ui(self):
        self.setObjectName("Main_current_interface")

        self.stack = add_layout(self, STACK)


# Pure UI class, no functionality
class Mask(QFrame):
    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        self.setStyleSheet(main_style)
        self.setObjectName("Main_mask")

        self.clicked_area = add_button(self, name="Main_mask_clicked_area", change_cursor=False)


# Pure UI class, no functionality
class Account(QFrame):
    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        self.head_img = None                # image filename string

        with Api("/account") as account_api:
            status, res = account_api.get()

            if status == 200:
                # Insert comma here so we can default to nameless greeting if api fails.
                self.username = f"{res['customer']['firstname'].capitalize()}"
                self.credits = round(res['customer']['credits'], 4)
            else:
                self.username = "New User"
                self.credits = 0

        self.credit_history = None          # button
        self.notification = None            # button
        self.setting_button = None          # button
        self.logout = None                  # button

        self._init_ui()
        self.setStyleSheet(main_style)

    def _init_ui(self):
        self.setObjectName("Main_account")

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
        title_frame.setObjectName("Main_title_frame")
        title_layout = add_layout(title_frame, HORIZONTAL, b_m=15)

        username = add_label(title_frame, f"{self.username}", name="Main_account_username", align=Qt.AlignVCenter)
        credit = add_label(title_frame, f"Credits: {self.credits}", name="Main_account_credit", align=Qt.AlignVCenter)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        title_layout.addWidget(username)
        title_layout.addItem(spacer)
        title_layout.addWidget(credit)

        # button frame
        button_frame = QFrame(self)
        button_layout = add_layout(button_frame, VERTICAL, t_m=42, space=5)

        self.credit_history = add_button(button_frame, "Credit History", name="Main_account_button")
        self.notification = add_button(button_frame, "Notification", name="Main_account_button")

        button_layout.addWidget(self.credit_history)
        button_layout.addWidget(self.notification)

        # bottom frame
        bottom_frame = QFrame(self)
        bottom_layout = add_layout(bottom_frame, HORIZONTAL)

        self.logout = add_button(bottom_frame, "Logout", name="Main_account_logout")

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        bottom_layout.addItem(spacer)
        bottom_layout.addWidget(self.logout)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        section_layout.addWidget(title_frame)
        section_layout.addWidget(button_frame)
        section_layout.addItem(spacer)
        section_layout.addWidget(bottom_frame)
