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

from ..stylesheet import resources_style

class ResourcesAddViewUI(Frame):

    signal:         pyqtSignal = None

    stack:              StackLayout = None
    stack_view:         Frame = None
    button_view:        Frame = None

    tech_sections:       Frame = None
    eco_sections:        Frame = None

    cancel:             Button = None
    back:               Button = None
    next_page:          Button = None
    submit:             Button = None

    current_cpu:        ConfigFrame = None
    current_core:       ConfigFrame = None
    current_ram:        ConfigFrame = None

    ip_address:         QLineEdit = None
    machine_name:       QLineEdit = None
    cpu_gpu:            QLineEdit = None
    cores:              QLineEdit = None
    ram:                QLineEdit = None

    verification_hint:  Label = None
    configuration_hint: Label = None
    planning_hint:      Label = None
    attendance_hint:    Label = None
    price_hint:         Label = None
    global_hint:        Label = None

    def __init__(self, signal:pyqtSignal, *args, **kwargs):
        super(ResourcesAddViewUI, self).__init__(*args, **kwargs)

        self.signal = signal
        self._init_ui()

        self.setStyleSheet(resources_style)

    def _init_ui(self):
        # --------- self/resource ---------

        window_layout = VerticalLayout(self, t_m=30, l_m=50, r_m=46, space=30)

        self.stack_view = Frame(self)
        window_layout.addWidget(self.stack_view)

        self.button_view = Frame(self)
        window_layout.addWidget(self.button_view)

        # --------- stack_view ---------

        self.stack = StackLayout(self.stack_view)

        self.tech_sections = Frame(self.stack_view)
        self.stack.insertWidget(0, self.tech_sections)

        self.eco_sections = Frame(self.stack_view)
        self.stack.insertWidget(1, self.eco_sections)

        self._init_tech_sections()
        self._init_eco_sections()

        # --------- button_view ---------

        layout = HorizontalLayout(self.button_view)

        self.cancel = Button(self.button_view, text="CANCEL")
        layout.addWidget(self.cancel)

        spacer = HorizontalSpacer()
        layout.addItem(spacer)

        self.back = Button(self.button_view, text="BACK")
        layout.addWidget(self.back)

        self.next_page = Button(self.button_view, text="NEXT")
        layout.addWidget(self.next_page)

        self.submit = Button(self.button_view, text="SUBMIT")
        layout.addWidget(self.submit)

        # --------- binding event to function ---------

        self.cancel.clicked.connect(self.on_cancel_clicked)
        self.back.clicked.connect(self.on_back_clicked)
        self.next_page.clicked.connect(self.on_next_page_clicked)
        self.submit.clicked.connect(self.on_submit_clicked)


    def _init_tech_sections(self):

        # --------- tech sections ---------

        sections_layout = VerticalLayout(self.tech_sections, space=30)

        verification_section = Frame(self.tech_sections)
        sections_layout.addWidget(verification_section)

        configuration_section = Frame(self.tech_sections, height=108)
        sections_layout.addWidget(configuration_section)

        planning_section = Frame(self.tech_sections)
        sections_layout.addWidget(planning_section)

        spacer = VerticalSpacer()
        sections_layout.addItem(spacer)

        # --------- verification section ---------

        section_layout = VerticalLayout(verification_section, space=30)

        # title frame
        frame = SectionTitleFrame(verification_section,
                                  label_one_text="Resource Verification",
                                  label_two_text="ip verification hint test")

        section_layout.addWidget(frame)
        self.verification_hint = frame.get_label_two()

        # ip_address
        frame = TabsInputFrame(verification_section,
                               title="IP Address:", title_width=66, space=21)

        section_layout.addWidget(frame)
        self.ip_address = frame.get_input()

        # --------- configuration section ---------

        section_layout = VerticalLayout(configuration_section,
                                        t_m=21, b_m=21, l_m=27, r_m=27, space=30)

        # title frame
        frame = SectionTitleFrame(configuration_section,
                                  label_one_text="Machine Configuration",
                                  label_two_text="config hint test")

        section_layout.addWidget(frame)
        self.configuration_hint = frame.get_label_two()

        # frame: three config frame
        frame = Frame(configuration_section)
        section_layout.addWidget(frame)

        layout = HorizontalLayout(frame)

        self.current_cpu = ConfigFrame(frame, label_one_text="Compute:", label_two_text="8GB")
        layout.addWidget(self.current_cpu)

        self.current_core = ConfigFrame(frame, label_one_text="Cores:", label_two_text="4")
        layout.addWidget(self.current_core)

        self.current_ram = ConfigFrame(frame, label_one_text="RAM:", label_two_text="4GB")
        layout.addWidget(self.current_ram)

        # --------- planning section ---------

        section_layout = VerticalLayout(planning_section, space=30)

        # title frame
        frame = SectionTitleFrame(planning_section,
                                  label_one_text="Resource Planning",
                                  label_two_text="planning hint test")

        section_layout.addWidget(frame)
        self.planning_hint = frame.get_label_two()

        # frame: two line frame contains inputs
        frame = Frame(planning_section, height=132)
        section_layout.addWidget(frame)

        layout = VerticalLayout(frame, t_m=27, r_m=32, b_m=27)

        # line_frame: machine_name, cpu_gpu
        line_frame = Frame(frame)
        layout.addWidget(line_frame)

        line_layout = HorizontalLayout(line_frame)

        frame = TabsInputFrame(line_frame, title="Machine Name:",
                                title_width=113, space=18, width=285,
                                fix_width=True)

        line_layout.addWidget(frame)
        self.machine_name = frame.get_input()

        frame = TabsInputFrame(line_frame, title="GPUs #:",
                                title_width=113, space=18, width=285,
                                fix_width=True)

        line_layout.addWidget(frame)
        self.cpu_gpu = frame.get_input()

        # spacer
        spacer = VerticalSpacer()
        layout.addItem(spacer)

        # line_frame: cores, ram, spacer, evaluate_button
        line_frame = Frame(frame)
        layout.addWidget(line_frame)

        line_layout = HorizontalLayout(line_frame)

        frame = TabsInputFrame(line_frame, title="Cores:",
                                title_width=113, space=18, width=285,
                                fix_width=True)

        line_layout.addWidget(frame)
        self.cores = frame.get_input()

        frame = TabsInputFrame(line_frame, title="RAM (Gb):",
                                title_width=113, space=18, width=285,
                                fix_width=True)

        line_layout.addWidget(frame)
        self.ram = frame.get_input()

    def _init_eco_sections(self):

        # --------- eco sections ---------

        sections_layout = VerticalLayout(self.eco_sections, space=30)

        attendance_section = Frame(self.eco_sections)
        sections_layout.addWidget(attendance_section)

        price_section = Frame(self.eco_sections)
        sections_layout.addWidget(price_section)

        spacer = VerticalSpacer()
        sections_layout.addItem(spacer)

        # --------- attendance section ---------

        section_layout = VerticalLayout(attendance_section, space=30)

        # title frame
        frame = SectionTitleFrame(attendance_section,
                                  label_one_text="Attendance",
                                  label_two_text="attendance hint test")

        section_layout.addWidget(frame)
        self.attendance_hint = frame.get_label_two()

        # TODO: fill the implementation here
        label = Label(attendance_section, text="attendance section here")
        section_layout.addWidget(label)

        # --------- price section ---------

        section_layout = VerticalLayout(price_section, space=30)

        # title frame
        frame = SectionTitleFrame(price_section,
                                  label_one_text="Resource Price",
                                  label_two_text="price hint test")

        section_layout.addWidget(frame)
        self.price_hint = frame.get_label_two()

        # TODO: fill the implementation here
        label = Label(attendance_section, text="price section here")
        section_layout.addWidget(label)

    def on_cancel_clicked(self):
        self.signal.emit()

    def on_back_clicked(self):
        self.stack.setCurrentIndex(0)

    def on_next_page_clicked(self):
        self.stack.setCurrentIndex(1)

    def on_submit_clicked(self):
        self.signal.emit()

