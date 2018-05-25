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


class Dashboard(MainView):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.overview = None            # section
        self.performance = None         # section
        self.resource_spec = None       # section

        self.greeting = None            # param string
        self.username = "Martin"        # param string
        self.add_dashlet = None         # button

        self._init_ui()
        self.setStyleSheet(dashboard_style)

    def _init_ui(self):
        section_layout = add_layout(self, VERTICAL, l_m=5, r_m=5, b_m=5)

        # title frame
        title_frame = QFrame(self)
        title_frame.setFixedHeight(82)
        title_layout = add_layout(title_frame, HORIZONTAL, l_m=30, r_m=30)

        now = datetime.datetime.now()

        if now.hour < 12:
            self.greeting = "Good morning,"
        elif 12 <= now.hour < 18:
            self.greeting = "Good afternoon,"
        else:
            self.greeting = "Good evening,"

        greeting = add_label(title_frame, f"{self.greeting}", name="Dashboard_greeting")
        username = add_label(title_frame, f" {self.username}", name="Dashboard_username")

        self.add_dashlet = add_button(title_frame, "Add Dashlet", name="Dashboard_add_dashlet")

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        title_layout.addWidget(greeting)
        title_layout.addWidget(username)
        title_layout.addItem(spacer)
        title_layout.addWidget(self.add_dashlet)

        # content frame
        content_frame = QFrame(self)
        content_layout = add_layout(content_frame, HORIZONTAL)

        # left frame
        left_frame = QFrame(content_frame)
        left_layout = add_layout(left_frame, VERTICAL, space=4)

        self.performance = DashboardPerformance(left_frame)
        self.resource_spec = DashboardResourceSpec(left_frame)

        left_layout.addWidget(self.performance)
        left_layout.addWidget(self.resource_spec)

        # right frame
        right_frame = QFrame(content_frame)
        right_layout = add_layout(right_frame, VERTICAL)

        self.overview = DashboardOverview(right_frame)

        right_layout.addWidget(self.overview)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        content_layout.addWidget(left_frame)
        content_layout.addItem(spacer)
        content_layout.addWidget(right_frame)

        section_layout.addWidget(title_frame)
        section_layout.addWidget(content_frame)


# pure UI unit
class DashboardOverview(QFrame):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.current_machine = 3            # input number
        self.panic_machine = 0              # input number
        self.current_resources = 7          # input number
        self.finished_resources = 3         # input number
        self.panic_resources = 1            # input number
        self.current_jobs = 6               # input number
        self.finished_jobs = 2              # input number
        self.panic_jobs = 0                 # input number

        self._init_geometry()
        self._init_ui()
        self.setStyleSheet(dashboard_style)

    def _init_geometry(self):
        self.setFixedWidth(455)

    def _init_ui(self):
        self.setObjectName("Dashboard_overview")

        section_layout = add_layout(self, VERTICAL, l_m=47, r_m=47, t_m=26, b_m=100)

        title_frame = QFrame(self)
        title_layout = add_layout(title_frame, HORIZONTAL)

        title = add_label(title_frame, "Overview", name="Dashboard_section_title")

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        title_layout.addWidget(title)
        title_layout.addItem(spacer)

        content_frame = QFrame(self)
        content_layout = add_layout(content_frame, VERTICAL, space=28)

        # current machine
        current_machine = QFrame(content_frame)
        current_machine_layout = add_layout(current_machine, HORIZONTAL)

        title = add_label(current_machine, "Current Running Machine #", name="Dashboard_section_context")
        current_machine_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        current_machine_layout.addItem(spacer)

        data = add_label(current_machine, f"{self.current_machine}", name="Dashboard_section_context")
        current_machine_layout.addWidget(data)

        # panic machine
        panic_machine = QFrame(content_frame)
        panic_machine_layout = add_layout(panic_machine, HORIZONTAL)

        title = add_label(panic_machine, "Panic Machine #", name="Dashboard_section_context")
        panic_machine_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        panic_machine_layout.addItem(spacer)

        data = add_label(panic_machine, f"{self.panic_machine}", name="Dashboard_section_context")
        panic_machine_layout.addWidget(data)

        # current resources
        current_resources = QFrame(content_frame)
        current_resources_layout = add_layout(current_resources, HORIZONTAL)

        title = add_label(current_resources, "Current Running Resources #", name="Dashboard_section_context")
        current_resources_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        current_resources_layout.addItem(spacer)

        data = add_label(current_resources, f"{self.current_resources}", name="Dashboard_section_context")
        current_resources_layout.addWidget(data)

        # finished resources
        finished_resources = QFrame(content_frame)
        finished_resources_layout = add_layout(finished_resources, HORIZONTAL)

        title = add_label(finished_resources, "Finished Resources #", name="Dashboard_section_context")
        finished_resources_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        finished_resources_layout.addItem(spacer)

        data = add_label(finished_resources, f"{self.finished_resources}", name="Dashboard_section_context")
        finished_resources_layout.addWidget(data)

        # panic resources
        panic_resources = QFrame(content_frame)
        panic_resources_layout = add_layout(panic_resources, HORIZONTAL)

        title = add_label(panic_resources, "Panic Resources #", name="Dashboard_section_context")
        panic_resources_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        panic_resources_layout.addItem(spacer)

        data = add_label(panic_resources, f"{self.panic_resources}", name="Dashboard_section_context")
        panic_resources_layout.addWidget(data)

        # current jobs
        current_jobs = QFrame(content_frame)
        current_jobs_layout = add_layout(current_jobs, HORIZONTAL)

        title = add_label(current_jobs, "Current Running Jobs #", name="Dashboard_section_context")
        current_jobs_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        current_jobs_layout.addItem(spacer)

        data = add_label(current_jobs, f"{self.current_jobs}", name="Dashboard_section_context")
        current_jobs_layout.addWidget(data)

        # finished jobs
        finished_jobs = QFrame(content_frame)
        finished_jobs_layout = add_layout(finished_jobs, HORIZONTAL)

        title = add_label(finished_jobs, "Finished Jobs #", name="Dashboard_section_context")
        finished_jobs_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        finished_jobs_layout.addItem(spacer)

        data = add_label(finished_jobs, f"{self.finished_jobs}", name="Dashboard_section_context")
        finished_jobs_layout.addWidget(data)

        # panic jobs
        panic_jobs = QFrame(content_frame)
        panic_jobs_layout = add_layout(panic_jobs, HORIZONTAL)

        title = add_label(panic_jobs, "Panic Jobs #", name="Dashboard_section_context")
        panic_jobs_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        panic_jobs_layout.addItem(spacer)

        data = add_label(panic_jobs, f"{self.panic_jobs}", name="Dashboard_section_context")
        panic_jobs_layout.addWidget(data)

        content_layout.addWidget(current_machine)
        content_layout.addWidget(panic_machine)
        content_layout.addWidget(current_resources)
        content_layout.addWidget(finished_resources)
        content_layout.addWidget(panic_resources)
        content_layout.addWidget(current_jobs)
        content_layout.addWidget(finished_jobs)
        content_layout.addWidget(panic_jobs)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        section_layout.addWidget(title_frame)
        section_layout.addItem(spacer)
        section_layout.addWidget(content_frame)


# pure UI unit
class DashboardPerformance(QFrame):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.profit = 30                    # input number
        self.cost = 15                      # input number

        self._init_geometry()
        self._init_ui()
        self.setStyleSheet(dashboard_style)

    def _init_geometry(self):
        self.setFixedSize(455, 278)

    def _init_ui(self):
        self.setObjectName("Dashboard_performance")

        section_layout = add_layout(self, VERTICAL, l_m=47, r_m=47, t_m=26, b_m=26)

        title_frame = QFrame(self)
        title_layout = add_layout(title_frame, HORIZONTAL)

        title = add_label(title_frame, "Performance", name="Dashboard_section_title")

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        title_layout.addWidget(title)
        title_layout.addItem(spacer)

        content_frame = QFrame(self)
        content_layout = add_layout(content_frame, VERTICAL, align=Qt.AlignHCenter)

        # parameter
        width = 150
        height = 180
        offset = 6

        # pen
        pen_01 = QPen(QColor(COLOR_04), offset)
        pen_02 = QPen(QColor(COLOR_05), offset)

        # brush
        brush_01 = QBrush(QColor(COLOR_04))
        brush_02 = QBrush(QColor(COLOR_05))

        # view & scene
        view, scene = add_graph_scene(content_frame, width=width, height=height, name="Dashboard_view")

        # circle geometry
        rect = QRectF(-width/2, -height/2, width-offset*2, width-offset*2)

        angle = int(360 * self.profit / (self.profit + self.cost))

        # profit
        path = QPainterPath()
        path.arcMoveTo(rect, 0)
        path.arcTo(rect, 0, angle)

        item = QGraphicsPathItem(path)
        item.setPen(pen_01)

        scene.addItem(item)

        # cost
        path = QPainterPath()
        path.arcMoveTo(rect, angle)

        path.arcTo(rect, angle, 360 - angle)

        item = QGraphicsPathItem(path)
        item.setPen(pen_02)

        scene.addItem(item)

        # profit legend

        item = QGraphicsEllipseItem(-65, 65, 14, 14)
        item.setPen(QPen(Qt.NoPen))
        item.setBrush(brush_01)

        scene.addItem(item)

        item = QGraphicsTextItem("Profit")
        item.setPos(-45, 61)

        font = QFont("Helvetica Neue", 12, QFont.Light)
        item.setFont(font)

        scene.addItem(item)

        # cost legend

        item = QGraphicsEllipseItem(5, 65, 14, 14)
        item.setPen(QPen(Qt.NoPen))
        item.setBrush(brush_02)

        scene.addItem(item)

        item = QGraphicsTextItem("Cost")
        item.setPos(25, 61)

        font = QFont("Helvetica Neue", 12, QFont.Light)
        item.setFont(font)

        scene.addItem(item)

        # title
        item = QGraphicsTextItem("Net Credit")
        item.setPos(-37, -50)

        font = QFont("Helvetica Neue", 13, QFont.Thin)
        item.setFont(font)

        scene.addItem(item)

        # net profit
        net = self.profit - self.cost

        if net > 0:
            net = "+ " + str(net) + " / DAY"
        else:
            net = str(net) + " / DAY"

        item = QGraphicsTextItem(net)
        item.setPos(-57, -25)

        font = QFont("Helvetica Neue", 20, 7)
        item.setFont(font)

        scene.addItem(item)

        content_layout.addWidget(view)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        section_layout.addWidget(title_frame)
        section_layout.addItem(spacer)
        section_layout.addWidget(content_frame)


# pure UI unit
class DashboardResourceSpec(QFrame):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        self.resource_num = None            # param number
        self.resource_name = None           # list of resource name
        self.resource_list = None           # list of list resource data

        self._init_ui()
        self.setStyleSheet(dashboard_style)

    def _init_ui(self):
        self.setObjectName("Dashboard_resources_spec")

        section_layout = add_layout(self, VERTICAL, l_m=47, r_m=47, t_m=26, b_m=26)

        title_frame = QFrame(self)
        title_layout = add_layout(title_frame, HORIZONTAL)

        title = add_label(title_frame, "Resources Spec.", name="Dashboard_section_title")

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        title_layout.addWidget(title)
        title_layout.addItem(spacer)

        content_frame = QFrame(self)
        content_layout = add_layout(content_frame, VERTICAL, align=Qt.AlignHCenter)

        width = 340
        height = 187

        view, scene = add_graph_scene(content_frame, width=width, height=height, name="Dashboard_view1")
        content_layout.addWidget(view)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        section_layout.addWidget(title_frame)
        section_layout.addItem(spacer)
        section_layout.addWidget(content_frame)
