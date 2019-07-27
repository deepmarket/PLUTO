"""

    This file provides a pure GUI interface for resources.
    This component provides a workflow style interface to add current machine to resources pool.

"""

from abc import ABCMeta, abstractmethod

from PyQt5.QtWidgets import QFrame, QLineEdit, QLabel, QRadioButton
from PyQt5.QtCore import pyqtSignal, Qt

from ..widgets import (Frame, SectionTitleFrame, ConfigFrame, ViewInputFrame,
                        ViewButton, Label, PriceBox,
                        HorizontalLayout, VerticalLayout, StackLayout,
                        HorizontalSpacer, VerticalSpacer)

from ..util import get_children
from ..stylesheet import resources_add_view_style

class ResourcesAddViewUI(Frame):

    # metaclass for defining abstract base classes
    # Reference can be found here: https://docs.python.org/2/library/abc.html#abc.abstractmethod
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

    cancel                  :ViewButton = None
    back                    :ViewButton = None
    next_page               :ViewButton = None
    submit                  :ViewButton = None

    current_cpu_gpu         :ConfigFrame = None
    current_cores           :ConfigFrame = None
    current_ram             :ConfigFrame = None

    ip_address              :ViewInputFrame = None
    machine_name            :ViewInputFrame = None
    cpu_gpu                 :ViewInputFrame = None
    cores                   :ViewInputFrame = None
    ram                     :ViewInputFrame = None

    auto_price_box          :PriceBox = None
    offer_price_box         :PriceBox = None

    global_hint             :Label = None
    verification_hint       :Label = None
    configuration_hint      :Label = None
    planning_hint           :Label = None
    attendance_hint         :Label = None
    price_hint              :Label = None
    submit_hint             :Label = None

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

    def on_auto_price_clicked(self):
        self.auto_price_box.check()
        self.offer_price_box.uncheck()

    def on_offer_price_clicked(self):
        self.auto_price_box.uncheck()
        self.offer_price_box.check()

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
        # reset input
        self.ip_address.reset()
        self.machine_name.reset()
        self.cpu_gpu.reset()
        self.cores.reset()
        self.ram.reset()

        # reset config
        self.current_cpu_gpu.reset()
        self.current_cores.reset()
        self.current_ram.reset()

        # reset price box
        self.auto_price_box.check()

        # reset hint
        self.reset_hint()

        # reload stylesheet
        self.reload_stylesheet()

        # redirect to default page
        self._to_tech_section()

    def reset_hint(self):
        self.global_hint.reset()
        self.verification_hint.reset()
        self.configuration_hint.reset()
        self.planning_hint.reset()
        self.attendance_hint.reset()
        self.price_hint.reset()
        self.submit_hint.reset()

    def reload_stylesheet(self):
        self.setStyleSheet(resources_add_view_style)

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

        self.cancel = ViewButton(self.button_view, text="CANCEL", cursor=True)
        layout.addWidget(self.cancel)

        spacer = HorizontalSpacer()
        layout.addItem(spacer)

        self.back = ViewButton(self.button_view, text="BACK", cursor=True)
        layout.addWidget(self.back)

        self.next_page = ViewButton(self.button_view, text="NEXT", cursor=True)
        layout.addWidget(self.next_page)

        self.submit = ViewButton(self.button_view, text="SUBMIT", cursor=True)
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

        self.machine_name.input_field.textChanged.connect(self.on_machine_name_edit)
        self.cpu_gpu.input_field.textChanged.connect(self.on_cpu_gpu_edit)
        self.cores.input_field.textChanged.connect(self.on_cores_edit)
        self.ram.input_field.textChanged.connect(self.on_ram_edit)

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
        self.ip_address = ViewInputFrame(content_frame, title="IP Address:", title_width=66)
        content_layout.addWidget(self.ip_address)

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

        self.machine_name = ViewInputFrame(line_frame, title="Machine Name:", title_width=113, fix_width=True)
        line_layout.addWidget(self.machine_name)

        self.cpu_gpu = ViewInputFrame(line_frame, title="GPUs #:", title_width=113, fix_width=True)
        line_layout.addWidget(self.cpu_gpu)

        # line_frame: cores, ram, spacer, evaluate_button
        line_frame = Frame(content_frame)
        content_layout.addWidget(line_frame)
        line_layout = HorizontalLayout(line_frame)

        self.cores = ViewInputFrame(line_frame, title="Cores:", title_width=113, fix_width=True)
        line_layout.addWidget(self.cores)

        self.ram = ViewInputFrame(line_frame, title="RAM (Gb):", title_width=113, fix_width=True)
        line_layout.addWidget(self.ram)

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

        self.submit_hint = Label(self.eco_sections, name="section_hint",
                                 align=(Qt.AlignRight | Qt.AlignVCenter))
        sections_layout.addWidget(self.submit_hint)

        self.auto_price_box.button.clicked.connect(self.on_auto_price_clicked)
        self.offer_price_box.button.clicked.connect(self.on_offer_price_clicked)

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

        content_layout = HorizontalLayout(content_frame, space=18)

        self.auto_price_box = PriceBox(self.price_section, title="Automated Price:", label="Credit / Hr")
        content_layout.addWidget(self.auto_price_box)
        self.auto_price_box.input_field.setEnabled(False)

        self.offer_price_box = PriceBox(self.price_section, title="Offering Price:", label="Credit / Hr")
        content_layout.addWidget(self.offer_price_box)
