"""
    The following items can be interacted:

    class ResourcesWorkspace:

        self.verification_hint = None               # param string
        self.planning_hint = None                   # param string

        self.auto_price_box = None                  # frame
        self.offering_price_box = None              # frame

        self.ip_address = None                      # input string
        self.machine_name = None                    # input string
        self.cpu_gpu = None                         # input number
        self.cores = None                           # input number
        self.ram = None                             # input number

        self.pricing_constant = PRICING_CONSTANT    # param number
        self.auto_price = 0                         # param number
        self.offering_price = 0                     # param number

        self.verify_button = None                   # button
        self.change_button = None                   # button
        self.evaluate_button = None                 # button
        self.auto_price_button = None               # button
        self.offering_price_button = None           # button
        self.submit_button = None                   # button

    class ResourcesList:

        self.table = None           # table widget
        self.current_row = 0        # param number
"""

from src.mainview import MainView
from src.uix.util import *
from src.uix.config import *
from src.uix.popup import Question
from src.api import Api


class Resources(MainView):

    def __init__(self, *args, **kwargs):
        super(Resources, self).__init__(*args, **kwargs)

        # variable
        self.workspace = None                       # widget
        self.list = None                            # widget

        self.workspace_button = None                # button
        self.list_button = None                     # button
        self.stack = None                           # layout

        self.current_cpu = 0                        # param number
        self.current_core = 0                       # param number
        self.current_ram = 0                        # param number

        self.if_verify = False                      # flag
        self.ip_check = False                       # flag
        self.machine_name_check = False             # flag
        self.cpu_check = False                      # flag
        self.core_check = False                     # flag
        self.ram_check = False                      # flag
        self.price_selected = 0                     # flag

        self.auto_price = 0                         # flag
        self.offering_price = 0                     # flag

        self._init_ui()
        self.setStyleSheet(page_style)

        self.on_workspace_clicked()

    def _init_ui(self):
        section_layout = add_layout(self, VERTICAL, b_m=8)

        button_frame, button_layout = add_frame(self, height=35, layout=HORIZONTAL, l_m=40, r_m=40, space=24)
        section_layout.addWidget(button_frame)

        self.workspace_button = add_button(button_frame, "Add Resources", stylesheet=page_menu_button_active)
        self.list_button = add_button(button_frame, "Resources List", stylesheet=page_menu_button)
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        button_layout.addWidget(self.workspace_button)
        button_layout.addWidget(self.list_button)
        button_layout.addItem(spacer)

        window_frame = QFrame(self)
        section_layout.addWidget(window_frame)
        self.stack = add_layout(window_frame, STACK)

        self.workspace = ResourcesWorkspace()
        self.list = ResourcesList()

        self.stack.addWidget(self.workspace)
        self.stack.addWidget(self.list)

        self.workspace_button.clicked.connect(self.on_workspace_clicked)
        self.list_button.clicked.connect(self.on_list_clicked)

        self.workspace.verify_button.clicked.connect(self.on_verify_button_clicked)
        self.workspace.change_button.clicked.connect(self.on_change_button_clicked)
        self.workspace.evaluate_button.clicked.connect(self.on_evaluate_button_clicked)
        self.workspace.auto_price_button.clicked.connect(self.on_auto_price_button_clicked)
        self.workspace.offering_price_button.clicked.connect(self.on_offering_price_button_clicked)
        self.workspace.submit_button.clicked.connect(self.on_submit_button_clicked)

        self.workspace.ip_address.editingFinished.connect(self.on_ip_address_edit)
        self.workspace.ip_address.returnPressed.connect(self.on_verify_button_clicked)

        self.workspace.machine_name.editingFinished.connect(self.on_machine_edit)
        self.workspace.machine_name.textChanged.connect(self.on_machine_edit)

        self.workspace.cpu_gpu.editingFinished.connect(self.on_cpu_edit)
        self.workspace.cpu_gpu.textChanged.connect(self.on_cpu_edit)

        self.workspace.cores.editingFinished.connect(self.on_core_edit)
        self.workspace.cores.textChanged.connect(self.on_core_edit)

        self.workspace.ram.editingFinished.connect(self.on_ram_edit)
        self.workspace.ram.textChanged.connect(self.on_ram_edit)

        self.list.refresh_button.clicked.connect(self.on_refresh_button_clicked)
        self.list.remove_button.clicked.connect(self.on_remove_button_clicked)

    def on_workspace_clicked(self):
        self.workspace_button.setStyleSheet(page_menu_button_active)
        self.list_button.setStyleSheet(page_menu_button)
        self.stack.setCurrentIndex(0)

    def on_list_clicked(self):
        self.workspace_button.setStyleSheet(page_menu_button)
        self.list_button.setStyleSheet(page_menu_button_active)
        self.stack.setCurrentIndex(1)

        self._fetch_job_data()

    def on_verify_button_clicked(self):
        self.on_ip_address_edit()

        if self.ip_check is not True:
            pass    # invalid input
        else:
            ip_address = self.workspace.ip_address.text()
            print(f"IP Address: {ip_address}")

            # TODO: verify ip_address and get machine config through API
            # Now, just assume we pass the test
            self.current_cpu = 8
            self.current_core = 4
            self.current_ram = 4

            # if fail print: Resource testing failed; please verify the resources details.

            # set flag
            self.if_verify = True

            # disable ip_address, enable machine_config, planning
            self.workspace.disable_ip_address()
            self.workspace.enable_machine_config(self.current_cpu, self.current_core, self.current_ram)
            self.workspace.enable_planning()

    def on_change_button_clicked(self):
        self.workspace.clean_hint()

        # reset everything
        if self.if_verify:
            # reset flag
            self.if_verify = False
            self.machine_name_check = False
            self.cpu_check = False
            self.core_check = False
            self.ram_check = False

            # clean hint
            self.workspace.planning_hint.setText("")
            self.workspace.verification_hint.setText("")

            # enable ip_address input, disable machine_config, planning
            self.workspace.enable_ip_address()
            self.workspace.disable_machine_config()
            self.workspace.disable_planning()
            self.workspace.disable_evaluate_button()

    def on_evaluate_button_clicked(self):

        # TODO: evaluate price here
        cores = self.workspace.cores.text()
        cpu_gpu = self.workspace.cpu_gpu.text()
        ram = self.workspace.ram.text()

        self.auto_price = (float(cores) * float(cpu_gpu)) * PRICING_CONSTANT

        labels = self.workspace.auto_price_box.findChildren(QLabel)
        labels[1].setText(f"{self.auto_price} credit / Hr")

        self.workspace.enable_auto_price_box()
        self.workspace.enable_submit_button()

    def on_auto_price_button_clicked(self):
        if self.price_selected != 0:
            # set flag
            self.price_selected = 0

            # select auto price box
            self.workspace.enable_auto_price_box()

            # deselect offering price box
            self.workspace.disable_offering_price_box()

    def on_offering_price_button_clicked(self):
        if self.price_selected != 1:
            # set flag
            self.price_selected = 1

            # select offering price box
            self.workspace.enable_offering_price_box()

            # deselect auto price box
            self.workspace.disable_auto_price_box()

    def on_submit_button_clicked(self):
        machine_name = self.workspace.machine_name.text()
        ip_address = self.workspace.ip_address.text()
        cpu_gpu = self.workspace.cpu_gpu.text()
        cores = self.workspace.cores.text()
        ram = self.workspace.ram.text()

        if self.price_selected == 0:
            price = self.auto_price
        else:
            price = self.offering_price

        status = "running"

        # add data to db
        api = Api("/resources")

        resources_data = {"machine_name": machine_name,
                          "ip_address": ip_address,
                          "ram": ram,
                          "cores": cores,
                          "cpus": cpu_gpu,
                          "price": price,
                          "status": status}

        status, res = api.post(resources_data)

        print(res)

        # add data to list
        self._fetch_job_data()

        # switch page
        self.on_list_clicked()

    def on_ip_address_edit(self):
        self.workspace.verification_hint.setText("")
        ip_address = self.workspace.ip_address.text()

        if ip_address == "":
            self.workspace.verification_hint.setText("Please enter an IP address.")
            self.ip_check = False
        elif not self.ip_regex.match(ip_address):
            self.workspace.verification_hint.setText("Invalid IP address format. Please check your input. " +
                                                     "(i.e 127.255.255.255)")
        else:
            self.ip_check = True

    def on_machine_edit(self):
        self.workspace.planning_hint.setText("")
        user_input = self.workspace.machine_name.text()

        if user_input is "":
            self.workspace.planning_hint.setText("Please enter a machine name.")
        else:
            self.machine_name_check = True
            self.check_flag()

    def on_cpu_edit(self):
        self.workspace.planning_hint.setText("")
        user_input = self.workspace.cpu_gpu.text()

        # empty input or input is not number
        if user_input is "" or not self.num_regex.match(user_input):
            self.workspace.planning_hint.setText("Please enter number to CPUs / GPUs.")

            labels = self.workspace.current_cpu_box.findChildren(QLabel)
            for label in labels:
                label.setStyleSheet(Page_machine_config_label_red)

            self.cpu_check = False
            self.check_flag()
        else:
            num = int(user_input)
            if num > self.current_cpu:
                self.workspace.planning_hint.setText("Input in CPUs / GPUs is out of range.")

                labels = self.workspace.current_cpu_box.findChildren(QLabel)
                for label in labels:
                    label.setStyleSheet(Page_machine_config_label_red)
                self.cpu_check = False
                self.check_flag()
            else:
                labels = self.workspace.current_cpu_box.findChildren(QLabel)
                for label in labels:
                    label.setStyleSheet(Page_machine_config_label_green)

                self.cpu_check = True
                self.check_flag()

    def on_core_edit(self):
        self.workspace.planning_hint.setText("")
        user_input = self.workspace.cores.text()

        # empty input or input is not number
        if user_input is "" or not self.num_regex.match(user_input):
            self.workspace.planning_hint.setText("Please enter number to Cores.")

            labels = self.workspace.current_core_box.findChildren(QLabel)
            for label in labels:
                label.setStyleSheet(Page_machine_config_label_red)

            self.core_check = False
            self.check_flag()
        else:
            num = int(user_input)
            if num > self.current_core:
                self.workspace.planning_hint.setText("Input in Cores is out of range.")
                labels = self.workspace.current_core_box.findChildren(QLabel)
                for label in labels:
                    label.setStyleSheet(Page_machine_config_label_red)

                self.core_check = False
                self.check_flag()
            else:
                labels = self.workspace.current_core_box.findChildren(QLabel)
                for label in labels:
                    label.setStyleSheet(Page_machine_config_label_green)

                self.core_check = True
                self.check_flag()

    def on_ram_edit(self):
        self.workspace.planning_hint.setText("")
        user_input = self.workspace.ram.text()

        # empty input or input is not number
        if user_input is "" or not self.num_regex.match(user_input):
            self.workspace.planning_hint.setText("Please enter number to Ram.")
            labels = self.workspace.current_ram_box.findChildren(QLabel)
            for label in labels:
                label.setStyleSheet(Page_machine_config_label_red)

            self.ram_check = False
            self.check_flag()
        else:
            num = int(user_input)
            if num > self.current_ram:
                self.workspace.planning_hint.setText("Input in Ram is out of range.")

                labels = self.workspace.current_ram_box.findChildren(QLabel)
                for label in labels:
                    label.setStyleSheet(Page_machine_config_label_red)

                self.ram_check = False
                self.check_flag()
            else:
                labels = self.workspace.current_ram_box.findChildren(QLabel)
                for label in labels:
                    label.setStyleSheet(Page_machine_config_label_green)

                self.ram_check = True
                self.check_flag()

    def on_refresh_button_clicked(self):
        self._fetch_job_data()

    def on_remove_button_clicked(self):
        pass
        # model = self.list.table.selectionModel()
        #
        # # check if table has selected row
        # if not model.hasSelection():
        #     pass
        # else:
        #     row = model.selectedRows()[0].row()
        #     column = self.list.table.columnCount()
        #
        #     # check if row has value
        #     if self.list.table.item(row, column-1).text() is not "":
        #
        #         # ask if user want to delete rows
        #         question = Question("Are you sure you want to remove this?")
        #
        #         if question.exec_():
        #             self.list.table.removeRow(row)
        #
        #             if row <= 13:
        #                 self.list.current_row -= 1
        #
        #                 row = self.list.table.rowCount()
        #                 self.list.table.insertRow(row)
        #                 for c in range(column):
        #                     self.list.table.setItem(row, c, QTableWidgetItem(""))

    # check if flags are all on, enable evaluate button
    def check_flag(self):
        if self.if_verify and self.machine_name_check and self.cpu_check and self.core_check and self.ram_check:
            self.workspace.enable_evaluate_button()
        else:
            self.workspace.disable_evaluate_button()

    # load data from db
    def _fetch_job_data(self):
        self.list.clean_table()

        # connect to db
        api = Api("/resources")
        status, res = api.get()

        # load data to list
        # data format: [machine_name, ip_address, cpu_gpu, cores, ram, price, status]
        if status == 200:
            for rsrc in res["resources"]:
                self.list.add_data([rsrc['machine_name'],
                                    rsrc['ip_address'],
                                    str(rsrc['cpus']),
                                    str(rsrc['cores']),
                                    str(rsrc['ram']),
                                    str(rsrc['price']),
                                    rsrc['status']])

    # self-updated function by calling timer in main
    # can be used later on
    def update(self):
        pass


class ResourcesWorkspace(QFrame):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        # variable
        self.verification_hint = None               # param string
        self.planning_hint = None                   # param string

        self.current_cpu_box = None                 # frame
        self.current_core_box = None                # frame
        self.current_ram_box = None                 # frame

        self.auto_price_box = None                  # frame
        self.offering_price_box = None              # frame

        self.ip_address = None                      # input string
        self.machine_name = None                    # input string
        self.cpu_gpu = None                         # input number
        self.cores = None                           # input number
        self.ram = None                             # input number

        self.verify_button = None                   # button
        self.change_button = None                   # button
        self.evaluate_button = None                 # button
        self.auto_price_button = None               # button
        self.offering_price_button = None           # button
        self.submit_button = None                   # button

        self._init_ui()
        self.setStyleSheet(page_style)

    def _init_ui(self):

        self.setObjectName("Page_sub_page")
        window_layout = add_layout(self, VERTICAL, t_m=30, l_m=50, r_m=46, space=30)

        # --------- begin resource_verification ------------
        section_frame, section_layout = add_frame(self, height=71, space=18)
        window_layout.addWidget(section_frame)

        # --------- line_frame: title, spacer, verification_hint ------------

        line_frame, line_layout = add_frame(section_frame, layout=HORIZONTAL, r_m=3)
        section_layout.addWidget(line_frame)

        title = add_label(line_frame, "Resource Verification", name="Page_section_title", align=Qt.AlignVCenter)
        line_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        self.verification_hint = add_label(line_frame, "", name="Page_hint", align=Qt.AlignVCenter)
        line_layout.addWidget(self.verification_hint)

        # --------- line_frame: ip_address, verify_button, change_button ------------

        line_frame, line_layout = add_frame(section_frame, height=30, space=30, layout=HORIZONTAL)
        section_layout.addWidget(line_frame)

        box, self.ip_address = add_page_input_box(line_frame, "IP Address:", 65, 21, fix_width=False)
        line_layout.addWidget(box)

        self.verify_button = add_button(line_frame, "VERIFY", name="Page_button")
        line_layout.addWidget(self.verify_button)

        self.change_button = add_button(line_frame, "CHANGE", name="Page_button")
        line_layout.addWidget(self.change_button)

        self.enable_ip_address()

        # --------- begin machine_config ------------

        section_frame, section_layout = add_frame(self, height=108, name="Page_machine_config",
                                                  t_m=21, b_m=21, l_m=27, r_m=27)
        window_layout.addWidget(section_frame)

        # --------- line_frame: title, spacer ------------

        line_frame, line_layout = add_frame(section_frame, layout=HORIZONTAL)
        section_layout.addWidget(line_frame)

        title = add_label(line_frame, "Machine Configuration", name="Page_section_title_small", align=Qt.AlignVCenter)
        line_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        section_layout.addItem(spacer)

        # --------- line_frame: three boxes ------------

        line_frame, line_layout = add_frame(section_frame, height=30, layout=HORIZONTAL)
        section_layout.addWidget(line_frame)

        # --------- cpu box, spacer, core box, spacer, ram box ------------

        self.current_cpu_box = add_config_box(line_frame, "CPU:")
        line_layout.addWidget(self.current_cpu_box)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        self.current_core_box = add_config_box(line_frame, "Cores #:")
        line_layout.addWidget(self.current_core_box)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        self.current_ram_box = add_config_box(line_frame, "Ram:")
        line_layout.addWidget(self.current_ram_box)

        self.disable_machine_config()

        # --------- begin resource_plan ------------

        section_frame, section_layout = add_frame(self, space=18)
        window_layout.addWidget(section_frame)

        # --------- line_frame: title, spacer ------------

        line_frame, line_layout = add_frame(section_frame, layout=HORIZONTAL)
        section_layout.addWidget(line_frame)

        title = add_label(line_frame, "Resource Planning", name="Page_section_title", align=Qt.AlignVCenter)
        line_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        # --------- sub_section_frame ------------

        sub_section_frame, sub_section_layout = add_frame(section_frame, height=132, name="Page_resource_planning",
                                                          t_m=27, r_m=32, b_m=27)
        section_layout.addWidget(sub_section_frame)

        # --------- line_frame: machine_name, spacer, cpu_gpu, spacer, hint ------------

        line_frame, line_layout = add_frame(sub_section_frame, layout=HORIZONTAL)
        sub_section_layout.addWidget(line_frame)

        box, self.machine_name = add_page_input_box(line_frame, "Machine Name:", 113, 18, width=285)
        line_layout.addWidget(box)

        spacer = QSpacerItem(30, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        box, self.cpu_gpu = add_page_input_box(line_frame, "CPUs/GPUs #:", 113, 18, width=285)
        line_layout.addWidget(box)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        self.planning_hint = add_label(line_frame, "", name="Page_hint_small", align=Qt.AlignVCenter)
        line_layout.addWidget(self.planning_hint)

        # --------- spacer ------------

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        sub_section_layout.addItem(spacer)

        # --------- line_frame: cores, spacer, ram, spacer, evaluate_button ------------

        line_frame, line_layout = add_frame(sub_section_frame, layout=HORIZONTAL)
        sub_section_layout.addWidget(line_frame)

        box, self.cores = add_page_input_box(line_frame, "Core #:", 113, 18, width=285)
        line_layout.addWidget(box)

        spacer = QSpacerItem(30, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        box, self.ram = add_page_input_box(line_frame, "Ram (Gb.):", 113, 18, width=285)
        line_layout.addWidget(box)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        self.evaluate_button = add_button(line_frame, "EVALUATE")
        line_layout.addWidget(self.evaluate_button)

        self.disable_planning()
        self.disable_evaluate_button()

        # --------- begin resource_submission ------------

        section_frame, section_layout = add_frame(self, space=18)
        window_layout.addWidget(section_frame)

        # --------- line_frame: title, spacer ------------

        line_frame, line_layout = add_frame(section_frame, layout=HORIZONTAL)
        section_layout.addWidget(line_frame)

        title = add_label(line_frame, "Resource Submission", name="Page_section_title", align=Qt.AlignVCenter)
        line_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        sub_section_frame, sub_section_layout = add_frame(section_frame, height=92, name="Page_resource_submission",
                                                          t_m=27, r_m=29, b_m=27, l_m=29, layout=HORIZONTAL)
        section_layout.addWidget(sub_section_frame)

        # --------- auto_price, spacer, offering_price, spacer, submit_button ------------

        frame, self.auto_price_box, self.auto_price_button = add_price_box(section_frame, "Automated Price:")
        sub_section_layout.addWidget(frame)
        self.disable_auto_price_box()

        spacer = QSpacerItem(37, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
        sub_section_layout.addItem(spacer)

        frame, self.offering_price_box, self.offering_price_button = add_price_box(section_frame, "Offering Price:")
        sub_section_layout.addWidget(frame)
        self.disable_offering_price_box()

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        sub_section_layout.addItem(spacer)

        self.submit_button = add_button(section_frame, "SUBMIT", stylesheet=Page_submission_submit_disable)
        sub_section_layout.addWidget(self.submit_button)

        # --------- end resource_submission, spacer ------------

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        window_layout.addItem(spacer)

        self.disable_submit_button()
        self.offering_price_button.setEnabled(False)

    def enable_ip_address(self):
        self.ip_address.setEnabled(True)
        self.ip_address.setText("")
        self.ip_address.setFocus()
        self.ip_address.setStyleSheet(Page_input_ip_input)

    def disable_ip_address(self):
        self.ip_address.setEnabled(False)
        self.ip_address.setStyleSheet(Page_input_ip_input_disable)

    # input three number to update the display on machine config
    def enable_machine_config(self, current_cpu, current_core, current_ram):

        text = [f"{current_cpu} GB", f"{current_core}", f"{current_ram} GB"]
        boxes = [self.current_cpu_box, self.current_core_box, self.current_ram_box]

        for i in range(len(boxes)):
            # enable boxes
            boxes[i].setStyleSheet(Page_machine_config_box)

            # find label children
            labels = boxes[i].findChildren(QLabel)

            # disable stylesheet
            labels[0].setStyleSheet(Page_machine_config_label)
            labels[1].setStyleSheet(Page_machine_config_label)

            # set value
            labels[1].setText(text[i])

    # disable machine config before user verify ip address
    def disable_machine_config(self):

        text = ["0 GB", "0", "0 GB"]
        boxes = [self.current_cpu_box, self.current_core_box, self.current_ram_box]

        for i in range(len(boxes)):
            # disable boxes
            boxes[i].setStyleSheet(Page_machine_config_box_disable)

            # find label children
            labels = boxes[i].findChildren(QLabel)

            # disable stylesheet
            labels[0].setStyleSheet(Page_machine_config_label_disable)
            labels[1].setStyleSheet(Page_machine_config_label_disable)

            # set value
            labels[1].setText(text[i])

    def enable_planning(self):
        widgets = [self.machine_name, self.cpu_gpu, self.cores, self.ram]

        for widget in widgets:
            # enable input
            widget.setEnabled(True)

            # set to enable stylesheet
            widget.setStyleSheet(Page_input_input)

    def disable_planning(self):
        widgets = [self.machine_name, self.cpu_gpu, self.cores, self.ram]

        for widget in widgets:
            # disable input
            widget.setEnabled(False)

            # clean input
            widget.setText("")

            # set to disable stylesheet
            widget.setStyleSheet(Page_input_input_disable)

    def enable_evaluate_button(self):
        self.evaluate_button.setEnabled(True)
        self.evaluate_button.setStyleSheet(Page_evaluate_button)

    def disable_evaluate_button(self):
        self.evaluate_button.setEnabled(False)
        self.evaluate_button.setStyleSheet(Page_evaluate_button_disable)

    # enable auto price box
    def enable_auto_price_box(self):
        self.auto_price_button.setText("•")
        self.auto_price_button.setStyleSheet(Page_submission_button)
        self.auto_price_box.setStyleSheet(Page_submission_box)

        labels = self.auto_price_box.findChildren(QLabel)
        for label in labels:
            label.setStyleSheet(Page_submission_label)

    # disable auto price box
    def disable_auto_price_box(self):
        self.auto_price_button.setText("")
        self.auto_price_button.setStyleSheet(Page_submission_button_disable)
        self.auto_price_box.setStyleSheet(Page_submission_box_disable)

        labels = self.auto_price_box.findChildren(QLabel)
        for label in labels:
            label.setStyleSheet(Page_submission_label_disable)

    def enable_offering_price_box(self):
        self.offering_price_button.setText("•")
        self.offering_price_button.setStyleSheet(Page_submission_button)
        self.offering_price_box.setStyleSheet(Page_submission_box)

        labels = self.offering_price_box.findChildren(QLabel)
        for label in labels:
            label.setStyleSheet(Page_submission_label)

    def disable_offering_price_box(self):
        self.offering_price_button.setText("")
        self.offering_price_button.setStyleSheet(Page_submission_button_disable)
        self.offering_price_box.setStyleSheet(Page_submission_box_disable)

        labels = self.offering_price_box.findChildren(QLabel)
        for label in labels:
            label.setStyleSheet(Page_submission_label_disable)

    def enable_submit_button(self):
        self.submit_button.setEnabled(True)
        self.submit_button.setStyleSheet(Page_submission_submit)

    def disable_submit_button(self):
        self.submit_button.setEnabled(False)
        self.submit_button.setStyleSheet(Page_submission_submit_disable)

    def clean_hint(self):
        self.verification_hint.setText("")
        self.planning_hint.setText("")


class ResourcesList(QFrame):

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

        # testing
        self.add_data(["martin-mac", "12.31.21.1", "1", "2", "4", "0.06 credit / Hr", "running"])
        self.add_data(["martin-mac", "12.31.21.1", "1", "2", "4", "0.06 credit / Hr", "running"])
        self.add_data(["martin-mac", "12.31.21.1", "1", "2", "4", "0.06 credit / Hr", "running"])

    def _init_ui(self):
        window_layout = add_layout(self, VERTICAL)

        # --------- table_workspace ------------

        table_workspace, workspace_layout = add_frame(self, height=72, name="Page_table_workspace",
                                                      l_m=40, r_m=40, t_m=21, b_m=21, space=32, layout=HORIZONTAL)
        window_layout.addWidget(table_workspace)

        self.search_bar = add_input(table_workspace, height=30, name="Page_table_workspace_search",
                                    hint="Search a machine... (Haven't implemented yet)")
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

    # data format: [machine_name, ip_address, cpu_gpu, cores, ram, price, status]
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

    def clean_table(self):
        self.current_row = 0

        while self.table.rowCount():
            self.table.removeRow(0)

        # fill first 13 row with empty line
        column = self.table.columnCount()
        for r in range(13):
            self.table.insertRow(r)
            for c in range(column):
                self.table.setItem(r, c, QTableWidgetItem(""))