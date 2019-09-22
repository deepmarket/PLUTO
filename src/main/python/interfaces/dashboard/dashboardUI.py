from collections import OrderedDict
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtCore import Qt

from ..widgets import (
    EstimateFrame,
    Frame,
    HorizontalLayout,
    HorizontalSpacer,
    Label,
    ParamFrame,
    SectionTitleFrame,
    Table,
    VerticalLayout,
    VerticalSpacer,
    ViewButton,
)
from ..config import DASHBOARD_MAX_ROW


class DashboardUI(Frame):

    overview_section: Frame = None

    title_section: Frame = None
    greeting: Label = None
    balance_credit: Label = None

    content_section: Frame = None

    machine_section: Frame = None
    resources_running: ParamFrame = None
    resources_dead: ParamFrame = None

    jobs_section: Frame = None
    jobs_running: ParamFrame = None
    jobs_finish: ParamFrame = None
    jobs_kill: ParamFrame = None

    credit_section: Frame = None
    estimate_profit: EstimateFrame = None
    estimate_cost: EstimateFrame = None

    history_section: Frame = None

    profit_section: Frame = None
    profit_table: Table = None

    cost_section: Frame = None
    cost_table: Table = None

    def __init__(self, cxt: ApplicationContext, *args, **kwargs):
        super(DashboardUI, self).__init__(*args, name="dashboard", **kwargs)

        self.cxt = cxt

        # self.get_dashboard_data()
        self._init_ui()
        self.setStyleSheet(self.cxt.dashboard_style)

    def _init_ui(self):

        window_layout = VerticalLayout(self, space=1)

        self.overview_section = Frame(self, name="overview_section")
        window_layout.addWidget(self.overview_section)
        self._init_overview_section()

        self.history_section = Frame(self, name="history_section")
        window_layout.addWidget(self.history_section)
        self._init_history_section()

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
        self.greeting = Label(self.title_section, name="greeting")
        section_layout.addWidget(self.greeting)

        spacer = HorizontalSpacer()
        section_layout.addItem(spacer)

        # --------- balance credit ------------
        credit_frame = Frame(self.title_section, name="balance")
        credit_layout = HorizontalLayout(credit_frame, space=10)
        section_layout.addWidget(credit_frame)

        balance_title = Label(
            credit_frame,
            text="Total Balance:",
            name="balance_title",
            align=Qt.AlignVCenter,
        )
        credit_layout.addWidget(balance_title)

        self.balance_credit = Label(credit_frame, name="balance_credit")
        credit_layout.addWidget(self.balance_credit)

    def _init_content_section(self):

        section_layout = HorizontalLayout(self.content_section)

        self.machine_section = Frame(self.content_section)
        section_layout.addWidget(self.machine_section)
        self._init_machine_section()

        spacer = HorizontalSpacer()
        section_layout.addItem(spacer)

        self.credit_section = Frame(self.content_section)
        section_layout.addWidget(self.credit_section)
        self._init_credit_section()

    def _init_machine_section(self):

        section_layout = HorizontalLayout(self.machine_section, space=50)

        # --------- resource ------------

        resource_frame = Frame(self.machine_section)
        resource_layout = VerticalLayout(resource_frame, space=5)
        section_layout.addWidget(resource_frame)

        spacer = VerticalSpacer()
        resource_layout.addItem(spacer)

        # --------- title ------------

        title = Label(
            resource_frame, text="Resources", name="machine_title", align=Qt.AlignLeft
        )
        resource_layout.addWidget(title)

        # --------- resource data ------------

        frame = Frame(resource_frame)
        frame_layout = HorizontalLayout(frame, space=20)
        resource_layout.addWidget(frame)

        self.resources_running = ParamFrame(frame, label="Running")
        frame_layout.addWidget(self.resources_running)

        self.resources_dead = ParamFrame(frame, label="Dead")
        frame_layout.addWidget(self.resources_dead)

        # --------- jobs ------------

        jobs_frame = Frame(self.machine_section)
        jobs_layout = VerticalLayout(jobs_frame, space=5)
        section_layout.addWidget(jobs_frame)

        spacer = VerticalSpacer()
        jobs_layout.addItem(spacer)

        # --------- title ------------

        title = Label(jobs_frame, text="Jobs", name="machine_title", align=Qt.AlignLeft)
        jobs_layout.addWidget(title)

        # --------- jobs data ------------

        frame = Frame(jobs_frame)
        frame_layout = HorizontalLayout(frame, space=20)
        jobs_layout.addWidget(frame)

        self.jobs_running = ParamFrame(frame, label="Running")
        frame_layout.addWidget(self.jobs_running)

        self.jobs_finish = ParamFrame(frame, label="Finished")
        frame_layout.addWidget(self.jobs_finish)

        self.jobs_kill = ParamFrame(frame, label="Killed")
        frame_layout.addWidget(self.jobs_kill)

    def _init_credit_section(self):

        section_layout = VerticalLayout(self.credit_section, space=10)

        self.estimate_profit = EstimateFrame(
            self.credit_section, title="Estimated profit:", in_out="+", credit="0"
        )
        section_layout.addWidget(self.estimate_profit)

        self.estimate_cost = EstimateFrame(
            self.credit_section, title="Estimated cost:", in_out="-", credit="0"
        )
        section_layout.addWidget(self.estimate_cost)

    def _init_history_section(self):

        section_layout = HorizontalLayout(self.history_section, space=1)

        self.profit_section = Frame(self.history_section)
        section_layout.addWidget(self.profit_section)
        self._init_profit_section()

        self.cost_section = Frame(self.history_section)
        section_layout.addWidget(self.cost_section)
        self._init_cost_section()

    def _init_profit_section(self):

        section_layout = VerticalLayout(self.profit_section, space=15)

        # --------- title ------------

        title = Label(
            self.profit_section,
            text="Past 30 days Profit History",
            name="history_title",
        )
        section_layout.addWidget(title)

        # --------- table ------------

        header = OrderedDict()

        header["ID"] = 130
        header["Time"] = 180
        header["Credit"] = 1

        self.profit_table = Table(
            self.profit_section,
            DASHBOARD_MAX_ROW,
            header,
            name="table_content_section",
            row_height=30,
        )
        section_layout.addWidget(self.profit_table)

    def _init_cost_section(self):

        section_layout = VerticalLayout(self.cost_section, space=15)

        # --------- title ------------

        title = Label(
            self.cost_section, text="Past 30 days Cost History", name="history_title"
        )
        section_layout.addWidget(title)

        # --------- table ------------

        header = OrderedDict()

        header["ID"] = 130
        header["Time"] = 180
        header["Credit"] = 1

        self.cost_table = Table(
            self.cost_section,
            DASHBOARD_MAX_ROW,
            header,
            name="table_content_section",
            row_height=30,
        )
        section_layout.addWidget(self.cost_table)
