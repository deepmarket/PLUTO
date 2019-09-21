from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.Qt import Qt

from ..widgets import (
    Frame,
    VerticalLayout,
    VerticalSpacer,
    Label,
    Button,
)

class AppSidebarUI(Frame):

    dashboard: Button = None           
    resources: Button = None           
    jobs: Button = None
    settings: Button = None               

    def __init__(self, parent, cxt:ApplicationContext, width: int, height: int, *args, **kwargs):
        super(AppSidebarUI, self).__init__(parent, name="sidebar")

        self._init_ui(width, height)

        self.setStyleSheet(cxt.app_style)
    
    def _init_ui(self, width: int, height: int):

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
        self.dashboard = Button(button_frame, text="Dashboard", name="sidebar_button_active", cursor=True)
        button_layout.addWidget(self.dashboard)

        # resources
        self.resources = Button(button_frame, text="Resources", name="sidebar_button", cursor=True)
        button_layout.addWidget(self.resources)

        # jobs
        self.jobs = Button(button_frame, text="Jobs", name="sidebar_button", cursor=True)
        button_layout.addWidget(self.jobs)

        # settings
        self.settings = Button(button_frame, text="Settings", name="sidebar_button", cursor=True)
        button_layout.addWidget(self.settings)

        spacer = VerticalSpacer()
        window_layout.addItem(spacer)
        