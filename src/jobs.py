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
from src.uix.popup import Question


class Jobs(MainView):

    def __init__(self, *args, **kwargs):
        super(Jobs, self).__init__(*args, **kwargs)

        # variable
        self.menu = None
        self.add_jobs = None

        self.jobs_workspace = None
        self.jobs_list = None

        self._init_ui()
        self.setStyleSheet(page_style)

    def _init_ui(self):
        section_layout = add_layout(self, VERTICAL)

        # menu frame
        self.menu = QFrame(self)
        self.menu.setFixedHeight(41)

        menu_layout = add_layout(self.menu, HORIZONTAL, t_m=6, l_m=40, r_m=40, space=40)

        self.add_jobs = add_button(self.menu, "Add Jobs", stylesheet=page_menu_button_active)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        menu_layout.addWidget(self.add_jobs)
        menu_layout.addItem(spacer)

        self.jobs_workspace = JobsWorkspace(self)
        self.jobs_list = JobsList(self)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        section_layout.addWidget(self.menu)
        section_layout.addWidget(self.jobs_workspace)
        section_layout.addWidget(self.jobs_list)
        section_layout.addItem(spacer)

        # connect function
        self.jobs_workspace.submit_button.clicked.connect(self.on_submit_clicked)
        self.jobs_workspace.refresh_button.clicked.connect(self.on_refresh_clicked)
        self.jobs_workspace.remove_button.clicked.connect(self.on_remove_clicked)

    # input data format: [job_id, workers, cores, memory, price, status, logs]
    def on_submit_clicked(self):

        # job_id generating strategy
        from random import randint
        job_id = "A01085" + str(randint(10, 99))

        workers = self.jobs_workspace.workers.text()
        cores = self.jobs_workspace.cores.text()
        memory = self.jobs_workspace.memory.text()

        # TODO: evaluate price here
        price = "15 credits / hr"

        # TODO: check if submission is success
        status = "Submitting"

        # TODO: what and where to present in this column
        # temp set logs value
        logs = "Logs"

        # testing
        # self.jobs_list.add_data(["AC1827320", "3", "4", "2", "15 credits / hr", "running", "No log shows"])
        # self.jobs_list.add_data(["DC1672343", "4", "3", "1", "15 credits / hr", "running", "No log shows"])
        # self.jobs_list.add_data(["AC1456462", "2", "2", "1", "15 credits / hr", "running", "No log shows"])

        self.jobs_workspace.hint.setText("Submission success!")
        self.jobs_list.add_data([job_id, workers, cores, memory, price, status, logs])

    def on_refresh_clicked(self):
        self.jobs_workspace.hint.setText("Refresh is clicked")

    def on_remove_clicked(self):
        # clean hint
        self.jobs_workspace.hint.setText("")

        model = self.jobs_list.table.selectionModel()

        # check if table has selected row
        if not model.hasSelection():
            pass
        else:
            row = model.selectedRows()[0].row()
            column = self.jobs_list.table.columnCount()

            # check if row has value
            if self.jobs_list.table.item(row, column - 2).text() is not "":

                # ask if user want to delete rows
                confirm_removal = Question(self)
                answer = confirm_removal.ask("Are you sure you want to remove this?")

                if answer:
                    self.jobs_list.table.removeRow(row)

                    if row <= 9:
                        self.jobs_list.current_row -= 1

                        row = self.jobs_list.table.rowCount()
                        self.jobs_list.table.insertRow(row)
                        for c in range(column):
                            self.jobs_list.table.setItem(row, c, QTableWidgetItem(""))


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
        self.remove_button = None       # button
        self.hint = None                # string

        self._init_ui()
        self.setStyleSheet(page_style)

    def _init_ui(self):
        self.setObjectName("Page_input_frame")
        self.setFixedHeight(165)
        section_layout = add_layout(self, VERTICAL, l_m=30, r_m=30)

        # line_01 frame
        line_01_frame = QFrame(self)
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
        line_02_frame = QFrame(self)
        line_02_layout = add_layout(line_02_frame, HORIZONTAL)

        # left frame
        left_frame = QFrame(line_02_frame)
        left_layout = add_layout(left_frame, VERTICAL, t_m=20, space=20)

        box, self.source_file = add_input_box_02(left_frame, "Source file:", fix_width=False)
        left_layout.addWidget(box)

        box, self.input_file = add_input_box_02(left_frame, "Input file:", fix_width=False)
        left_layout.addWidget(box)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        left_layout.addItem(spacer)

        # right frame
        right_frame = QFrame(line_02_frame)
        right_frame.setFixedWidth(286)
        right_layout = add_layout(right_frame, VERTICAL, l_m=74, t_m=5, space=10)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        right_layout.addItem(spacer)

        self.hint = add_label(right_frame, "", name="Page_hint", align=Qt.AlignBottom)
        self.hint.setFixedHeight(15)
        right_layout.addWidget(self.hint)

        # button frame
        button_frame_01 = QFrame(right_frame)
        button_layout = add_layout(button_frame_01, HORIZONTAL, space=15)

        self.submit_button = add_button(right_frame, text="SUBMIT", name="Page_button_small")
        button_layout.addWidget(self.submit_button)

        self.refresh_button = add_button(right_frame, text="REFRESH", name="Page_button_small")
        button_layout.addWidget(self.refresh_button)

        button_frame_02 = QFrame(right_frame)
        button_layout = add_layout(button_frame_02, HORIZONTAL, space=15)

        self.remove_button = add_button(right_frame, text="REMOVE", name="Page_button_small")
        button_layout.addWidget(self.remove_button)

        spacer = QSpacerItem(113, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
        button_layout.addItem(spacer)

        right_layout.addWidget(button_frame_01)
        right_layout.addWidget(button_frame_02)

        spacer = QSpacerItem(34, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        line_02_layout.addWidget(left_frame)
        line_02_layout.addWidget(right_frame)
        line_02_layout.addItem(spacer)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        section_layout.addWidget(line_01_frame)
        section_layout.addWidget(line_02_frame)
        section_layout.addItem(spacer)


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
        # hide gird line
        # set default row height
        # self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
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

    # data format: [job_id, workers, cores, memory, price, status, logs]
    def add_data(self, data):
        column = self.table.columnCount()

        if self.current_row <= 9:
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
