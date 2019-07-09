"""

    This file provides a pure GUI interface for resources.
    This component is overall UI manager for resources tab.

"""

from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import pyqtSignal

from ..widgets import StackLayout


class ResourcesUI(QFrame):

    _stack = None
    _to_controller_signal = pyqtSignal()
    _to_add_view_signal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(ResourcesUI, self).__init__(*args, **kwargs)

        # create layout for interface
        self._stack = StackLayout(self)

        # connect signal
        self._to_controller_signal.connect(self._to_controller)
        self._to_add_view_signal.connect(self._to_add_view)
    
    # set functions, given widget, set to the corresponding index
    def set_controller(self, widget):
        self._stack.insertWidget(0, widget)

    def set_add_view(self, widget):
        self._stack.insertWidget(1, widget)
    
    # display the widget in the corresponding index, raise error if happened
    def _to_controller(self):
        self._build_check()
        self._stack.setCurrentIndex(0)
    
    def _to_add_view(self):
        self._build_check()        
        self._stack.setCurrentIndex(1)

    def _build_check(self):
        self._stack.count() != 2 and print("Error: either controller/add_view has not been set!")
