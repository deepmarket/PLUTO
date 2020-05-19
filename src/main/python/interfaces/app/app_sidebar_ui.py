from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtCore import Qt

from ..widgets import Frame, VerticalLayout, VerticalSpacer, Label, Button


class AppSidebarUI(Frame):

    dashboard: Button = None
    resources: Button = None
    jobs: Button = None
    settings: Button = None

    def __init__(
        self, parent, cxt: ApplicationContext, width: int, height: int, *args, **kwargs
    ):
        super(AppSidebarUI, self).__init__(parent, name="sidebar")

        self.cxt = cxt

        self._init_ui(width, height)

        self.setStyleSheet(self.cxt.app_style)

    def reload_stylesheet(self):
        """
        This function resets the app's style sheet
        :return:
        """
        self.setStyleSheet(self.cxt.app_style)

    def on_dashboard_clicked(self):
        """
        This event is called on the click of Dashboard button.
        Changes the style of Dashboard button to reflect
        its active status.
        :return:
        """
        self.reset()
        self.dashboard.setObjectName("sidebar_button_active")
        self.reload_stylesheet()

    def on_resources_clicked(self):
        """
        This event is called on click of Resources button.
        Changes the style of Resources button to reflect
        its active status.
        :return:
        """
        self.reset()
        self.resources.setObjectName("sidebar_button_active")
        self.reload_stylesheet()

    def on_jobs_clicked(self):
        """
        This event is called on click of Jobs button.
        Changes the style of Jobs button to reflect
        its active status.
        :return:
        """
        self.reset()
        self.jobs.setObjectName("sidebar_button_active")
        self.reload_stylesheet()

    def on_settings_clicked(self):
        """
        This event is called on click of Settings button.
        Changes the style of Settings button to reflect
        its active status.
        :return:
        """
        self.reset()
        self.settings.setObjectName("sidebar_button_active")
        self.reload_stylesheet()

    def reset(self):
        """
        This functions sets all widget to base styles
        and let clicked callback override them
        :return:
        """
        self.dashboard.setObjectName("sidebar_button")
        self.resources.setObjectName("sidebar_button")
        self.jobs.setObjectName("sidebar_button")
        self.settings.setObjectName("sidebar_button")

    def _init_ui(self, width: int, height: int):
        """
        This function initializes the sidebar UI.
        It adds buttons for dashboard, resources,
        jobs and settings.
        :param width:
        :param height:
        :return:
        """

        self.setFixedSize(width, height)

        window_layout = VerticalLayout(self)

        # title
        title = Label(self, text="PLUTO", name="sidebar_title", align=Qt.AlignHCenter)
        window_layout.addWidget(title)

        # button frame: dashboard, resources, jobs
        button_frame = Frame(self, name="sidebar_button_frame")
        button_layout = VerticalLayout(button_frame, space=18)
        window_layout.addWidget(button_frame)

        # dashboard
        self.dashboard = Button(
            button_frame, text="Dashboard", name="sidebar_button_active", cursor=True
        )
        button_layout.addWidget(self.dashboard)

        # resources
        self.resources = Button(
            button_frame, text="Resources", name="sidebar_button", cursor=True
        )
        button_layout.addWidget(self.resources)

        # jobs
        self.jobs = Button(
            button_frame, text="Jobs", name="sidebar_button", cursor=True
        )
        button_layout.addWidget(self.jobs)

        # settings
        self.settings = Button(
            button_frame, text="Settings", name="sidebar_button", cursor=True
        )
        button_layout.addWidget(self.settings)

        spacer = VerticalSpacer()
        window_layout.addItem(spacer)
