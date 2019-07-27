"""

    This module provide a group box widget

"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QWidget


class GroupBox(QGroupBox):

    def __init__(
        self,
        widget:QWidget,
        *args,
        name: str = "",
        align: Qt = None,
        **kwargs
    ):
        super(GroupBox, self).__init__(widget, *args)

        # Set property if given
        name and self.setObjectName(name)
        align and self.setAlignment(align)
