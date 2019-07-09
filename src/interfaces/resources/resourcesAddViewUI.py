"""

    This file provides a pure GUI interface for resources.
    This component provides a workflow style interface to add current machine to resources pool.

"""

from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import pyqtSignal

from ..widgets import Button, VerticalLayout


class ResourcesAddViewUI(QFrame):

    def __init__(self, signal:pyqtSignal, *args, **kwargs):
        super(ResourcesAddViewUI, self).__init__()

        self.signal = signal

        self._init_ui()

    def _init_ui(self):
        layout = VerticalLayout(self)

        button = Button(self, text="CANCEL")
        button.clicked.connect(self.on_cancel_button_clicked)

        layout.addWidget(button)
    
    def on_cancel_button_clicked(self):
        self.signal.emit()