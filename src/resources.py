"""
    The following items can be interacted:

    class ResourcesWorkspace:

        self.add_resources = None       # button
        self.machine_name = None        # input string
        self.ip_address = None          # input string
        self.cpu_gpu = None             # input number
        self.cores = None               # input number
        self.ram = None                 # input number

        self.hint = None                # label string
        self.test_button = None         # button
        self.add_button = None          # button
        self.remove_button = None       # button

    class ResourcesList:

        self.table = None           # table widget
        self.current_row = 0        # param number
"""

from src.mainview import MainView
from src.uix.util import *
from src.uix.popup import Question


class Resources(MainView):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.resources_workspace = None
        self.resources_list = None
        self.if_test = False

        self.price = None

        self._init_ui()
        self.setStyleSheet(page_style)

    def _init_ui(self):
        section_layout = add_layout(self, VERTICAL)

        self.resources_workspace = ResourcesWorkspace(self)
        self.resources_list = ResourcesList(self)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        section_layout.addWidget(self.resources_workspace)
        section_layout.addWidget(self.resources_list)
        section_layout.addItem(spacer)

        # connect function
        self.resources_workspace.test_button.clicked.connect(self.on_test_clicked)
        self.resources_workspace.add_button.clicked.connect(self.on_add_clicked)
        self.resources_workspace.remove_button.clicked.connect(self.on_remove_clicked)

    def on_test_clicked(self):
        # TODO: evaluate price here

        self.price = "15 credits / hr"

        # TEST PASS
        self.resources_workspace.hint.setText("TEST PASS. Be able to add.")
        self.if_test = True

    # input data format: [machine_name, ip_address, cpu_gpu, cores, ram, price, status]
    def on_add_clicked(self):
        if not self.if_test:
            # testing
            # self.resources_list.add_data(["Martin-Mac", "100.10.2.1", "4", "2", "4", "$30/hr", "running"])
            # self.resources_list.add_data(["Martin-Window", "180.10.2.1", "3", "1", "2", "$15/hr", "running"])
            # self.resources_list.add_data(["Martin-Linux", "120.10.2.1", "1", "1", "1", "$8.5/hr", "finished"])

            self.resources_workspace.hint.setText("The resource must be tested before add.")
        else:
            # resource information
            machine_name = self.resources_workspace.machine_name.text()
            ip_address = self.resources_workspace.ip_address.text()
            cpu_gpu = self.resources_workspace.cpu_gpu.text()
            cores = self.resources_workspace.cores.text()
            ram = self.resources_workspace.ram.text()

            # first status would be 'Submitting'
            status = "Submitting"

            self.resources_list.add_data([machine_name, ip_address, cpu_gpu, cores, ram, self.price, status])

    def on_remove_clicked(self):
        model = self.resources_list.table.selectionModel()

        # check if table has selected row
        if not model.hasSelection():
            pass
        else:
            row = model.selectedRows()[0].row()
            column = self.resources_list.table.columnCount()

            # check if row has value
            if self.resources_list.table.item(row, column-1).text() is not "":

                # ask if user want to delete rows
                confirm_removal = Question(self)
                answer = confirm_removal.ask("Are you sure you want to remove this?")

                if answer:
                    self.resources_list.table.removeRow(row)

                    if row <= 9:
                        self.resources_list.current_row -= 1

                        row = self.resources_list.table.rowCount()
                        self.resources_list.table.insertRow(row)
                        for c in range(column):
                            self.resources_list.table.setItem(row, c, QTableWidgetItem(""))


# pure UI unit
class ResourcesWorkspace(QFrame):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.add_resources = None       # button
        self.machine_name = None        # input string
        self.ip_address = None          # input string
        self.cpu_gpu = None             # input number
        self.cores = None               # input number
        self.ram = None                 # input number

        self.hint = None                # label string
        self.test_button = None         # button
        self.add_button = None          # button
        self.remove_button = None       # button

        self._init_ui()
        self.setStyleSheet(page_style)

    def _init_geometry(self):
        self.setFixedHeight(206)

    def _init_ui(self):
        section_layout = add_layout(self, VERTICAL, t_m=6)

        # menu frame
        menu_frame = QFrame(self)
        menu_layout = add_layout(menu_frame, HORIZONTAL, l_m=40, r_m=40, space=40)

        self.add_resources = add_button(menu_frame, "Add Resources", stylesheet=page_menu_button_active)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        menu_layout.addWidget(self.add_resources)
        menu_layout.addItem(spacer)

        # input frame
        input_frame = QFrame(self)
        input_frame.setObjectName("Page_input_frame")
        input_frame.setFixedHeight(165)

        input_layout = add_layout(input_frame, VERTICAL, l_m=30, r_m=30, space=20)

        # line_01 frame
        line_01_frame = QFrame(input_frame)
        line_01_layout = add_layout(line_01_frame, HORIZONTAL, t_m=35, space=30)

        box, self.machine_name = add_input_box_02(line_01_frame, "Machine Name:")
        line_01_layout.addWidget(box)

        box, self.ip_address = add_input_box_02(line_01_frame, "IP Address:", fix_length=False)
        line_01_layout.addWidget(box)

        # line_02 frame
        line_02_frame = QFrame(input_frame)
        line_02_layout = add_layout(line_02_frame, HORIZONTAL, space=30)

        box, self.cpu_gpu = add_input_box_02(line_02_frame, "CPUs/GPUs #:")
        line_02_layout.addWidget(box)

        box, self.cores = add_input_box_02(line_02_frame, "Cores:")
        line_02_layout.addWidget(box)

        box, self.ram = add_input_box_02(line_02_frame, "Ram (Gb.):", fix_length=False)
        line_02_layout.addWidget(box)

        # line_03 frame
        line_03_frame = QFrame(input_frame)
        line_03_layout = add_layout(line_03_frame, HORIZONTAL, space=30)

        spacer = QSpacerItem(5, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
        line_03_layout.addItem(spacer)

        self.hint = add_label(line_03_frame, text="", name="Page_hint", align=Qt.AlignVCenter)
        line_03_layout.addWidget(self.hint)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_03_layout.addItem(spacer)

        self.test_button = add_button(line_03_frame, text="TEST", name="Page_button_small")
        line_03_layout.addWidget(self.test_button)

        self.add_button = add_button(line_03_frame, text="ADD", name="Page_button_small")
        line_03_layout.addWidget(self.add_button)

        self.remove_button = add_button(line_03_frame, text="REMOVE", name="Page_button_small")
        line_03_layout.addWidget(self.remove_button)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        input_layout.addWidget(line_01_frame)
        input_layout.addWidget(line_02_frame)
        input_layout.addWidget(line_03_frame)
        input_layout.addItem(spacer)

        section_layout.addWidget(menu_frame)
        section_layout.addWidget(input_frame)


# pure UI unit
class ResourcesList(QFrame):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.table = None           # table widget
        self.current_row = 0        # param number

        self._init_geometry()
        self._init_ui()
        self.setStyleSheet(page_style)

    def _init_geometry(self):
        self.setFixedHeight(470)

    def _init_ui(self):
        section_layout = add_layout(self, HORIZONTAL, t_m=4, b_m=4, l_m=4, r_m=4)

        self.table = QTableWidget(self)
        self.table.setObjectName("Page_table")

        table_headers = ["Machine Name", "IP Address", "CPUs/GPUs", "Cores", "Ram (Gb.)", "Price", "Status"]
        table_headers_width = [150, 150, 100, 100, 100, 120, 150]

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

    # data format: [machine_name, ip_address, cpu_gpu, cores, ram, price, status]
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
