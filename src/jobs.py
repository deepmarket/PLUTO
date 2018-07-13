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

        button_frame, button_layout = add_frame(self, height=35, layout=HORIZONTAL, l_m=40, r_m=40, space=24)
        section_layout.addWidget(button_frame)

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

        self.workspace.submit_button.clicked.connect(self.on_submit_clicked)
        self.list.remove_button.clicked.connect(self.on_remove_clicked)

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

        self._fetch_job_data()

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

    # input data format: [job_id, workers, cores, memory, price, status, logs]
    def on_submit_clicked(self):
        workers = self.workspace.workers.text()
        cores = self.workspace.cores.text()
        memory = self.workspace.memory.text()
        source_files = self.workspace.source_file.text()
        input_files = self.workspace.input_file.text()
        # price = (float(cores) * float(workers)) * PRICING_CONSTANT

        # find the selected frame
        if self.workspace.select_scheme == 1:
            frame = self.workspace.scheme_01_frame
        elif self.workspace.select_scheme == 2:
            frame = self.workspace.scheme_02_frame
        elif self.workspace.select_scheme == 3:
            frame = self.workspace.scheme_03_frame
        else:
            frame = self.workspace.scheme_04_frame

        # get text
        text = []
        labels = frame.findChildren(QLabel)

        for label in labels:
            text.append(label.text())

        # TODO: generate job name here
        job_id = "My-Job-01"

        question = f"""Job "{job_id}" will be charged with """
        question += f"""CPU: {text[1]}, GPU: {text[2]}, Memory: {text[3]}\nDisk Space: {text[4]} """
        question += f"""and run in the Time slot: {text[0]}\n\n"""
        question += f"""You are required """
        question += f"""worker #: {workers}, Cores #: {cores}, Memory: {memory} GB for this submission.\n\n"""
        question += f"""Do you want to submit this job at the above mentioned rate and time slot?"""

        question = Question(question)

        if question.exec_():
            dat = [workers, cores, memory, "0.005", source_files, input_files, "-"]

            # add data to list
            self.list.add_data(dat)

            # add data to db
            self._post_job_data(dat)

            # switch page
            self.on_list_clicked()

    # remove button functionality for JobList
    def on_remove_clicked(self):
        model = self.list.table.selectionModel()

        # check if table has selected row
        if not model.hasSelection():
            pass
        else:
            row = model.selectedRows()[0].row()
            column = self.list.table.columnCount()

            # ask if user want to delete rows
            question = Question("Are you sure you want to remove this?")

            if question.exec_():
                self.list.table.removeRow(row)

                if row <= 9:
                    self.list.current_row -= 1
                    row = self.list.table.rowCount()
                    self.list.table.insertRow(row)
                    for c in range(column):
                        self.list.table.setItem(row, c, QTableWidgetItem(""))

    # load data from db
    def _fetch_job_data(self):

        job_api = Api("/jobs")
        status, res = job_api.get()

        if status == 200:
            for job in res["jobs"]:
                self.list.add_data([job['_id'],
                                    job['workers'],
                                    job['cores'],
                                    job['memory'],
                                    job['price'],
                                    job['status'], "-"])

    # submit data to db
    @staticmethod
    def _post_job_data(dat):
        job_data = {"data": dat, "job_id": dat[0], "customer_id": "customer_id"}

        job_api = Api("/jobs")

        status, res = job_api.post(job_data)

        print(res)


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

        section_frame, section_layout = add_frame(self, space=18)
        window_layout.addWidget(section_frame)

        # --------- line_frame: title, spacer ------------

        line_frame = QFrame(section_frame)
        section_layout.addWidget(line_frame)
        line_layout = add_layout(line_frame, HORIZONTAL)

        title = add_label(line_frame, "Pricing Scheme", name="Page_section_title", align=Qt.AlignVCenter)
        line_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        # --------- begin sub_section: left_section, right_section ------------

        sub_section_frame, sub_section_layout = add_frame(section_frame, height=211, layout=HORIZONTAL)
        section_layout.addWidget(sub_section_frame)

        # --------- left_section: scheme_title, four scheme choice frame, spacer ------------

        left_frame, left_layout = add_frame(sub_section_frame, name="Page_scheme", layout=HORIZONTAL,
                                            l_m=28, t_m=12, b_m=12, space=10)
        sub_section_layout.addWidget(left_frame)

        # --------- title_frame ------------

        title_frame, title_layout = add_frame(left_frame, t_m=31, b_m=32, r_m=13, space=16)
        left_layout.addWidget(title_frame)

        titles = ["Time", "CPU:", "GPU:", "Memory:", "Disk Space:"]
        add_labels(title_layout, title_frame, titles, Page_scheme_label_disable, Qt.AlignRight)

        # --------- scheme_01_frame ------------

        self.scheme_01_frame, scheme_layout = add_frame(left_frame, width=124, stylesheet=Page_scheme_box,
                                                        t_m=31, b_m=32, space=16)
        left_layout.addWidget(self.scheme_01_frame)

        labels = ["12:00 AM - 5:59 AM", "0 Credit/Hr", "0 Credit/Hr", "0 Credit/Hr", "0 Credit/Hr"]
        add_labels(scheme_layout, self.scheme_01_frame, labels, Page_scheme_label, Qt.AlignHCenter)

        self.scheme_01_frame.mousePressEvent = self.enable_scheme_01_frame

        # --------- scheme_02_frame ------------

        self.scheme_02_frame, scheme_layout = add_frame(left_frame, width=124, stylesheet=Page_scheme_box_disable,
                                                        t_m=31, b_m=32, space=16)
        left_layout.addWidget(self.scheme_02_frame)

        labels[0] = "6:00 AM - 11:59 PM"
        add_labels(scheme_layout, self.scheme_02_frame, labels, Page_scheme_label_disable, Qt.AlignHCenter)

        self.scheme_02_frame.mousePressEvent = self.enable_scheme_02_frame

        # --------- scheme_03_frame ------------

        self.scheme_03_frame, scheme_layout = add_frame(left_frame, width=124, stylesheet=Page_scheme_box_disable,
                                                        t_m=31, b_m=32, space=16)
        left_layout.addWidget(self.scheme_03_frame)

        labels[0] = "12:00 PM - 5: 59 PM"
        add_labels(scheme_layout, self.scheme_03_frame, labels, Page_scheme_label_disable, Qt.AlignHCenter)

        self.scheme_03_frame.mousePressEvent = self.enable_scheme_03_frame

        # --------- scheme_04_frame ------------

        self.scheme_04_frame, scheme_layout = add_frame(left_frame, width=124, stylesheet=Page_scheme_box_disable,
                                                        t_m=31, b_m=32, space=16)
        left_layout.addWidget(self.scheme_04_frame)

        labels[0] = "6:00 PM - 11: 59 PM"
        add_labels(scheme_layout, self.scheme_04_frame, labels, Page_scheme_label_disable, Qt.AlignHCenter)

        self.scheme_04_frame.mousePressEvent = self.enable_scheme_04_frame

        # --------- spacer ------------

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        left_layout.addItem(spacer)

        # --------- right_section: title, available cpu, gpu, memory, disk_space ------------

        right_frame, right_layout = add_frame(sub_section_frame, width=170, name="Page_available_resources",
                                              t_m=37, b_m=40)
        sub_section_layout.addWidget(right_frame)

        title = add_label(right_frame, "Available Resources", name="Page_available_title", align=Qt.AlignCenter)
        title.setFixedHeight(13)
        right_layout.addWidget(title)

        spacer = QSpacerItem(0, 17, QSizePolicy.Minimum, QSizePolicy.Fixed)
        right_layout.addItem(spacer)

        # --------- line_frame: cpu, gpu, memory, disk_space ------------

        line_frame, line_layout = add_frame(right_frame, l_m=30, r_m=30, space=16)
        right_layout.addWidget(line_frame)

        self.available_cpu = add_label(line_frame, "CPU #: 0", name="Page_available_label")
        line_layout.addWidget(self.available_cpu)

        self.available_gpu = add_label(line_frame, "GPU #: 0", name="Page_available_label")
        line_layout.addWidget(self.available_gpu)

        self.available_memory = add_label(line_frame, "Memory: 0 GB", name="Page_available_label")
        line_layout.addWidget(self.available_memory)

        self.available_disk = add_label(line_frame, "Disk Space: 0 GB", name="Page_available_label")
        line_layout.addWidget(self.available_disk)

        # --------- begin job_submission ------------

        section_frame, section_layout = add_frame(self, space=18)
        window_layout.addWidget(section_frame)

        # --------- line_frame: title, spacer ------------

        line_frame, line_layout = add_frame(section_frame, layout=HORIZONTAL)
        section_layout.addWidget(line_frame)

        title = add_label(line_frame, "Job Submission", name="Page_section_title", align=Qt.AlignVCenter)
        line_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        # --------- begin sub_section ------------

        sub_section_frame, sub_section_layout = add_frame(section_frame, height=234, name="Page_job_submission",
                                                          t_m=25, b_m=25, l_m=30, r_m=30, space=22)
        section_layout.addWidget(sub_section_frame)

        # --------- line_frame: workers, cores, memory ------------

        line_frame, line_layout = add_frame(section_frame, layout=HORIZONTAL)
        sub_section_layout.addWidget(line_frame)

        box, self.workers = add_page_input_box(line_frame, "Workers #:", 70, 20, stylesheet=Page_input_input)
        line_layout.addWidget(box)

        box, self.cores = add_page_input_box(line_frame, "Cores #:", 70, 20, stylesheet=Page_input_input)
        line_layout.addWidget(box)

        box, self.memory = add_page_input_box(line_frame, "Memory:", 70, 20, stylesheet=Page_input_input)
        line_layout.addWidget(box)

        # --------- source_file and input_file ------------

        box, self.source_file = add_page_input_box(line_frame, "Source file:", 70, 20,
                                                   stylesheet=Page_input_input, fix_width=False)
        sub_section_layout.addWidget(box)

        box, self.input_file = add_page_input_box(line_frame, "Input file:", 70, 20,
                                                  stylesheet=Page_input_input, fix_width=False)
        sub_section_layout.addWidget(box)

        # --------- spacer ------------

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        sub_section_layout.addItem(spacer)

        # --------- line_frame: submission_hint, spacer, submit_button ------------

        line_frame, line_layout = add_frame(section_frame, layout=HORIZONTAL, l_m=8)
        sub_section_layout.addWidget(line_frame)

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
        set_frame(self, 1, self.scheme_01_frame)

    def enable_scheme_02_frame(self, event):
        set_frame(self, 2, self.scheme_02_frame)

    def enable_scheme_03_frame(self, event):
        set_frame(self, 3, self.scheme_03_frame)

    def enable_scheme_04_frame(self, event):
        set_frame(self, 4, self.scheme_04_frame)


class JobList(QFrame):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.table = None                   # widget
        self.search_bar = None              # input
        self.refresh_button = None          # button
        self.remove_button = None           # button

        self.current_row = 0                # param number

        self._init_ui()
        self.setStyleSheet(page_style)

    def _init_ui(self):
        window_layout = add_layout(self, VERTICAL)

        # --------- table_workspace ------------

        table_workspace, workspace_layout = add_frame(self, height=72, name="Page_table_workspace", layout=HORIZONTAL,
                                                      l_m=40, r_m=40, t_m=21, b_m=21, space=32)
        window_layout.addWidget(table_workspace)

        self.search_bar = add_input(table_workspace, height=30, name="Page_table_workspace_search",
                                    hint="Search a job... (Haven't implemented yet)")
        workspace_layout.addWidget(self.search_bar)

        self.refresh_button = add_button(table_workspace, "REFRESH", name="Page_table_workspace_button")
        workspace_layout.addWidget(self.refresh_button)

        self.remove_button = add_button(table_workspace, "REMOVE", name="Page_table_workspace_button")
        workspace_layout.addWidget(self.remove_button)

        # --------- table_frame ------------

        table_frame, table_layout = add_frame(self, l_m=5, r_m=5, t_m=5)
        window_layout.addWidget(table_frame)

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
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
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

        # for testing TODO: change back when finish testing
        data = data_obj
        # data = data_obj["data"]

        if self.current_row <= 13:
            add_row(self.table, column, data, self.current_row)

            self.current_row += 1
        else:
            row = self.table.rowCount()

            self.table.insertRow(row)
            add_row(self.table, column, data, row)



