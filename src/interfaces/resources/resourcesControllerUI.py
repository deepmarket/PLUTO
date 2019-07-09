"""

    This file provides a pure GUI interface for resources.
    This component is controlling interface for resources tab

"""

from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import pyqtSignal

from ..widgets import Button, VerticalLayout


class ResourcesControllerUI(QFrame):
    
    def __init__(self, signal:pyqtSignal, *args, **kwargs):
        super(ResourcesControllerUI, self).__init__()

        self.signal = signal

        self._init_ui()

    def _init_ui(self):
        layout = VerticalLayout(self)

        button = Button(self, text="ADD")

        layout.addWidget(button)
        button.clicked.connect(self.on_add_button_clicked)

        layout.addWidget(button)

    def on_add_button_clicked(self):
        self.signal.emit()