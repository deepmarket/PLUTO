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


class Jobs(MainView):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.jobs_workspace = None
        self.jobs_list = None

        self._init_ui()
        self.setStyleSheet(page_style)

        self.clean()

    def _init_ui(self):
        section_layout = add_layout(self, VERTICAL)

        self.jobs_workspace = JobsWorkspace(self)
        self.jobs_list = JobsList(self)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        section_layout.addWidget(self.jobs_workspace)
        section_layout.addWidget(self.jobs_list)
        section_layout.addItem(spacer)

        # connect function
        self.jobs_workspace.submit_button.clicked.connect(self.on_submit_clicked)

    def on_submit_clicked(self):

        # TODO: job_id generating strategy
        from random import randint
        job_id = "A01085" + str(randint(10, 99))

        workers = self.jobs_workspace.workers.text()
        cores = self.jobs_workspace.cores.text()
        memory = self.jobs_workspace.memory.text()

        # TODO: check if submission is success

        status = "Submitting"

        # TODO: what and where to present in this column
        # temp set logs value
        logs = "Logs"

        # testing
        # self.jobs_list.add_data(["AC1827320", "3", "4", "2", "running", "No log shows"])
        # self.jobs_list.add_data(["DC1672343", "4", "3", "1", "running", "No log shows"])
        # self.jobs_list.add_data(["AC1456462", "2", "2", "1", "running", "No log shows"])

        self.jobs_workspace.hint.setText("Submission success!")
        self.jobs_list.add_data([job_id, workers, cores, memory, status, logs])

    def clean(self):
        self.jobs_workspace.workers.setText("")
        self.jobs_workspace.cores.setText("")
        self.jobs_workspace.memory.setText("")
        self.jobs_workspace.source_file.setText("")
        self.jobs_workspace.input_file.setText("")
        self.jobs_workspace.hint.setText("")


# pure UI unit
class JobsWorkspace(QFrame):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.add_jobs = None            # button
        self.workers = None             # input string
        self.cores = None               # input number
        self.memory = None              # input number
        self.source_file = None         # input string
        self.input_file = None          # input string

        self.submit_button = None       # button
        self.refresh_button = None      # button
        self.hint = None                # button

        self._init_ui()
        self.setStyleSheet(page_style)

    def _init_geometry(self):
        self.setFixedHeight(206)

    def _init_ui(self):
        section_layout = add_layout(self, VERTICAL, t_m=6)

        # menu frame
        menu_frame = QFrame(self)
        menu_layout = add_layout(menu_frame, HORIZONTAL, l_m=40, r_m=40, space=40)

        self.add_jobs = add_button(menu_frame, "Add Jobs", stylesheet=page_menu_button_active)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        menu_layout.addWidget(self.add_jobs)
        menu_layout.addItem(spacer)

        # input frame
        input_frame = QFrame(self)
        input_frame.setObjectName("Page_input_frame")
        input_frame.setFixedHeight(165)

        input_layout = add_layout(input_frame, VERTICAL, l_m=30, r_m=30, space=20)

        # line_01 frame
        line_01_frame = QFrame(input_frame)
        line_01_layout = add_layout(line_01_frame, HORIZONTAL, t_m=35, space=25)

        box, self.workers = add_input_box_02(line_01_frame, "Workers #:")
        line_01_layout.addWidget(box)

        box, self.cores = add_input_box_02(line_01_frame, "Cores #:")
        line_01_layout.addWidget(box)

        box, self.memory = add_input_box_02(line_01_frame, "Memory:")
        line_01_layout.addWidget(box)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_01_layout.addItem(spacer)

        # line_02 frame
        line_02_frame = QFrame(input_frame)
        line_02_layout = add_layout(line_02_frame, HORIZONTAL)

        # left frame
        left_frame = QFrame(line_02_frame)
        left_layout = add_layout(left_frame, VERTICAL, space=20)

        box, self.source_file = add_input_box_02(left_frame, "Source file:", fix_length=False)
        left_layout.addWidget(box)

        box, self.input_file = add_input_box_02(left_frame, "Input file:", fix_length=False)
        left_layout.addWidget(box)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        left_layout.addItem(spacer)

        # right frame
        right_frame = QFrame(line_02_frame)
        right_frame.setFixedWidth(286)
        right_layout = add_layout(right_frame, VERTICAL, l_m=74, b_m=25, space=15)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        right_layout.addItem(spacer)

        self.hint = add_label(right_frame, "", name="Page_hint", align=Qt.AlignBottom)
        self.hint.setFixedHeight(15)
        right_layout.addWidget(self.hint)

        # button frame
        button_frame = QFrame(right_frame)
        button_layout = add_layout(button_frame, HORIZONTAL, space=15)

        self.submit_button = add_button(right_frame, text="SUBMIT", name="Page_button_large")
        button_layout.addWidget(self.submit_button)

        self.refresh_button = add_button(right_frame, text="REFRESH", name="Page_button_large")
        button_layout.addWidget(self.refresh_button)

        right_layout.addWidget(button_frame)

        spacer = QSpacerItem(34, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        line_02_layout.addWidget(left_frame)
        line_02_layout.addWidget(right_frame)
        line_02_layout.addItem(spacer)

        input_layout.addWidget(line_01_frame)
        input_layout.addWidget(line_02_frame)

        section_layout.addWidget(menu_frame)
        section_layout.addWidget(input_frame)


# pure UI unit
class JobsList(QFrame):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.table = None               # section
        self.current_row = 0            # param number

        self._init_geometry()
        self._init_ui()
        self.setStyleSheet(page_style)

    def _init_geometry(self):
        self.setFixedHeight(470)

    def _init_ui(self):
        section_layout = add_layout(self, HORIZONTAL, t_m=4, b_m=4, l_m=4, r_m=4)

        self.table = QTableWidget(self)
        self.table.setObjectName("Page_table")

        table_headers = ["Job ID", "Workers #", "Cores", "Memory", "Status", "Logs", ""]
        table_headers_width = [150, 100, 100, 100, 120, 300, 1]

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
        # hide gird line
        # set default row height
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setAlternatingRowColors(True)
        self.table.setShowGrid(False)
        self.table.verticalHeader().setDefaultSectionSize(40)

        # fill first 10 row with empty line
        column = self.table.columnCount()
        for r in range(10):
            self.table.insertRow(r)
            for c in range(column):
                self.table.setItem(r, c, QTableWidgetItem(""))

        section_layout.addWidget(self.table)

    # data format: [job_id, workers, cores, memory, status, logs]
    def add_data(self, data):
        column = self.table.columnCount()-1

        if self.current_row <= 9:
            for i in range(column):
                self.table.setItem(self.current_row, i, QTableWidgetItem(data[i]))
                self.table.item(self.current_row, i).setTextAlignment(Qt.AlignCenter)
                self.table.item(self.current_row, i).setFont(QFont("Helvetica Neue", 12, QFont.Light))

            button = add_button(self.table, "x", name="Page_table_button")
            self.table.setCellWidget(self.current_row, column, button)

            button.clicked.connect(partial(self.remove_data, self.current_row))

            self.current_row += 1
        else:
            row = self.table.rowCount()

            self.table.insertRow(row)
            for i in range(column):
                self.table.setItem(row, i, QTableWidgetItem(data[i]))
                self.table.item(row, i).setTextAlignment(Qt.AlignCenter)
                self.table.item(row, i).setFont(QFont("Helvetica Neue", 12, QFont.Light))

            button = add_button(self.table, "x", name="Page_table_button")
            self.table.setCellWidget(row, column, button)

            button.clicked.connect(partial(self.remove_data, self.current_row))

    def remove_data(self, row):

        # confirm_removal = Question("Are you sure you want to remove this?")
        self.table.removeRow(row)
