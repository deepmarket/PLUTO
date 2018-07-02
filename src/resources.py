"""
    The following items can be interacted:

    class ResourcesWorkspace:

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
from src.api import Api

# Amount per (core * worker) / hour
PRICING_CONSTANT = 0.005


class Resources(MainView):

    def __init__(self, *args, **kwargs):
        super(Resources, self).__init__(*args, **kwargs)

        # variable
        self.menu = None
        self.add_resources = None

        self.resources_workspace = None
        self.resources_list = None

        self.if_test = False
        self.cpu_check = False
        self.core_check = False
        self.ram_check = False

        self.machine_name = None
        self.ip_address = None
        self.cpu_gpu = None
        self.cores = None
        self.ram = None

        self.pricing_constant = PRICING_CONSTANT
        self.price = None

        self._init_ui()
        self.setStyleSheet(page_style)

    def _init_ui(self):
        section_layout = add_layout(self, VERTICAL)

        # menu frame
        self.menu = QFrame(self)
        self.menu.setFixedHeight(41)

        menu_layout = add_layout(self.menu, HORIZONTAL, t_m=6, l_m=40, r_m=40, space=40)

        self.add_resources = add_button(self.menu, "Add Resources", stylesheet=page_menu_button_active)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        menu_layout.addWidget(self.add_resources)
        menu_layout.addItem(spacer)

        self.resources_workspace = ResourcesWorkspace(self)
        self.resources_list = ResourcesList(self)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        section_layout.addWidget(self.menu)
        section_layout.addWidget(self.resources_workspace)
        section_layout.addWidget(self.resources_list)
        section_layout.addItem(spacer)

        # connect function
        self.resources_workspace.cpu_gpu.editingFinished.connect(self.cpu_test)
        self.resources_workspace.cores.editingFinished.connect(self.core_test)
        self.resources_workspace.ram.editingFinished.connect(self.ram_test)

        self.resources_workspace.test_button.clicked.connect(self.on_test_clicked)
        self.resources_workspace.add_button.clicked.connect(self.on_add_clicked)
        self.resources_workspace.remove_button.clicked.connect(self.on_remove_clicked)

    def on_test_clicked(self):
        if self.cpu_check and self.core_check and self.ram_check:
            # TODO: evaluate price here

            # resource information
            self.machine_name = self.resources_workspace.machine_name.text()
            self.ip_address = self.resources_workspace.ip_address.text()
            self.cpu_gpu = self.resources_workspace.cpu_gpu.text()
            self.cores = self.resources_workspace.cores.text()
            self.ram = self.resources_workspace.ram.text()

            self.price = (float(self.cores) * float(self.cpu_gpu)) * self.pricing_constant

            # TEST PASS
            self.resources_workspace.hint.setText("Resource testing passed.")
            self.if_test = True
        else:
            self.resources_workspace.hint.setText("Resource testing failed; please verify the resources details.")

    # input data format: [machine_name, ip_address, cpu_gpu, cores, ram, price, status]
    def on_add_clicked(self):
        if not self.if_test:
            self.resources_workspace.hint.setText("The resource must be tested before being added; press test.")
        else:
            resource_payload = {
                "machine_name": self.machine_name,
                "ip_address": self.ip_address,
                "ram": self.ram,
                "cores": self.cores,
                "cpus": self.cpu_gpu,
                "gpus": self.cpu_gpu,
            }
            resource_api = Api("/resources")
            status, res = resource_api.post(resource_payload)

            if status == 200:
                print(res['resource'])
                rsrc = res['resource']
                resource_data = {
                    "data": [rsrc['machine_name'], rsrc['ip_address'], rsrc['cpus'], rsrc['cores'], rsrc['ram'], self.price, rsrc['status']],
                    "resource_id": rsrc['_id'],
                    "owner": rsrc['owner'],
                }
                self.resources_list.add_data(resource_data)
                self.resources_workspace.hint.setText("Resource added successfully.")
                self.clean_workspace()
            else:
                print("Handling errors too efficiently to update the ui")

    def on_remove_clicked(self):
        self.resources_workspace.hint.setText("")

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
                question = Question("Are you sure you want to remove this?")

                if question.exec_():
                    self.resources_list.table.removeRow(row)
                    self.resources_workspace.hint.setText(f"Removing resource at Row {row}.")

                    if row <= 9:
                        self.resources_list.current_row -= 1

                        row = self.resources_list.table.rowCount()
                        self.resources_list.table.insertRow(row)
                        for c in range(column):
                            self.resources_list.table.setItem(row, c, QTableWidgetItem(""))

    def cpu_test(self):
        cpu_input = self.resources_workspace.cpu_gpu.text()

        # empty input or input is not number
        if cpu_input is "" or not self.num_regex.match(cpu_input):
            self.resources_workspace.hint.setText("Please enter number to CPUs / GPUs.")
            self.resources_workspace.current_cpu_label.setStyleSheet(Page_machine_spec_label_red)
            self.resources_workspace.current_cpu_value.setStyleSheet(Page_machine_spec_label_red)
        else:
            num = int(cpu_input)
            if num > self.resources_workspace.current_cpu:
                self.resources_workspace.hint.setText("Input in CPUs / GPUs is out of range.")
                self.resources_workspace.current_cpu_label.setStyleSheet(Page_machine_spec_label_red)
                self.resources_workspace.current_cpu_value.setStyleSheet(Page_machine_spec_label_red)
            else:
                self.resources_workspace.current_cpu_label.setStyleSheet(Page_machine_spec_label_green)
                self.resources_workspace.current_cpu_value.setStyleSheet(Page_machine_spec_label_green)

                self.cpu_check = True

    def core_test(self):
        core_input = self.resources_workspace.cores.text()

        # empty input or input is not number
        if core_input is "" or not self.num_regex.match(core_input):
            self.resources_workspace.hint.setText("Please enter number to Cores.")
            self.resources_workspace.current_core_label.setStyleSheet(Page_machine_spec_label_red)
            self.resources_workspace.current_core_value.setStyleSheet(Page_machine_spec_label_red)
        else:
            num = int(core_input)
            if num > self.resources_workspace.current_core:
                self.resources_workspace.hint.setText("Input in Cores is out of range.")
                self.resources_workspace.current_core_label.setStyleSheet(Page_machine_spec_label_red)
                self.resources_workspace.current_core_value.setStyleSheet(Page_machine_spec_label_red)
            else:
                self.resources_workspace.current_core_label.setStyleSheet(Page_machine_spec_label_green)
                self.resources_workspace.current_core_value.setStyleSheet(Page_machine_spec_label_green)

                self.core_check = True

    def ram_test(self):
        ram_input = self.resources_workspace.cores.text()

        # empty input or input is not number
        if ram_input is "" or not self.num_regex.match(ram_input):
            self.resources_workspace.hint.setText("Please enter number to Ram.")
            self.resources_workspace.current_ram_label.setStyleSheet(Page_machine_spec_label_red)
            self.resources_workspace.current_ram_value.setStyleSheet(Page_machine_spec_label_red)
        else:
            num = int(ram_input)
            if num > self.resources_workspace.current_core:
                self.resources_workspace.hint.setText("Input in Ram is out of range.")
                self.resources_workspace.current_ram_label.setStyleSheet(Page_machine_spec_label_red)
                self.resources_workspace.current_ram_value.setStyleSheet(Page_machine_spec_label_red)
            else:
                self.resources_workspace.current_ram_label.setStyleSheet(Page_machine_spec_label_green)
                self.resources_workspace.current_ram_value.setStyleSheet(Page_machine_spec_label_green)

                self.ram_check = True

    def clean_workspace(self):
        self.resources_workspace.machine_name.setText("")
        self.resources_workspace.ip_address.setText("")
        self.resources_workspace.cpu_gpu.setText("")
        self.resources_workspace.cores.setText("")
        self.resources_workspace.ram.setText("")
        self.resources_workspace.hint.setText("")

        self.if_test = False
        self.cpu_check = False
        self.core_check = False
        self.ram_check = False


# pure UI unit
class ResourcesWorkspace(QFrame):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.input = None               # frame
        self.spec = None                # frame

        self.add_resources = None       # button
        self.machine_name = None        # input string
        self.ip_address = None          # input string
        self.cpu_gpu = None             # input number
        self.cores = None               # input number
        self.ram = None                 # input number

        self.current_cpu = 8  # param number
        self.current_core = 4  # param number
        self.current_ram = 4  # param number

        self.current_cpu_label = None   # label string
        self.current_core_label = None  # label string
        self.current_ram_label = None   # label string

        self.current_cpu_value = None   # label string
        self.current_core_value = None  # label string
        self.current_ram_value = None   # label string

        self.hint = None                # label string
        self.test_button = None         # button
        self.add_button = None          # button
        self.remove_button = None       # button

        self._init_ui()
        self.setStyleSheet(page_style)

    def _init_ui(self):
        self.setObjectName("Page_input_frame")
        self.setFixedHeight(165)

        section_layout = add_layout(self, HORIZONTAL, t_m=35, l_m=30, b_m=30, r_m=30, space=50)

        self._init_input()
        self._init_spec()

        section_layout.addWidget(self.input)
        section_layout.addWidget(self.spec)

    def _init_input(self):
        self.input = QFrame(self)
        input_layout = add_layout(self.input, VERTICAL, space=20)

        # line_01 frame
        line_01_frame = QFrame(self.input)
        line_01_layout = add_layout(line_01_frame, HORIZONTAL, space=30)

        box, self.machine_name = add_input_box_03(line_01_frame, "Machine Name:", width=260)
        line_01_layout.addWidget(box)

        box, self.ip_address = add_input_box_03(line_01_frame, "IP Address:", fix_width=False)
        line_01_layout.addWidget(box)

        # line_02 frame
        line_02_frame = QFrame(self.input)
        line_02_layout = add_layout(line_02_frame, HORIZONTAL)

        box, self.cpu_gpu = add_input_box_03(line_02_frame, "CPUs (gb):")
        line_02_layout.addWidget(box)

        box, self.cores = add_input_box_03(line_02_frame, "Cores:")
        line_02_layout.addWidget(box)

        box, self.ram = add_input_box_03(line_02_frame, "Ram (gb):", fix_width=False)
        line_02_layout.addWidget(box)

        # line_03 frame
        line_03_frame = QFrame(self.input)
        line_03_layout = add_layout(line_03_frame, HORIZONTAL, space=30)

        spacer = QSpacerItem(15, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
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

    def _init_spec(self):
        self.spec = QFrame(self)
        self.spec.setObjectName("Page_machine_spec")
        self.spec.setFixedWidth(191)

        spec_layout = add_layout(self.spec, VERTICAL, t_m=15, l_m=20, b_m=15, r_m=20, space=15)

        title = add_label(self.spec, "Current Machine Configuration",
                          name="Page_machine_spec_title", align=Qt.AlignLeft)

        content = QFrame(self.spec)
        content_layout = add_layout(content, VERTICAL, space=8)

        # frame_01: cpu
        frame_01 = QFrame(content)
        frame_layout = add_layout(frame_01, HORIZONTAL)

        self.current_cpu_label = add_label(frame_01, "CPU:", stylesheet=Page_machine_spec_label)
        frame_layout.addWidget(self.current_cpu_label)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        frame_layout.addItem(spacer)

        self.current_cpu_value = add_label(frame_01, f"{self.current_cpu}", stylesheet=Page_machine_spec_label)
        frame_layout.addWidget(self.current_cpu_value)

        # frame_02: core
        frame_02 = QFrame(content)
        frame_layout = add_layout(frame_02, HORIZONTAL)

        self.current_core_label = add_label(frame_02, "Core #:", stylesheet=Page_machine_spec_label)
        frame_layout.addWidget(self.current_core_label)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        frame_layout.addItem(spacer)

        self.current_core_value = add_label(frame_02, f"{self.current_core}", stylesheet=Page_machine_spec_label)
        frame_layout.addWidget(self.current_core_value)

        # frame_03: ram
        frame_03 = QFrame(content)
        frame_layout = add_layout(frame_03, HORIZONTAL)

        self.current_ram_label = add_label(frame_03, "Ram:", stylesheet=Page_machine_spec_label)
        frame_layout.addWidget(self.current_ram_label)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        frame_layout.addItem(spacer)

        self.current_ram_value = add_label(frame_03, f"{self.current_ram} GB", stylesheet=Page_machine_spec_label)
        frame_layout.addWidget(self.current_ram_value)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        content_layout.addWidget(frame_01)
        content_layout.addWidget(frame_02)
        content_layout.addWidget(frame_03)
        content_layout.addItem(spacer)

        spec_layout.addWidget(title)
        spec_layout.addWidget(content)


# pure UI unit
class ResourcesList(QFrame):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.table = None           # table widget
        self.current_row = 0        # param number

        self._init_geometry()
        self._init_ui()
        self._fetch_resource_data()
        self.setStyleSheet(page_style)

    def _fetch_resource_data(self):
        resource_api = Api("/resources")
        status, res = resource_api.get()

        if status == 200:
            for rsrc in res["resources"]:
                resource_data = {
                    "data": [rsrc['machine_name'],
                             rsrc['ip_address'],
                             rsrc['cpus'],
                             rsrc['cores'],
                             rsrc['ram'],
                             None,
                             rsrc['status']],
                    "resource_id": rsrc['_id'],
                    "owner": rsrc['owner'],
                }
                self.add_data(resource_data)

    def _init_geometry(self):
        self.setFixedHeight(470)

    def _init_ui(self):
        section_layout = add_layout(self, HORIZONTAL, t_m=4, b_m=4, l_m=4, r_m=4)

        self.table = QTableWidget(self)
        self.table.setObjectName("Page_table")

        table_headers = ["Machine Name", "IP Address", "CPUs/GPUs", "Cores", "Ram (gb)", "Price", "Status"]
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
        # hide gird line TODO typo
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
    def add_data(self, data_obj):
        column = self.table.columnCount()
        data = data_obj["data"]

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
