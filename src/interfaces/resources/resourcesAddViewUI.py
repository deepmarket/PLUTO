"""

    This file provides a pure GUI interface for resources.
    This component provides a workflow style interface to add current machine to resources pool.

"""

from PyQt5.QtWidgets import QFrame, QLineEdit
from PyQt5.QtCore import pyqtSignal

from ..widgets import Frame, Button, VerticalLayout, StackLayout


class ResourcesAddViewUI(Frame):

    signal:         pyqtSignal = None

    stack:          StackLayout = None
    stack_view:     Frame = None
    button_view:    Frame = None

    tech_section:   Frame = None
    eco_section:    Frame = None

    next_page:      Button = None
    back:           Button = None
    submit:         Button = None
    cancel:         Button = None

    current_cpu:    int = 0
    current_core:   int = 0
    current_ram:    int = 0

    ip_address:     QLineEdit = None
    machine_name:   QLineEdit = None
    cpu_gpu:        QLineEdit = None
    ram:            QLineEdit = None


    def __init__(self, signal:pyqtSignal, *args, **kwargs):
        super(ResourcesAddViewUI, self).__init__(*args, **kwargs)

        self.signal = signal
        self._init_ui()

    def _init_ui(self):
        
        self.stack_view = Frame(self)
        self.button_view = Frame(self)

        layout = VerticalLayout(self)
        layout.addWidget(self.stack_view)
        layout.addWidget(self.button_view)

        self.tech_section = Frame(self.stack_view)
        self.eco_section = Frame(self.stack_view)

        self._init_tech_section()
        self._init_eco_section()

        self.stack = StackLayout(self.stack_view)
        self.stack.addWidget(tech_section)
        self.stack.addWidget(eco_section)

        self.next_page = Button(self.button_view, text="NEXT")
        self.back = Button(self.button_view, text="BACK")
        self.submit = Button(self.button_view, text="SUBMIT")
        self.cancel = Button(self.button_view, text="CANCEL")

        # spacer

    def _init_tech_section(self):
        # layout = VerticalLayout(self)

        # button = Button(self, text="CANCEL")
        # button.clicked.connect(self.on_cancel_button_clicked)

        # layout.addWidget(button)

    def _init_eco_section(self):
        pass

    def on
    
    def on_submit_button_clicked(self):
        self.signal.emit()

    def on_cancel_button_clicked(self):
        self.signal.emit()