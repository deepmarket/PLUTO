from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QWidget


class GroupBox(QGroupBox):
    def __init__(
        self, widget: QWidget, *args, name: str = "", align: Qt = None, **kwargs
    ):
        """
        Wrapper object for QGroupBox
        :param widget: required. defined the parent widget for groupbox widget
        :param name: optional. object name for this groupbox
        :param align: optional. groupbox internal align.
        """
        super(GroupBox, self).__init__(widget, *args)

        # Set property if given
        name and self.setObjectName(name)
        align and self.setAlignment(align)
