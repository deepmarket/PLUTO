"""

    This module generate an input field allows user to enter and edit single line of plain text.

"""

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt


class LineEdit(QLineEdit):

    def __init__(self, widget, **kwargs):
        super(LineEdit, self).__init__(widget)

        # disable focus frame (blue outline)
        self.setAttribute(Qt.WA_MacShowFocusRect, 0)

        # Lambda func grab input args
        get_param = lambda x : kwargs.get(x)

        height = get_param("height")
        width = get_param("width")
        name = get_param("name")
        hint = get_param("hint")
        echo = get_param("echo")
        align = get_param("align")
        stylesheet = get_param("stylesheet")

        # Set size
        height and self.setFixedHeight(height)
        width and self.setFixedWidth(width)
        align and self.setAlignment(align)

        # Set property if given
        name and self.setObjectName(name)
        hint and self.setPlaceholderText(hint)
        echo is True and self.setEchoMode(QLineEdit.Password)

    def enable(self):
        self.setEnabled(True)

    def disable(self):
        self.setEnabled(False)

    def reset(self):
        self.setText("")
        self.clearFocus()
        self.enable()
