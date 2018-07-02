"""
    The following items can be interacted:

    class JobsWorkspace:

        self.add_jobs = None            # button
        self.workers = None             # input string
        self.cores = None               # input number
        self.memory = None              # input number
        self.source_file = None         # input string
        self.input_file = None          # input string

        self.submit_button = None       # button
        self.refresh_button = None      # button
        self.hint = None                # button

    class JobsList:

        self.table = None               # section
        self.current_row = 0            # param number
"""

from src.mainview import MainView
from src.uix.util import *
from src.uix.config import *
from src.uix.popup import Question
from src.api import Api


class Jobs(MainView):

    def __init__(self, *args, **kwargs):
        super(Jobs, self).__init__(*args, **kwargs)

        # Constant price
        self.price_per_hour = 0.005

        # variable
        self.workspace = None                   # widget
        self.list = None                        # widget

        self.workspace_button = None            # button
        self.list_button = None                 # button
        self.stack = None                       # layout

        self._init_ui()
        self.setStyleSheet(page_style)

        self.on_workspace_clicked()

    def _init_ui(self):
        section_layout = add_layout(self, VERTICAL, b_m=8)

        button_frame = QFrame(self)
        section_layout.addWidget(button_frame)
        button_frame.setFixedHeight(35)
        button_layout = add_layout(button_frame, HORIZONTAL, l_m=40, r_m=40, space=24)

        self.workspace_button = add_button(button_frame, "Add Job", stylesheet=page_menu_button_active)
        self.list_button = add_button(button_frame, "Job Lists", stylesheet=page_menu_button)
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        button_layout.addWidget(self.workspace_button)
        button_layout.addWidget(self.list_button)
        button_layout.addItem(spacer)

        window_frame = QFrame(self)
        section_layout.addWidget(window_frame)
        self.stack = add_layout(window_frame, STACK)

        self.workspace = JobWorkspace()
        self.list = JobList()

        self.stack.addWidget(self.workspace)
        self.stack.addWidget(self.list)

        self.workspace_button.clicked.connect(self.on_workspace_clicked)
        self.list_button.clicked.connect(self.on_list_clicked)

    def on_workspace_clicked(self):
        # set button to enable stylesheet
        self.workspace_button.setStyleSheet(page_menu_button_active)
        self.list_button.setStyleSheet(page_menu_button)
        self.stack.setCurrentIndex(0)

        self.update_workspace()

    def on_list_clicked(self):
        # set button to enable stylesheet
        self.workspace_button.setStyleSheet(page_menu_button)
        self.list_button.setStyleSheet(page_menu_button_active)
        self.stack.setCurrentIndex(1)

    def update_workspace(self):
        # update scheme
        frames = [self.workspace.scheme_01_frame,
                  self.workspace.scheme_02_frame,
                  self.workspace.scheme_03_frame,
                  self.workspace.scheme_04_frame]

        for frame in frames:
            # find all QLabel children within the frame
            labels = frame.findChildren(QLabel)

            # exclude the first label, which is the time label
            labels.pop(0)

            for label in labels:
                label.setText(f"{self.price_per_hour} Credit/Hr")

        # TODO: load dat here
        # format: [cpu, gpu, memory, space], type: int
        dat = [12, 2, 24, 40]

        # update available resources
        labels = [self.workspace.available_cpu,
                  self.workspace.available_gpu,
                  self.workspace.available_memory,
                  self.workspace.available_disk]

        text = [f"CPU #: {dat[0]}", f"GPU #: {dat[1]}", f"Memory: {dat[2]} GB", f"Disk Space: {dat[3]} GB"]

        for i in range(len(dat)):
            labels[i].setText(text[i])


class JobWorkspace(QFrame):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.workers = None                     # input string
        self.cores = None                       # input number
        self.memory = None                      # input number
        self.source_file = None                 # input string
        self.input_file = None                  # input string

        self.submission_hint = None             # param string

        self.available_cpu = None               # param string
        self.available_gpu = None               # param string
        self.available_memory = None            # param string
        self.available_disk = None              # param string

        self.scheme_01_frame = None             # frame
        self.scheme_02_frame = None             # frame
        self.scheme_03_frame = None             # frame
        self.scheme_04_frame = None             # frame

        self.select_scheme = 1                  # flag

        self.submit_button = None               # button

        self._init_ui()
        self.setStyleSheet(page_style)

    def _init_ui(self):

        self.setObjectName("Page_sub_page")
        window_layout = add_layout(self, VERTICAL, t_m=40, l_m=45, r_m=45, space=30)

        # --------- begin pricing_scheme: line_frame, sub_section_frame ------------

        section_frame = QFrame(self)
        window_layout.addWidget(section_frame)
        section_layout = add_layout(section_frame, VERTICAL, space=18)

        # --------- line_frame: title, spacer ------------

        line_frame = QFrame(section_frame)
        section_layout.addWidget(line_frame)
        line_layout = add_layout(line_frame, HORIZONTAL)

        title = add_label(line_frame, "Pricing Scheme", name="Page_section_title", align=Qt.AlignVCenter)
        line_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        # --------- begin sub_section: left_section, right_section ------------

        sub_section_frame = QFrame(section_frame)
        sub_section_frame.setFixedHeight(211)
        section_layout.addWidget(sub_section_frame)
        sub_section_layout = add_layout(sub_section_frame, HORIZONTAL)

        # --------- left_section: scheme_title, four scheme choice frame, spacer ------------

        left_frame = QFrame(sub_section_frame)
        left_frame.setObjectName("Page_scheme")
        sub_section_layout.addWidget(left_frame)
        left_layout = add_layout(left_frame, HORIZONTAL, l_m=28, t_m=12, b_m=12, space=10)

        # --------- title_frame ------------

        title_frame = QFrame(left_frame)
        left_layout.addWidget(title_frame)
        title_layout = add_layout(title_frame, VERTICAL, t_m=31, b_m=32, r_m=13, space=16)

        title = add_label(title_frame, "Time", stylesheet=Page_scheme_label_disable, align=Qt.AlignRight)
        title_layout.addWidget(title)

        title = add_label(title_frame, "CPU:", stylesheet=Page_scheme_label_disable, align=Qt.AlignRight)
        title_layout.addWidget(title)

        title = add_label(title_frame, "GPU:", stylesheet=Page_scheme_label_disable, align=Qt.AlignRight)
        title_layout.addWidget(title)

        title = add_label(title_frame, "Memory:", stylesheet=Page_scheme_label_disable, align=Qt.AlignRight)
        title_layout.addWidget(title)

        title = add_label(title_frame, "Disk Space:", stylesheet=Page_scheme_label_disable, align=Qt.AlignRight)
        title_layout.addWidget(title)

        # --------- scheme_01_frame ------------

        self.scheme_01_frame = QFrame(left_frame)
        self.scheme_01_frame.setFixedWidth(124)
        self.scheme_01_frame.setStyleSheet(Page_scheme_box)
        left_layout.addWidget(self.scheme_01_frame)
        scheme_layout = add_layout(self.scheme_01_frame, VERTICAL, t_m=31, b_m=32, space=16)

        label = add_label(self.scheme_01_frame, "12:00 AM - 5:59 AM",
                          stylesheet=Page_scheme_label, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        label = add_label(self.scheme_01_frame, "0 Credit/Hr",
                          stylesheet=Page_scheme_label, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        label = add_label(self.scheme_01_frame, "0 Credit/Hr",
                          stylesheet=Page_scheme_label, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        label = add_label(self.scheme_01_frame, "0 Credit/Hr",
                          stylesheet=Page_scheme_label, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        label = add_label(self.scheme_01_frame, "0 Credit/Hr",
                          stylesheet=Page_scheme_label, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        self.scheme_01_frame.mousePressEvent = self.enable_scheme_01_frame

        # --------- scheme_02_frame ------------

        self.scheme_02_frame = QFrame(left_frame)
        self.scheme_02_frame.setFixedWidth(124)
        self.scheme_02_frame.setStyleSheet(Page_scheme_box_disable)
        left_layout.addWidget(self.scheme_02_frame)
        scheme_layout = add_layout(self.scheme_02_frame, VERTICAL, t_m=31, b_m=32, space=16)

        label = add_label(self.scheme_02_frame, "6:00 AM - 11:59 PM",
                          stylesheet=Page_scheme_label_disable, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        label = add_label(self.scheme_02_frame, "0 Credit/Hr",
                          stylesheet=Page_scheme_label_disable, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        label = add_label(self.scheme_02_frame, "0 Credit/Hr",
                          stylesheet=Page_scheme_label_disable, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        label = add_label(self.scheme_02_frame, "0 Credit/Hr",
                          stylesheet=Page_scheme_label_disable, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        label = add_label(self.scheme_02_frame, "0 Credit/Hr",
                          stylesheet=Page_scheme_label_disable, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        self.scheme_02_frame.mousePressEvent = self.enable_scheme_02_frame

        # --------- scheme_03_frame ------------

        self.scheme_03_frame = QFrame(left_frame)
        self.scheme_03_frame.setFixedWidth(124)
        self.scheme_03_frame.setStyleSheet(Page_scheme_box_disable)
        left_layout.addWidget(self.scheme_03_frame)
        scheme_layout = add_layout(self.scheme_03_frame, VERTICAL, t_m=31, b_m=32, space=16)

        label = add_label(self.scheme_03_frame, "12:00 PM - 5: 59 PM",
                          stylesheet=Page_scheme_label_disable, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        label = add_label(self.scheme_03_frame, "0 Credit/Hr",
                          stylesheet=Page_scheme_label_disable, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        label = add_label(self.scheme_03_frame, "0 Credit/Hr",
                          stylesheet=Page_scheme_label_disable, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        label = add_label(self.scheme_03_frame, "0 Credit/Hr",
                          stylesheet=Page_scheme_label_disable, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        label = add_label(self.scheme_03_frame, "0 Credit/Hr",
                          stylesheet=Page_scheme_label_disable, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        self.scheme_03_frame.mousePressEvent = self.enable_scheme_03_frame

        # --------- scheme_04_frame ------------

        self.scheme_04_frame = QFrame(left_frame)
        self.scheme_04_frame.setFixedWidth(124)
        self.scheme_04_frame.setStyleSheet(Page_scheme_box_disable)
        left_layout.addWidget(self.scheme_04_frame)
        scheme_layout = add_layout(self.scheme_04_frame, VERTICAL, t_m=31, b_m=32, space=16)

        label = add_label(self.scheme_04_frame, "6:00 PM - 11: 59 PM",
                          stylesheet=Page_scheme_label_disable, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        label = add_label(self.scheme_04_frame, "0 Credit/Hr",
                          stylesheet=Page_scheme_label_disable, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        label = add_label(self.scheme_04_frame, "0 Credit/Hr",
                          stylesheet=Page_scheme_label_disable, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        label = add_label(self.scheme_04_frame, "0 Credit/Hr",
                          stylesheet=Page_scheme_label_disable, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        label = add_label(self.scheme_04_frame, "0 Credit/Hr",
                          stylesheet=Page_scheme_label_disable, align=Qt.AlignHCenter)
        scheme_layout.addWidget(label)

        self.scheme_04_frame.mousePressEvent = self.enable_scheme_04_frame

        # --------- spacer ------------

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        left_layout.addItem(spacer)

        # --------- right_section: title, available cpu, gpu, memory, disk_space ------------

        right_frame = QFrame(sub_section_frame)
        right_frame.setFixedWidth(170)
        right_frame.setObjectName("Page_available_resources")
        sub_section_layout.addWidget(right_frame)
        right_layout = add_layout(right_frame, VERTICAL, t_m=37, b_m=40)

        title = add_label(right_frame, "Available Resources", name="Page_available_title", align=Qt.AlignCenter)
        title.setFixedHeight(13)
        right_layout.addWidget(title)

        spacer = QSpacerItem(0, 17, QSizePolicy.Minimum, QSizePolicy.Fixed)
        right_layout.addItem(spacer)

        # --------- line_frame: cpu, gpu, memory, disk_space ------------

        line_frame = QFrame(right_frame)
        right_layout.addWidget(line_frame)
        line_layout = add_layout(line_frame, VERTICAL, l_m=30, r_m=30, space=16)

        self.available_cpu = add_label(line_frame, "CPU #: 0", name="Page_available_label")
        line_layout.addWidget(self.available_cpu)

        self.available_gpu = add_label(line_frame, "GPU #: 0", name="Page_available_label")
        line_layout.addWidget(self.available_gpu)

        self.available_memory = add_label(line_frame, "Memory: 0 GB", name="Page_available_label")
        line_layout.addWidget(self.available_memory)

        self.available_disk = add_label(line_frame, "Disk Space: 0 GB", name="Page_available_label")
        line_layout.addWidget(self.available_disk)

        # --------- begin job_submission ------------

        section_frame = QFrame(self)
        window_layout.addWidget(section_frame)
        section_layout = add_layout(section_frame, VERTICAL, space=18)

        # --------- line_frame: title, spacer ------------

        line_frame = QFrame(section_frame)
        section_layout.addWidget(line_frame)
        line_layout = add_layout(line_frame, HORIZONTAL)

        title = add_label(line_frame, "Job Submission", name="Page_section_title", align=Qt.AlignVCenter)
        line_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        # --------- begin sub_section ------------

        sub_section_frame = QFrame(section_frame)
        sub_section_frame.setFixedHeight(234)
        sub_section_frame.setObjectName("Page_job_submission")
        section_layout.addWidget(sub_section_frame)
        section_layout = add_layout(sub_section_frame, VERTICAL, t_m=25, b_m=25, l_m=30, r_m=30, space=22)

        # --------- line_frame: workers, cores, memory ------------

        line_frame = QFrame(section_frame)
        section_layout.addWidget(line_frame)
        line_layout = add_layout(line_frame, HORIZONTAL)

        box, self.workers = add_page_input_box(line_frame, "Workers #:", 70, 20, stylesheet=Page_input_input)
        line_layout.addWidget(box)

        box, self.cores = add_page_input_box(line_frame, "Cores #:", 70, 20, stylesheet=Page_input_input)
        line_layout.addWidget(box)

        box, self.memory = add_page_input_box(line_frame, "Memory:", 70, 20, stylesheet=Page_input_input)
        line_layout.addWidget(box)

        # --------- source_file and input_file ------------

        box, self.source_file = add_page_input_box(line_frame, "Source file:", 70, 20,
                                                   stylesheet=Page_input_input, fix_width=False)
        section_layout.addWidget(box)

        box, self.input_file = add_page_input_box(line_frame, "Input file:", 70, 20,
                                                  stylesheet=Page_input_input, fix_width=False)
        section_layout.addWidget(box)

        # --------- spacer ------------

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        section_layout.addItem(spacer)

        # --------- line_frame: submission_hint, spacer, submit_button ------------

        line_frame = QFrame(section_frame)
        section_layout.addWidget(line_frame)
        line_layout = add_layout(line_frame, HORIZONTAL, l_m=8)

        self.submission_hint = add_label(line_frame, "", name="Page_hint", align=Qt.AlignVCenter)
        line_layout.addWidget(self.submission_hint)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        self.submit_button = add_button(line_frame, "SUBMIT", name="Page_button")
        line_layout.addWidget(self.submit_button)

        # --------- end job_submission, spacer ------------

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        window_layout.addItem(spacer)

    def enable_scheme_01_frame(self, event):
        if self.select_scheme != 1:
            # find the previous selected frame
            if self.select_scheme == 2:
                frame = self.scheme_02_frame
            elif self.select_scheme == 3:
                frame = self.scheme_03_frame
            else:
                frame = self.scheme_04_frame

            # set frame to disable stylesheet
            frame.setStyleSheet(Page_scheme_box_disable)

            # find all QLabel children within the frame
            labels = frame.findChildren(QLabel)

            # set labels to disable stylesheet
            for label in labels:
                label.setStyleSheet(Page_scheme_label_disable)

            # set flag
            self.select_scheme = 1

            # set frame to active stylesheet
            self.scheme_01_frame.setStyleSheet(Page_scheme_box)

            # find all QLabel children within the frame
            labels = self.scheme_01_frame.findChildren(QLabel)

            # set labels to enable stylesheet
            for label in labels:
                label.setStyleSheet(Page_scheme_label)

    def enable_scheme_02_frame(self, event):
        if self.select_scheme != 2:
            # find the previous selected frame
            if self.select_scheme == 1:
                frame = self.scheme_01_frame
            elif self.select_scheme == 3:
                frame = self.scheme_03_frame
            else:
                frame = self.scheme_04_frame

            # set frame to disable stylesheet
            frame.setStyleSheet(Page_scheme_box_disable)

            # find all QLabel children within the frame
            labels = frame.findChildren(QLabel)

            # set labels to disable stylesheet
            for label in labels:
                label.setStyleSheet(Page_scheme_label_disable)

            # set flag
            self.select_scheme = 2

            # set frame to active stylesheet
            self.scheme_02_frame.setStyleSheet(Page_scheme_box)

            # find all QLabel children within the frame
            labels = self.scheme_02_frame.findChildren(QLabel)

            # set labels to enable stylesheet
            for label in labels:
                label.setStyleSheet(Page_scheme_label)

    def enable_scheme_03_frame(self, event):
        if self.select_scheme != 3:
            # find the previous selected frame
            if self.select_scheme == 1:
                frame = self.scheme_01_frame
            elif self.select_scheme == 2:
                frame = self.scheme_02_frame
            else:
                frame = self.scheme_04_frame

            # set frame to disable stylesheet
            frame.setStyleSheet(Page_scheme_box_disable)

            # find all QLabel children within the frame
            labels = frame.findChildren(QLabel)

            # set labels to disable stylesheet
            for label in labels:
                label.setStyleSheet(Page_scheme_label_disable)

            # set flag
            self.select_scheme = 3

            # set frame to active stylesheet
            self.scheme_03_frame.setStyleSheet(Page_scheme_box)

            # find all QLabel children within the frame
            labels = self.scheme_03_frame.findChildren(QLabel)

            # set labels to enable stylesheet
            for label in labels:
                label.setStyleSheet(Page_scheme_label)

    def enable_scheme_04_frame(self, event):
        if self.select_scheme != 4:
            # find the previous selected frame
            if self.select_scheme == 1:
                frame = self.scheme_01_frame
            elif self.select_scheme == 2:
                frame = self.scheme_02_frame
            else:
                frame = self.scheme_03_frame

            # set frame to disable stylesheet
            frame.setStyleSheet(Page_scheme_box_disable)

            # find all QLabel children within the frame
            labels = frame.findChildren(QLabel)

            # set labels to disable stylesheet
            for label in labels:
                label.setStyleSheet(Page_scheme_label_disable)

            # set flag
            self.select_scheme = 4

            # set frame to active stylesheet
            self.scheme_04_frame.setStyleSheet(Page_scheme_box)

            # find all QLabel children within the frame
            labels = self.scheme_04_frame.findChildren(QLabel)

            # set labels to enable stylesheet
            for label in labels:
                label.setStyleSheet(Page_scheme_label)


class JobList(QFrame):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.table = None                   # widget
        self.search_bar = None              # input
        self.edit_button = None             # button
        self.remove_button = None           # button

        self.current_row = 0                # param number

        self._init_ui()
        self.setStyleSheet(page_style)

    def _init_ui(self):
        window_layout = add_layout(self, VERTICAL)

        # --------- table_workspace ------------

        table_workspace = QFrame(self)
        table_workspace.setFixedHeight(72)
        table_workspace.setObjectName("Page_table_workspace")
        window_layout.addWidget(table_workspace)
        workspace_layout = add_layout(table_workspace, HORIZONTAL, l_m=40, r_m=40, t_m=21, b_m=21, space=32)

        self.search_bar = QLineEdit(table_workspace)
        self.search_bar.setObjectName("Page_table_workspace_search")
        workspace_layout.addWidget(self.search_bar)
        self.search_bar.setFixedHeight(30)
        self.search_bar.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.search_bar.setPlaceholderText("Search a job...")

        self.edit_button = add_button(table_workspace, "EDIT", name="Page_table_workspace_button")
        workspace_layout.addWidget(self.edit_button)

        self.remove_button = add_button(table_workspace, "REMOVE", name="Page_table_workspace_button")
        workspace_layout.addWidget(self.remove_button)

        # --------- table_frame ------------

        table_frame = QFrame(self)
        window_layout.addWidget(table_frame)
        table_layout = add_layout(table_frame, VERTICAL, l_m=5, r_m=5, t_m=5)

        self.table = QTableWidget(table_frame)
        self.table.setObjectName("Page_table")
        table_layout.addWidget(self.table)

        table_headers = ["Job ID", "Workers #", "Cores", "Memory", "Price", "Status", "Logs"]
        table_headers_width = [150, 100, 100, 100, 120, 120, 1]

        self.table.setColumnCount(len(table_headers))
        self.table.setHorizontalHeaderLabels(table_headers)
        self.table.verticalHeader().setVisible(False)

        for i in range(len(table_headers_width)):
            self.table.setColumnWidth(i, table_headers_width[i])
        self.table.horizontalHeader().setStretchLastSection(True)

        # Set table property,
        # disable edited,
        # selected entire row,
        # single rows selected each time,
        # alternating coloring,
        # hide grid line
        # set default row height
        # self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setAlternatingRowColors(True)
        self.table.setShowGrid(False)
        self.table.verticalHeader().setDefaultSectionSize(40)

        # fill first 10 row with empty line
        column = self.table.columnCount()
        for r in range(13):
            self.table.insertRow(r)
            for c in range(column):
                self.table.setItem(r, c, QTableWidgetItem(""))

    # data format: [job_id, workers, cores, memory, price, status, logs]
    def add_data(self, data_obj):
        column = self.table.columnCount()
        data = data_obj["data"]

        if self.current_row <= 13:
            for i in range(column):
                self.table.setItem(self.current_row, i, QTableWidgetItem(data[i]))
                if self.table.item(self.current_row, i) is not None:
                    self.table.item(self.current_row, i).setTextAlignment(Qt.AlignCenter)
                    self.table.item(self.current_row, i).setFont(QFont("Helvetica Neue", 12, QFont.Light))

            self.current_row += 1
        else:
            row = self.table.rowCount()

            self.table.insertRow(row)
            for i in range(column):
                self.table.setItem(row, i, QTableWidgetItem(data[i]))
                if self.table.item(row, i) is not None:
                    self.table.item(row, i).setTextAlignment(Qt.AlignCenter)
                    self.table.item(row, i).setFont(QFont("Helvetica Neue", 12, QFont.Light))

#
#     # input data format: [job_id, workers, cores, memory, price, status, logs]
#     def on_submit_clicked(self):
#         workers = self.jobs_workspace.workers.text()
#         cores = self.jobs_workspace.cores.text()
#         memory = self.jobs_workspace.memory.text()
#         source_files = self.jobs_workspace.source_file.text()
#         input_files = self.jobs_workspace.input_file.text()
#
#         price = (float(cores) * float(workers)) * PRICING_CONSTANT
#
#         job_payload = {
#             "workers": workers,
#             "cores": cores,
#             "memory": memory,
#             "price": price,
#             "source_files": source_files,
#             "input_files": input_files,
#         }
#         job_api = Api("/jobs")
#         status, res = job_api.post(job_payload)
#
#         if status == 200:
#             job = res['job']
#             job_data = {
#                 "data": [job['_id'],
#                          job['workers'],
#                          job['cores'],
#                          job['memory'],
#                          job['price'],
#                          job['status'],
#                          "logs"],
#                 "job_id": job['_id'],
#                 "customer_id": job['customer_id'],
#             }
#
#             self.jobs_workspace.hint.setText("Successfully added job to queue.")
#             self.jobs_list.add_data(job_data)
#
#     def on_refresh_clicked(self):
#         self.jobs_workspace.hint.setText("Refreshing...")
#
#     def on_remove_clicked(self):
#         # clean hint
#         self.jobs_workspace.hint.setText("")
#
#         model = self.jobs_list.table.selectionModel()
#
#         # check if table has selected row
#         if not model.hasSelection():
#             pass
#         else:
#             row = model.selectedRows()[0].row()
#             column = self.jobs_list.table.columnCount()
#
#             # ask if user want to delete rows
#             question = Question("Are you sure you want to remove this?")
#
#             if question.exec_():
#
#                 self.jobs_list.table.removeRow(row)
#                 self.jobs_workspace.hint.setText(f"Remove job....")
#
#                 if row <= 9:
#                     self.jobs_list.current_row -= 1
#
#                     row = self.jobs_list.table.rowCount()
#                     self.jobs_list.table.insertRow(row)
#                     for c in range(column):
#                         self.jobs_list.table.setItem(row, c, QTableWidgetItem(""))
#
#
# # pure UI unit
# class JobsWorkspace(QFrame):
#
#     def __init__(self, *args, **kwargs):
#         super(QFrame, self).__init__(*args, **kwargs)
#
#         # variable
#         self.add_jobs = None            # button
#         self.workers = None             # input string
#         self.cores = None               # input number
#         self.memory = None              # input number
#         self.source_file = None         # input string
#         self.input_file = None          # input string
#
#         self.submit_button = None       # button
#         self.refresh_button = None      # button
#         self.remove_button = None       # button
#         self.hint = None                # string
#
#         self._init_ui()
#         self.setStyleSheet(page_style)
#
#     def _init_ui(self):
#         self.setObjectName("Page_input_frame")
#         self.setFixedHeight(165)
#         section_layout = add_layout(self, VERTICAL, l_m=30, r_m=30)
#
#         # line_01 frame
#         line_01_frame = QFrame(self)
#         line_01_layout = add_layout(line_01_frame, HORIZONTAL, t_m=35, space=25)
#
#         box, self.workers = add_input_box_02(line_01_frame, "Workers #:")
#         line_01_layout.addWidget(box)
#
#         box, self.cores = add_input_box_02(line_01_frame, "Cores #:")
#         line_01_layout.addWidget(box)
#
#         box, self.memory = add_input_box_02(line_01_frame, "Memory:")
#         line_01_layout.addWidget(box)
#
#         spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
#         line_01_layout.addItem(spacer)
#
#         # line_02 frame
#         line_02_frame = QFrame(self)
#         line_02_layout = add_layout(line_02_frame, HORIZONTAL)
#
#         # left frame
#         left_frame = QFrame(line_02_frame)
#         left_layout = add_layout(left_frame, VERTICAL, t_m=20, space=20)
#
#         box, self.source_file = add_input_box_02(left_frame, "Source files:", fix_width=False)
#         left_layout.addWidget(box)
#
#         box, self.input_file = add_input_box_02(left_frame, "Input files:", fix_width=False)
#         left_layout.addWidget(box)
#
#         spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
#         left_layout.addItem(spacer)
#
#         # right frame
#         right_frame = QFrame(line_02_frame)
#         right_frame.setFixedWidth(286)
#         right_layout = add_layout(right_frame, VERTICAL, l_m=74, t_m=5, space=10)
#
#         spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
#         right_layout.addItem(spacer)
#
#         self.hint = add_label(right_frame, "", name="Page_hint", align=Qt.AlignBottom)
#         self.hint.setFixedHeight(15)
#         right_layout.addWidget(self.hint)
#
#         # button frame
#         button_frame_01 = QFrame(right_frame)
#         button_layout = add_layout(button_frame_01, HORIZONTAL, space=15)
#
#         self.submit_button = add_button(right_frame, text="SUBMIT", name="Page_button_small")
#         button_layout.addWidget(self.submit_button)
#
#         self.refresh_button = add_button(right_frame, text="REFRESH", name="Page_button_small")
#         button_layout.addWidget(self.refresh_button)
#
#         button_frame_02 = QFrame(right_frame)
#         button_layout = add_layout(button_frame_02, HORIZONTAL, space=15)
#
#         self.remove_button = add_button(right_frame, text="REMOVE", name="Page_button_small")
#         button_layout.addWidget(self.remove_button)
#
#         spacer = QSpacerItem(113, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
#         button_layout.addItem(spacer)
#
#         right_layout.addWidget(button_frame_01)
#         right_layout.addWidget(button_frame_02)
#
#         spacer = QSpacerItem(34, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
#
#         line_02_layout.addWidget(left_frame)
#         line_02_layout.addWidget(right_frame)
#         line_02_layout.addItem(spacer)
#
#         spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
#
#         section_layout.addWidget(line_01_frame)
#         section_layout.addWidget(line_02_frame)
#         section_layout.addItem(spacer)
#
#     def _fetch_job_data(self):
#         job_api = Api("/jobs")
#         status, res = job_api.get()
#
#         if status == 200:
#             for job in res["jobs"]:
#                 job_data = {
#                     "data": [job['_id'],
#                              job['workers'],
#                              job['cores'],
#                              job['memory'],
#                              job['price'],
#                              job['status'],
#                              "logs"],
#                     "job_id": job['_id'],
#                     "customer_id": job['customer_id'],
#                 }
#                 self.add_data(job_data)

