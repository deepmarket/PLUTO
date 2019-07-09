"""

    This file provides a pure GUI interface for resources.
    This component provides a workflow style interface to add current machine to resources pool.

"""

from PyQt5.QtWidgets import QFrame, QLineEdit
from PyQt5.QtCore import pyqtSignal

from ..widgets import (Frame, Button, Label,
                        HorizontalLayout, VerticalLayout, StackLayout,
                        HorizontalSpacer, VerticalSpacer)


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

    current_cpu:        int = 0
    current_core:       int = 0
    current_ram:        int = 0

    ip_address:         QLineEdit = None
    machine_name:       QLineEdit = None
    cpu_gpu:            QLineEdit = None
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

    def _init_ui(self):
        # --------- self/resource ---------

        window_layout = VerticalLayout(self)

        self.stack_view = Frame(self)
        window_layout.addWidget(self.stack_view)

        self.button_view = Frame(self)
        window_layout.addWidget(self.button_view)

        # --------- stack_view ---------
        
        print(self.stack_view.geometry().width())
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

        sections_layout = VerticalLayout(self.tech_sections)

        verification_section = Frame(self.tech_sections)
        sections_layout.addWidget(verification_section)

        configuration_section = Frame(self.tech_sections)
        sections_layout.addWidget(configuration_section)

        planning_section = Frame(self.tech_sections)
        sections_layout.addWidget(planning_section)

        spacer = VerticalSpacer()
        sections_layout.addItem(spacer)

        # --------- verification section ---------
        
        section_layout = VerticalLayout(verification_section)

        # line_frame: title, spacer, verification_hint 

        line_frame = Frame(verification_section)
        section_layout.addWidget(line_frame)

        line_layout = HorizontalLayout(line_frame)

        title = Label(line_frame, text="IP Verification")
        line_layout.addWidget(title)

        spacer = HorizontalSpacer()
        line_layout.addItem(spacer)

        self.verification_hint = Label(line_frame, text="ip verification hint")
        line_layout.addWidget(self.verification_hint)

        # line_frame: label, ip_address 

        # --------- configuration section ---------

        # line_frame: title, spacer, configuration_hint
        
        # line_frame: three boxes

        # --------- planning section ---------

        # line_frame: title, spacer, planning_hint

        # line_frame: machine_name, cpu_gpu

        # line_frame: cores, ram

        
    def _init_eco_sections(self):
        
        # --------- eco sections ---------

        sections_layout = VerticalLayout(self.eco_sections)

        attendance_section = Frame(self.eco_sections)
        sections_layout.addWidget(attendance_section)

        price_section = Frame(self.eco_sections)
        sections_layout.addWidget(price_section)

        spacer = VerticalSpacer()
        sections_layout.addItem(spacer)

        # --------- attendance section ---------

        section_layout = VerticalLayout(attendance_section)

        # line_frame: title, spacer, attendance_hint
        line_frame = Frame(attendance_section)
        section_layout.addWidget(line_frame)
        line_layout = HorizontalLayout(line_frame)

        title = Label(line_frame, text="Attendance")
        line_layout.addWidget(title)

        spacer = HorizontalSpacer()
        line_layout.addItem(spacer)

        self.attendance_hint = Label(line_frame, text="attendance hint")
        line_layout.addWidget(self.attendance_hint)

        # --------- price section ---------
        

    def on_cancel_clicked(self):
        self.signal.emit()

    def on_back_clicked(self):
        self.stack.setCurrentIndex(0)

    def on_next_page_clicked(self):
        self.stack.setCurrentIndex(1)
    
    def on_submit_clicked(self):
        self.signal.emit()

