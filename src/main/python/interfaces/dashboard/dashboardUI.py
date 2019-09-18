from fbs_runtime.application_context.PyQt5 import ApplicationContext

from api import Api
from PyQt5.Qt import Qt

from ..widgets import (
    Frame,
    VerticalLayout,
    HorizontalLayout,
    Label,
    HorizontalSpacer,
    VerticalSpacer,
    ViewButton,
    SectionTitleFrame,
    DashboardParamFrame,
)

class DashboardUI(Frame):

    overview_section: Frame = None
    
    title_section: Frame = None
    content_section: Frame = None

    machine_section: Frame = None
    resources_running: DashboardParamFrame = None
    resources_dead: DashboardParamFrame = None

    jobs_section: Frame = None
    jobs_running: DashboardParamFrame = None
    jobs_finish: DashboardParamFrame = None
    jobs_kill: DashboardParamFrame = None

    credit_section: Frame = None

    history_section: Frame = None

    def __init__(self, cxt: ApplicationContext, *args, **kwargs):
        super(DashboardUI, self).__init__(*args, name="dashboard", **kwargs)

        self.cxt = cxt

        # self.get_dashboard_data()
        self._init_ui()
        self.setStyleSheet(self.cxt.dashboard_style)
        
    def _init_ui(self):

        window_layout = VerticalLayout(self, space=5)

        self.overview_section = Frame(self, name="overview_section")
        window_layout.addWidget(self.overview_section)
        self._init_overview_section()

        spacer = VerticalSpacer()
        window_layout.addItem(spacer)

        # history_section = Frame(self)
        # window_layout.addWidget(history_section)
        # self._init_history_section()

    def _init_overview_section(self):

        section_layout = VerticalLayout(self.overview_section)

        self.title_section = Frame(self.overview_section)
        section_layout.addWidget(self.title_section)
        self._init_title_section()

        spacer = VerticalSpacer()
        section_layout.addItem(spacer)

        self.content_section = Frame(self.overview_section)
        section_layout.addWidget(self.content_section)
        self._init_content_section()

    def _init_title_section(self):

        section_layout = HorizontalLayout(self.title_section)

        # --------- greeting ------------
        greeting = Label(
            self.title_section, text="Hello", name="greeting"
        )
        section_layout.addWidget(greeting)

        spacer = HorizontalSpacer()
        section_layout.addItem(spacer)

        # --------- balance credit ------------
        credit_frame = Frame(self.title_section, name="balance")
        credit_layout = HorizontalLayout(credit_frame, space=10)
        section_layout.addWidget(credit_frame)

        balance_title = Label(
            credit_frame, text="Total Balance:", name="balance_title", align=Qt.AlignVCenter
        )
        credit_layout.addWidget(balance_title)
        
        balance_credit = Label(
            credit_frame, text="0 credits", name="balance_credit"
        )
        credit_layout.addWidget(balance_credit)

    def _init_content_section(self):

        section_layout = HorizontalLayout(self.content_section)

        self.machine_section = Frame(self.content_section,)
        section_layout.addWidget(self.machine_section)
        self._init_machine_section()

        spacer = HorizontalSpacer()
        section_layout.addWidget(spacer)

        self.credit_section = Frame(self.content_section)
        section_layout.addWidget(self.credit_section)
        self._init_credit_section()

    def _init_machine_section(self):

        section_layout = HorizontalLayout(self.machine_section)

        # --------- resource ------------

        resource_frame = Frame(self.machine_section)
        resource_layout = VerticalLayout(resource_frame, space=10)
        section_layout.addWidget(resource_frame)

        # --------- title ------------

        title = Label(resource_frame, text="Resources", name="machine_title", align=Qt.AlignLeft)
        resource_layout.addWidget(title)

        # --------- resource data ------------

        frame = Frame(resource_frame)
        frame_layout = HorizontalLayout(frame, space=7)
        resource_layout.addWidget(frame)

        self.resources_running = DashboardParamFrame(frame, dat="0", label="running")
        frame_layout.addWidget(self.resources_running)

        self.resources_dead = DashboardParamFrame(frame, dat="0", label="dead")
        frame_layout.addWidget(self.resources_dead)

        # --------- jobs ------------

        jobs_frame = Frame(self.machine_section)
        jobs_layout = VerticalLayout(jobs_frame, space=5)
        section_layout.addWidget(jobs_frame)

        # --------- title ------------
        
        title = Label(jobs_frame, text="Jobs", name="machine_title", align=Qt.AlignLeft)
        jobs_layout.addWidget(title)

        # --------- jobs data ------------

        frame = Frame(jobs_frame)
        frame_layout = HorizontalLayout(frame, space=7)
        jobs_layout.addWidget(frame)

        self.jobs_running = DashboardParamFrame(frame, dat="0", label="running")
        frame_layout.addWidget(self.jobs_running)

        self.jobs_finish = DashboardParamFrame(frame, dat="0", label="finished")
        frame_layout.addWidget(self.jobs_finish)

        self.jobs_kill = DashboardParamFrame(frame, dat="0", label="killed")
        frame_layout.addWidget(self.jobs_kill)

    def _init_credit_section(self):

        section_layout = VerticalLayout(self.credit_section)

        





