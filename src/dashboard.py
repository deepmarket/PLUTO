"""
    The following items can be interacted:

    class DashboardOverview:

        self.current_machine = 3            # input number
        self.panic_machine = 0              # input number
        self.current_resources = 7          # input number
        self.finished_resources = 3         # input number
        self.panic_resources = 1            # input number
        self.current_jobs = 6               # input number
        self.finished_jobs = 2              # input number
        self.panic_jobs = 0                 # input number

    class DashboardPerformance:

        self.profit = 30                    # input number
        self.cost = 15                      # input number

    class DashboardResourceSpec:

        self.resource_num = None            # param number
        self.resource_name = None           # list of resource name
        self.resource_list = None           # list of list resource data
"""

from src.mainview import MainView
from src.uix.util import *
from src.api import Api


class Dashboard(MainView):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.overview = None                # section
        self.profit_history_frame = None    # section
        self.cost_history_frame = None      # section

        self.profit_history = None          # table widget
        self.cost_history = None            # table widget

        self.greeting = add_greeting()      # param string
        self.username = ""                  # param string
        self.total_balance = 15             # param number
        self.estimated_profit = 30          # param number
        self.estimated_cost = 20            # param number
        self.running_machine = 5            # param number
        self.panic_machine = 2              # param number
        self.finished_job = 3               # param number
        self.running_job = 2                # param number
        self.panic_job = 0                  # param number

        # account_api = Api("/account")
        # status, res = account_api.get()
        #
        # if status == 200:
        #     # Insert comma here so we can default to nameless greeting if api fails.
        #     self.username = f", {res['customer']['firstname'].capitalize()}"

        # TODO: request "Total Balance", "Estimated profit", "Estimated cost" "machine status"from api also

        # for testing
        self.username = "Martin"

        self._init_ui()
        self.setStyleSheet(dashboard_style)

    def _init_ui(self):
        widget_layout = add_layout(self, VERTICAL, t_m=5, b_m=5, space=5)

        self._init_overview()

        history_frame = QFrame(self)
        history_layout = add_layout(history_frame, HORIZONTAL, space=2)

        self._init_profit_history()
        self._init_cost_history()
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        history_layout.addWidget(self.profit_history_frame)
        history_layout.addItem(spacer)
        history_layout.addWidget(self.cost_history_frame)

        widget_layout.addWidget(self.overview)
        widget_layout.addWidget(history_frame)

    def _init_overview(self):
        self.overview = QFrame(self)
        self.overview.setFixedHeight(300)
        self.overview.setObjectName("Dashboard_overview")

        section_layout = add_layout(self.overview, HORIZONTAL, t_m=45, b_m=67, l_m=40, r_m=50)

        # --------- begin left_frame ------------

        left_frame = QFrame(self.overview)
        left_layout = add_layout(left_frame, VERTICAL, space=2)

        # --------- title_frame ------------

        title_frame = QFrame(left_frame)
        title_layout = add_layout(title_frame, HORIZONTAL, space=10)

        greeting = add_label(left_frame, f"{self.greeting}", name="Dashboard_greeting")
        username = add_label(left_frame, f"{self.username}", name="Dashboard_username")
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        title_layout.addWidget(greeting)
        title_layout.addWidget(username)
        title_layout.addItem(spacer)
        left_layout.addWidget(title_frame)

        # --------- spacer ------------

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        left_layout.addItem(spacer)

        # --------- begin description, a line ------------

        line_frame = QFrame(left_frame)
        line_layout = add_layout(line_frame, HORIZONTAL)

        segment = add_label(line_frame, "Here is some detail about resources / jobs:", name="Dashboard_description")
        line_layout.addWidget(segment)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        # --------- a line ------------

        left_layout.addWidget(line_frame)

        line_frame = QFrame(left_frame)
        line_layout = add_layout(line_frame, HORIZONTAL)

        segment = add_label(line_frame, "Within your last logout,", name="Dashboard_description")
        line_layout.addWidget(segment)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        left_layout.addWidget(line_frame)

        # --------- a line ------------

        line_frame = QFrame(left_frame)
        line_layout = add_layout(line_frame, HORIZONTAL)

        segment = add_label(line_frame, "There are ", name="Dashboard_description")
        line_layout.addWidget(segment)

        segment = add_label(line_frame, f"{self.running_machine}", name="Dashboard_highlight_description")
        line_layout.addWidget(segment)

        segment = add_label(line_frame, " resources are running, and ", name="Dashboard_description")
        line_layout.addWidget(segment)

        segment = add_label(line_frame, f"{self.panic_machine}", name="Dashboard_highlight_description")
        line_layout.addWidget(segment)

        segment = add_label(line_frame, " are panic.", name="Dashboard_description")
        line_layout.addWidget(segment)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        left_layout.addWidget(line_frame)

        # --------- a line ------------

        line_frame = QFrame(left_frame)
        line_layout = add_layout(line_frame, HORIZONTAL)

        segment = add_label(line_frame, "There are ", name="Dashboard_description")
        line_layout.addWidget(segment)

        segment = add_label(line_frame, f"{self.finished_job}", name="Dashboard_highlight_description")
        line_layout.addWidget(segment)

        segment = add_label(line_frame, " jobs are finished, ", name="Dashboard_description")
        line_layout.addWidget(segment)

        segment = add_label(line_frame, f"{self.running_job}", name="Dashboard_highlight_description")
        line_layout.addWidget(segment)

        segment = add_label(line_frame, " are still running, and ", name="Dashboard_description")
        line_layout.addWidget(segment)

        segment = add_label(line_frame, f"{self.panic_job}", name="Dashboard_highlight_description")
        line_layout.addWidget(segment)

        segment = add_label(line_frame, " jobs are panic.", name="Dashboard_description")
        line_layout.addWidget(segment)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        left_layout.addWidget(line_frame)

        # --------- end left_frame, begin right_frame ------------

        right_frame = QFrame(self.overview)
        right_layout = add_layout(right_frame, VERTICAL, space=17)

        # --------- balance_frame ------------

        balance_frame = QFrame(right_frame)
        balance_layout = add_layout(balance_frame, HORIZONTAL, space=25)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        balance_layout.addItem(spacer)

        balance_title = add_label(balance_frame, "Total Balance:", name="Dashboard_balance_title",
                                  align=Qt.AlignVCenter)
        balance_layout.addWidget(balance_title)

        balance = add_label(balance_frame, f"{self.total_balance} credits", name="Dashboard_balance")
        balance_layout.addWidget(balance)

        right_layout.addWidget(balance_frame)

        # --------- spacer ------------

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        right_layout.addItem(spacer)

        # --------- estimated item ------------

        estimated_frame = QFrame(right_frame)
        estimated_layout = add_layout(estimated_frame, HORIZONTAL, space=60)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        estimated_layout.addItem(spacer)

        estimated_title_frame = QFrame(estimated_frame)
        estimated_title_layout = add_layout(estimated_title_frame, VERTICAL)

        estimated_title = add_label(estimated_title_frame, "Estimated profit:", name="Dashboard_estimated_title")
        estimated_title_layout.addWidget(estimated_title)

        estimated_subtitle = add_label(estimated_title_frame, "(within next 24 hrs)",
                                       name="Dashboard_estimated_title_small", align=Qt.AlignLeft)
        estimated_title_layout.addWidget(estimated_subtitle)

        estimated_layout.addWidget(estimated_title_frame)

        estimated_value = add_label(estimated_frame, f"+ {self.estimated_profit} credits",
                                    name="Dashboard_estimated", align=Qt.AlignVCenter)
        estimated_layout.addWidget(estimated_value)

        right_layout.addWidget(estimated_frame)

        # --------- estimated item ------------

        estimated_frame = QFrame(right_frame)
        estimated_layout = add_layout(estimated_frame, HORIZONTAL, space=60)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        estimated_layout.addItem(spacer)

        estimated_title_frame = QFrame(estimated_frame)
        estimated_title_layout = add_layout(estimated_title_frame, VERTICAL)

        estimated_title = add_label(estimated_title_frame, "Estimated cost:", name="Dashboard_estimated_title")
        estimated_title_layout.addWidget(estimated_title)

        estimated_subtitle = add_label(estimated_title_frame, "(within next 24 hrs)",
                                       name="Dashboard_estimated_title_small", align=Qt.AlignLeft)
        estimated_title_layout.addWidget(estimated_subtitle)

        estimated_layout.addWidget(estimated_title_frame)

        estimated_value = add_label(estimated_frame, f"- {self.estimated_cost} credits",
                                    name="Dashboard_estimated", align=Qt.AlignVCenter)
        estimated_layout.addWidget(estimated_value)

        right_layout.addWidget(estimated_frame)

        # --------- end right_frame ------------

        # spacer
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        section_layout.addWidget(left_frame)
        section_layout.addItem(spacer)
        section_layout.addWidget(right_frame)

    def _init_profit_history(self):
        self.profit_history_frame = QFrame(self)
        self.profit_history_frame.setFixedWidth(461)
        self.profit_history_frame.setObjectName("Dashboard_history")

        section_layout = add_layout(self.profit_history_frame, VERTICAL, space=14, t_m=20, b_m=20, l_m=22, r_m=15)

        title = add_label(self.profit_history_frame, "Past 30 days Profit History", name="Dashboard_history_title")
        section_layout.addWidget(title)

        self.profit_history = QTableWidget(self.profit_history_frame)
        self.profit_history.setObjectName("Dashboard_history_table")
        section_layout.addWidget(self.profit_history)

        column_width = [130, 180, 1]

        self.profit_history.setColumnCount(len(column_width))
        for i in range(len(column_width)):
            self.profit_history.setColumnWidth(i, column_width[i])
        self.profit_history.horizontalHeader().setStretchLastSection(True)

        # table property
        # hide horizontal, vertical header
        # hide horizontal scroll bar
        # disable edited
        # not allow selected row
        # alternating color
        # hide grid line
        # set default row height
        self.profit_history.horizontalHeader().hide()
        self.profit_history.verticalHeader().hide()
        self.profit_history.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.profit_history.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.profit_history.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.profit_history.setSelectionMode(QAbstractItemView.NoSelection)
        self.profit_history.setAlternatingRowColors(True)
        self.profit_history.setShowGrid(False)

        self.profit_history.verticalHeader().setDefaultSectionSize(31)

        column = self.profit_history.columnCount()
        for r in range(9):
            self.profit_history.insertRow(r)
            for c in range(column):
                self.profit_history.setItem(r, c, QTableWidgetItem(""))

        row = self.profit_history.rowCount()
        if row > 9:
            self.profit_history.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    def _init_cost_history(self):
        self.cost_history_frame = QFrame(self)
        self.cost_history_frame.setFixedWidth(461)
        self.cost_history_frame.setObjectName("Dashboard_history")

        section_layout = add_layout(self.cost_history_frame, VERTICAL, space=14, t_m=20, b_m=20, l_m=15, r_m=22)

        title = add_label(self.cost_history_frame, "Past 30 days Cost History", name="Dashboard_history_title")
        section_layout.addWidget(title)

        self.cost_history = QTableWidget(self.profit_history_frame)
        self.cost_history.setObjectName("Dashboard_history_table")
        section_layout.addWidget(self.cost_history)

        column_width = [130, 180, 1]

        self.cost_history.setColumnCount(len(column_width))
        for i in range(len(column_width)):
            self.cost_history.setColumnWidth(i, column_width[i])
        self.cost_history.horizontalHeader().setStretchLastSection(True)

        # table property
        # hide horizontal, vertical header
        # hide horizontal scroll bar
        # disable edited
        # not allow selected row
        # alternating color
        # hide grid line
        # set default row height
        self.cost_history.horizontalHeader().hide()
        self.cost_history.verticalHeader().hide()
        self.cost_history.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cost_history.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cost_history.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cost_history.setSelectionMode(QAbstractItemView.NoSelection)
        self.cost_history.setAlternatingRowColors(True)
        self.cost_history.setShowGrid(False)
        self.cost_history.verticalHeader().setDefaultSectionSize(31)

        column = self.cost_history.columnCount()
        for r in range(9):
            self.cost_history.insertRow(r)
            for c in range(column):
                self.cost_history.setItem(r, c, QTableWidgetItem(""))

        row = self.cost_history.rowCount()
        if row > 9:
            self.cost_history.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    # self-updated function by calling timer in main
    # can be used later on
    def update(self):
        pass

