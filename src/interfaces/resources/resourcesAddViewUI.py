"""

    This file provides a pure GUI interface for resources.
    This component provides a workflow style interface to add current machine to resources pool.

"""

from PyQt5.QtWidgets import QFrame, QLineEdit
from PyQt5.QtCore import pyqtSignal

from ..widgets import (Frame, Button, Label,
                        HorizontalLayout, VerticalLayout, StackLayout,
                        HorizontalSpacer)


class ResourcesAddViewUI(Frame):

    signal:         pyqtSignal = None

    stack:          StackLayout = None
    stack_view:     Frame = None
    button_view:    Frame = None

    tech_section:   Frame = None
    eco_section:    Frame = None

    cancel:         Button = None
    back:           Button = None
    next_page:      Button = None
    submit:         Button = None

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
        
        # widgets for self
        self.stack_view = Frame(self)
        self.button_view = Frame(self)

        # insert to layout
        layout = VerticalLayout(self)
        layout.addWidget(self.stack_view)
        layout.addWidget(self.button_view)

        # widgets for stack_view
        self.tech_section = Frame(self.stack_view)
        self.eco_section = Frame(self.stack_view)

        self._init_tech_section()
        self._init_eco_section()

        # insert to layout
        self.stack = StackLayout(self.stack_view)
        self.stack.addWidget(self.tech_section)
        self.stack.addWidget(self.eco_section)

        
        # widgets for button_view
        self.cancel = Button(self.button_view, text="CANCEL")
        self.back = Button(self.button_view, text="BACK")
        self.next_page = Button(self.button_view, text="NEXT")
        self.submit = Button(self.button_view, text="SUBMIT")

        # insert to layout
        spacer = HorizontalSpacer()

        layout = HorizontalLayout(self.button_view)
        layout.addWidget(self.cancel)
        layout.addItem(spacer)
        layout.addWidget(self.back)
        layout.addWidget(self.next_page)
        layout.addWidget(self.submit)

        # binding event to function
        self.cancel.clicked.connect(self.on_cancel_clicked)
        self.back.clicked.connect(self.on_back_clicked)
        self.next_page.clicked.connect(self.on_next_page_clicked)
        self.submit.clicked.connect(self.on_submit_clicked)


    def _init_tech_section(self):
        pass

    def _init_eco_section(self):
        pass

    def on_cancel_clicked(self):
        self.signal.emit()

    def on_back_clicked(self):
        pass

    def on_next_page_clicked(self):
        pass
    
    def on_submit_clicked(self):
        self.signal.emit()

