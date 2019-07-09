"""
    This file provide a pure GUI interface for resource tab:
    1. ResourceUI: UI manager, control which widget is shown to user.
    2. ResourceControllerUI: initial interface shown to user, control 'add', 'edit', 'remove'
    3. ResourceAddViewUI: workflow style interface to add current machine to resources pool.

"""

from PyQt5 import QtWidgets, QtCore

from .widgets import Button, VerticalLayout, StackLayout


class ResourcesUI(QtWidgets.QFrame):

    _controler_signal = QtCore.pyqtSignal()
    _add_view_signal = QtCore.pyqtSignal()


    def __init__(self, *args, **kwargs):
        super(ResourceUI, self).__init__(*args, **kwargs)

        # Allocate child widgets
        self.controller = ResourceControllerUI(self._controler_signal)
        self.add_view = ResourceAddViewUI(self._add_view_signal)

        # insert widgets to layout
        self._stack = StackLayout(self)
        self._stack.addWidget(self.controller)
        self._stack.addWidget(self.add_view)

        # connect signal
        self._controler_signal.connect(self._show_add_view)
        self._add_view_signal.connect(self._show_controller)

        # show initial view
        self._show_controller()
    
    def _show_controller(self):
        self._stack.setCurrentIndex(0)
    
    def _show_add_view(self):
        self._stack.setCurrentIndex(1)


class ResourceControllerUI(QtWidgets.QFrame):
    
    def __init__(self, signal:QtCore.pyqtSignal, *args, **kwargs):
        super(ResourceControllerUI, self).__init__()

        self.signal = signal

        self._init_ui()

    def _init_ui(self):
        layout = VerticalLayout(self)

        button = Button(self, text="Add")

        layout.addWidget(button)
        button.clicked.connect(self.on_add_button_clicked)

        layout.addWidget(button)

    def on_add_button_clicked(self):
        self.signal.emit()


# TODO: should change to a better name
class ResourceAddViewUI(QtWidgets.QFrame):

    def __init__(self, signal:QtCore.pyqtSignal, *args, **kwargs):
        super(ResourceAddViewUI, self).__init__()

        self.signal = signal

        self._init_ui()

    def _init_ui(self):
        layout = VerticalLayout(self)

        button = Button(self, text="CANCEL")
        button.clicked.connect(self.on_cancel_button_clicked)

        layout.addWidget(button)
    
    def on_cancel_button_clicked(self):
        self.signal.emit()