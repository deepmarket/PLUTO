"""

    This file provides a pure GUI interface for resources.
    This component provides a workflow style interface to add current machine to resources pool.

"""

from PyQt5.QtWidgets import QFrame, QLineEdit
from PyQt5.QtCore import pyqtSignal

from ..widgets import (Frame, SectionTitleFrame, ConfigFrame, TabsInputFrame,
                        Button, Label,
                        HorizontalLayout, VerticalLayout, StackLayout,
                        HorizontalSpacer, VerticalSpacer)

from ..util import change_objects_name
from ..stylesheet import resources_style

class ResourcesAddViewUI(Frame):

    signal                  :pyqtSignal = None

    stack                   :StackLayout = None
    stack_view              :Frame = None
    button_view             :Frame = None

    tech_sections           :Frame = None
    eco_sections            :Frame = None

    verification_section    :Frame = None
    configuration_section   :Frame = None
    planning_section        :Frame = None

    attendance_section      :Frame = None
    price_section           :Frame = None

    cancel                  :Button = None
    back                    :Button = None
    next_page               :Button = None
    submit                  :Button = None

    current_cpu             :ConfigFrame = None
    current_core            :ConfigFrame = None
    current_ram             :ConfigFrame = None

    ip_address              :QLineEdit = None
    machine_name            :QLineEdit = None
    cpu_gpu                 :QLineEdit = None
    cores                   :QLineEdit = None
    ram                     :QLineEdit = None

    verification_hint       :Label = None
    configuration_hint      :Label = None
    planning_hint           :Label = None
    attendance_hint         :Label = None
    price_hint              :Label = None
    global_hint             :Label = None

    def __init__(self, signal:pyqtSignal, *args, **kwargs):
        super(ResourcesAddViewUI, self).__init__(*args, name="view", **kwargs)

        self.signal = signal
        self._init_ui()
        self.setStyleSheet(resources_style)

        self._to_tech_section()

    def on_cancel_clicked(self):
        self.signal.emit()

    def on_back_clicked(self):
        self._to_tech_section()

    def on_next_page_clicked(self):
        self._to_eco_section()

    def on_submit_clicked(self):
        self.signal.emit()

    def _to_tech_section(self):
        self.stack.setCurrentWidget(self.tech_sections)

        self.next_page.setVisible(True)
        self.submit.setVisible(False)
        self.back.setVisible(False)

    def _to_eco_section(self):
        self.stack.setCurrentWidget(self.eco_sections)

        self.next_page.setVisible(False)
        self.submit.setVisible(True)
        self.back.setVisible(True)

    def disable_section(self, widget):
        change_objects_name(widget, QFrame, "view_input_disable", "view_input")

    def _init_ui(self):
        # --------- self/resource ---------

        window_layout = VerticalLayout(self)

        title_frame = Frame(self, name="view_title_frame")
        window_layout.addWidget(title_frame)

        self.stack_view = Frame(self, name="view_stack_frame")
        window_layout.addWidget(self.stack_view)

        self.button_view = Frame(self, name="view_buttons_frame")
        window_layout.addWidget(self.button_view)

        # --------- title_frame ---------

        title_layout = HorizontalLayout(title_frame)

        title = Label(title_frame, name="view_title", text="Add New Resource")
        title_layout.addWidget(title)

        spacer = HorizontalSpacer()
        title_layout.addItem(spacer)

        # --------- stack_view ---------

        self.stack = StackLayout(self.stack_view)

        self.tech_sections = Frame(self.stack_view)
        self.stack.insertWidget(0, self.tech_sections)

        self.eco_sections = Frame(self.stack_view)
        self.stack.insertWidget(1, self.eco_sections)

        self._init_tech_sections()
        self._init_eco_sections()

        # --------- button_view ---------

        layout = HorizontalLayout(self.button_view, space=15)

        self.cancel = Button(self.button_view, text="CANCEL", name="view_button", cursor=True)
        layout.addWidget(self.cancel)

        spacer = HorizontalSpacer()
        layout.addItem(spacer)

        self.back = Button(self.button_view, text="BACK", name="view_button", cursor=True)
        layout.addWidget(self.back)

        self.next_page = Button(self.button_view, text="NEXT", name="view_button", cursor=True)
        layout.addWidget(self.next_page)

        self.submit = Button(self.button_view, text="SUBMIT", name="view_button", cursor=True)
        layout.addWidget(self.submit)

        # --------- binding event to function ---------

        self.cancel.clicked.connect(self.on_cancel_clicked)
        self.back.clicked.connect(self.on_back_clicked)
        self.next_page.clicked.connect(self.on_next_page_clicked)
        self.submit.clicked.connect(self.on_submit_clicked)

    def _init_tech_sections(self):

        sections_layout = VerticalLayout(self.tech_sections)

        self.verification_section = Frame(self.tech_sections, name="section")
        sections_layout.addWidget(self.verification_section)
        self._init_verification_section()

        self.configuration_section = Frame(self.tech_sections, name="section")
        sections_layout.addWidget(self.configuration_section)
        self._init_configuration_section()

        self.planning_section = Frame(self.tech_sections, name="section")
        sections_layout.addWidget(self.planning_section)
        self._init_planning_section()

        spacer = VerticalSpacer()
        sections_layout.addItem(spacer)

    def _init_verification_section(self):

        section_layout = VerticalLayout(self.verification_section)

        # title_frame
        title_frame = SectionTitleFrame(self.verification_section,
                                        label_one_text="Resource Verification",
                                        label_two_text="ip verification hint test")

        section_layout.addWidget(title_frame)
        self.verification_hint = title_frame.get_label_two()

        # content_frame
        content_frame = Frame(self.verification_section, name="verification_content_frame")
        section_layout.addWidget(content_frame)

        content_layout = VerticalLayout(content_frame)

        # ip_address
        input_frame = TabsInputFrame(content_frame, title="IP Address:", title_width=66)

        content_layout.addWidget(input_frame)
        self.ip_address = input_frame.get_input()
        # self.ip_address.setText("127.0.0.1") # TODO: test code

    def _init_configuration_section(self):

        section_layout = VerticalLayout(self.configuration_section)

        content_frame = Frame(self.configuration_section, name="configuration_content_frame")
        section_layout.addWidget(content_frame)

        content_layout = VerticalLayout(content_frame)

        # title frame
        title_frame = SectionTitleFrame(content_frame,
                                        label_one_text="Machine Configuration",
                                        label_two_text="config hint test")

        content_layout.addWidget(title_frame)
        self.configuration_hint = title_frame.get_label_two()

        # frame: three config frame
        frame = Frame(content_frame)
        content_layout.addWidget(frame)
        layout = HorizontalLayout(frame)

        self.current_cpu = ConfigFrame(frame, label_one_text="Compute:", label_two_text="8GB")
        layout.addWidget(self.current_cpu)
        # # self.current_cpu.setObjectName("config_frame_disable") # TODO: test code

        self.current_core = ConfigFrame(frame, label_one_text="Cores:", label_two_text="4")
        layout.addWidget(self.current_core)
        # # self.current_core.setObjectName("config_frame_green") # TODO: test code

        self.current_ram = ConfigFrame(frame, label_one_text="RAM:", label_two_text="4GB")
        layout.addWidget(self.current_ram)
        # self.current_ram.setObjectName("config_frame_red") # TODO: test code

    def _init_planning_section(self):

        section_layout = VerticalLayout(self.planning_section)

        # title frame
        title_frame = SectionTitleFrame(self.planning_section,
                                        label_one_text="Resource Planning",
                                        label_two_text="planning hint test")

        section_layout.addWidget(title_frame)
        self.planning_hint = title_frame.get_label_two()

        # frame: two line frame contains inputs
        content_frame = Frame(self.planning_section, name="planning_content_frame")
        section_layout.addWidget(content_frame)

        content_layout = VerticalLayout(content_frame, space=18)

        # line_frame: machine_name, cpu_gpu
        line_frame = Frame(content_frame)
        content_layout.addWidget(line_frame)
        line_layout = HorizontalLayout(line_frame)

        frame = TabsInputFrame(line_frame, title="Machine Name:", title_width=113, fix_width=True)
        line_layout.addWidget(frame)
        self.machine_name = frame.get_input()

        frame = TabsInputFrame(line_frame, title="GPUs #:", title_width=113, fix_width=True)
        line_layout.addWidget(frame)
        self.cpu_gpu = frame.get_input()

        # line_frame: cores, ram, spacer, evaluate_button
        line_frame = Frame(content_frame)
        content_layout.addWidget(line_frame)
        line_layout = HorizontalLayout(line_frame)

        frame = TabsInputFrame(line_frame, title="Cores:", title_width=113, fix_width=True)
        line_layout.addWidget(frame)
        self.cores = frame.get_input()

        frame = TabsInputFrame(line_frame, title="RAM (Gb):", title_width=113, fix_width=True)
        line_layout.addWidget(frame)
        self.ram = frame.get_input()

    def _init_eco_sections(self):

        sections_layout = VerticalLayout(self.eco_sections)

        self.attendance_section = Frame(self.eco_sections, name="section")
        sections_layout.addWidget(self.attendance_section)
        self._init_attendance_section()

        self.price_section = Frame(self.eco_sections, name="section")
        sections_layout.addWidget(self.price_section)
        self._init_price_section()

        spacer = VerticalSpacer()
        sections_layout.addItem(spacer)

    def _init_attendance_section(self):

        section_layout = VerticalLayout(self.attendance_section)

        # title_frame
        title_frame = SectionTitleFrame(self.attendance_section,
                                        label_one_text="Attendance",
                                        label_two_text="attendance hint test")

        section_layout.addWidget(title_frame)
        self.attendance_hint = title_frame.get_label_two()

        # content_frame
        content_frame = Frame(self.attendance_section, name="attendance_content_frame")
        section_layout.addWidget(content_frame)

        content_layout = VerticalLayout(content_frame)

        # TODO: fill the implementation here
        label = Label(content_frame, text="Attendance implementation here.")
        content_layout.addWidget(label)

    def _init_price_section(self):

        section_layout = VerticalLayout(self.price_section)

        # title frame
        title_frame = SectionTitleFrame(self.price_section,
                                        label_one_text="Resource Price",
                                        label_two_text="price hint test")

        section_layout.addWidget(title_frame)
        self.price_hint = title_frame.get_label_two()

        # content_frame
        content_frame = Frame(self.price_section, name="price_content_frame")
        section_layout.addWidget(content_frame)

        content_layout = VerticalLayout(content_frame)

        # TODO: fill the implementation here
        label = Label(content_frame, text="Price implementation here.")
        content_layout.addWidget(label)

