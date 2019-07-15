"""

    This file provides a pure GUI interface for resources.
    This component provides a workflow style interface to add current machine to resources pool.

"""

from abc import ABCMeta, abstractmethod

from PyQt5.QtWidgets import QFrame, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSignal

from ..widgets import (Frame, SectionTitleFrame, ConfigFrame, TabsInputFrame,
                        Button, Label,
                        HorizontalLayout, VerticalLayout, StackLayout,
                        HorizontalSpacer, VerticalSpacer)

from ..util import get_children
from ..stylesheet import resources_add_view_style

class ResourcesAddViewUI(Frame):

    # metaclass for defining abstract base classes
    __metaclass__ = ABCMeta

    signal                  :pyqtSignal = None

    title_view              :Frame = None
    stack_view              :Frame = None
    stack                   :StackLayout = None
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

    current_cpu_gpu         :ConfigFrame = None
    current_cores           :ConfigFrame = None
    current_ram             :ConfigFrame = None

    ip_address              :QLineEdit = None
    machine_name            :QLineEdit = None
    cpu_gpu                 :QLineEdit = None
    cores                   :QLineEdit = None
    ram                     :QLineEdit = None

    global_hint             :Label = None
    verification_hint       :Label = None
    configuration_hint      :Label = None
    planning_hint           :Label = None
    attendance_hint         :Label = None
    price_hint              :Label = None

    def __init__(self, signal:pyqtSignal, *args, **kwargs):
        super(ResourcesAddViewUI, self).__init__(*args, name="view", **kwargs)

        self.signal = signal
        self._init_ui()
        self.setStyleSheet(resources_add_view_style)

        self._to_tech_section()

    def on_cancel_clicked(self):
        self.signal.emit()

    def on_back_clicked(self):
        self._to_tech_section()

    def on_next_page_clicked(self):
        self._to_eco_section()

    def on_submit_clicked(self):
        self.signal.emit()

    @abstractmethod
    def on_machine_name_edit(self):
        pass

    @abstractmethod
    def on_cpu_gpu_edit(self):
        pass

    @abstractmethod
    def on_cores_edit(self):
        pass

    @abstractmethod
    def on_ram_edit(self):
        pass

    def reset(self):
        self.reset_section(self.verification_section)
        self.reset_section(self.configuration_section)
        self.reset_section(self.planning_section)
        self.reset_section(self.attendance_section)
        self.reset_section(self.price_section)

        self.reset_config(self.current_cpu_gpu)
        self.reset_config(self.current_cores)
        self.reset_config(self.current_ram)

        self.reset_hint()

        self._to_tech_section()

    def enable_section(self, section):
        if section in vars(self).values():
            input_frame = get_children(section, QFrame, "view_input_disable")

            # change style
            for frame in input_frame:
                frame.setObjectName("view_input")

            # enable input
            qlineedit = get_children(section, QLineEdit)
            for edit in qlineedit:
                edit.setEnabled(True)

    def disable_section(self, section):
        if section in vars(self).values():
            input_frame = get_children(section, QFrame, "view_input")

            # change style
            for frame in input_frame:
                frame.setObjectName("view_input_disable")

            # enable input
            qlineedit = get_children(section, QLineEdit)
            for edit in qlineedit:
                edit.setEnabled(False)

    def enable_button(self, button):
        if button in vars(self).values():
            button.setObjectName("view_button")
            button.setEnabled(True)

    def disable_button(self, button):
        if button in vars(self).values():
            button.setObjectName("view_button_disable")
            button.setEnabled(False)

    def set_config_text(self, config:ConfigFrame, text:str):
        if config in vars(self).values():
            config.set_label_two_text(text)

    def set_config_green(self, config:ConfigFrame):
        if config in vars(self).values():
            # update object name
            config.setObjectName("config_frame_green")

            # reload stylesheet
            self.setStyleSheet(resources_add_view_style)

    def set_config_red(self, config:ConfigFrame):
        if config in vars(self).values():
            # update object name
            config.setObjectName("config_frame_red")

            # reload stylesheet
            self.setStyleSheet(resources_add_view_style)

    def set_hint(self, hint:QLabel, text:str):
        if hint in vars(self).values():
            hint.setText(text)

    def reset_section(self, section):
        if section in vars(self).values():
            qlineedit = get_children(section, QLineEdit)
            for edit in qlineedit:
                edit.setText("")
                edit.clearFocus()

    def reset_config(self, config):
        if config in vars(self).values():
            self.set_config_text(config, "-")
            config.setObjectName("config_frame")
            self.setStyleSheet(resources_add_view_style)

    def reset_hint(self):
        self.verification_hint.setText("")
        self.configuration_hint.setText("")
        self.planning_hint.setText("")
        self.attendance_hint.setText("")
        self.price_hint.setText("")

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

    def _init_ui(self):

        window_layout = VerticalLayout(self)

        self.title_view = Frame(self, name="view_title_frame")
        window_layout.addWidget(self.title_view)
        self._init_title_view()

        self.stack_view = Frame(self, name="view_stack_frame")
        window_layout.addWidget(self.stack_view)
        self._init_stack_view()

        self.button_view = Frame(self, name="view_buttons_frame")
        window_layout.addWidget(self.button_view)
        self._init_button_view()

    def _init_title_view(self):

        layout = HorizontalLayout(self.title_view)

        title = Label(self.title_view, name="view_title", text="Add New Resource")
        layout.addWidget(title)

        spacer = HorizontalSpacer()
        layout.addItem(spacer)

        self.global_hint = Label(self.title_view, name="section_hint")
        layout.addWidget(self.global_hint)

    def _init_stack_view(self):

        self.stack = StackLayout(self.stack_view)

        self.tech_sections = Frame(self.stack_view)
        self.stack.insertWidget(0, self.tech_sections)

        self.eco_sections = Frame(self.stack_view)
        self.stack.insertWidget(1, self.eco_sections)

        self._init_tech_sections()
        self._init_eco_sections()

    def _init_button_view(self):

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

        self.machine_name.textChanged.connect(self.on_machine_name_edit)
        self.cpu_gpu.textChanged.connect(self.on_cpu_gpu_edit)
        self.cores.textChanged.connect(self.on_cores_edit)
        self.ram.textChanged.connect(self.on_ram_edit)

    def _init_verification_section(self):

        section_layout = VerticalLayout(self.verification_section)

        # title_frame
        title_frame = SectionTitleFrame(self.verification_section, label_one_text="Resource Verification")

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
        title_frame = SectionTitleFrame(content_frame, label_one_text="Machine Configuration")

        content_layout.addWidget(title_frame)
        self.configuration_hint = title_frame.get_label_two()

        # frame: three config frame
        frame = Frame(content_frame)
        content_layout.addWidget(frame)
        layout = HorizontalLayout(frame)

        self.current_cpu_gpu = ConfigFrame(frame, label_one_text="Compute:", label_two_text="-")
        layout.addWidget(self.current_cpu_gpu)

        self.current_cores = ConfigFrame(frame, label_one_text="Cores:", label_two_text="-")
        layout.addWidget(self.current_cores)

        self.current_ram = ConfigFrame(frame, label_one_text="RAM:", label_two_text="-")
        layout.addWidget(self.current_ram)

    def _init_planning_section(self):

        section_layout = VerticalLayout(self.planning_section)

        # title frame
        title_frame = SectionTitleFrame(self.planning_section, label_one_text="Resource Planning")

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

