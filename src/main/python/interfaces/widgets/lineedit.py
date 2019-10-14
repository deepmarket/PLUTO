from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QWidget


class LineEdit(QLineEdit):
    def __init__(
        self,
        widget: QWidget,
        height: int = 0,
        width: int = 0,
        name: str = "",
        hint: str = "",
        echo: bool = False,
        align: Qt = None,
        stylesheet=None,
        **kwargs
    ):
        """
        Wrapper object for QLineEdit
        :param widget: required. the parent widget for this the lineedit input object
        :param height: optional. the height of this input
        :param width: optional. the width of this input
        :param name: optional. the object name fot this input
        :param hint: optional. the placeholder in this input
        :param echo: optional. if the input will be encrypted to dot
        :param align: optional. the align of the input text
        :param stylesheet: optional. apply stylesheet for input
        """
        super(LineEdit, self).__init__(widget)

        # disable focus frame (blue outline)
        self.setAttribute(Qt.WA_MacShowFocusRect, 0)

        # Set size
        height and self.setFixedHeight(height)
        width and self.setFixedWidth(width)
        align and self.setAlignment(align)

        # Set property if given
        name and self.setObjectName(name)
        hint and self.setPlaceholderText(hint)
        echo is True and self.setEchoMode(QLineEdit.Password)

    def enable(self):
        """
        Enable input.
        """
        self.setEnabled(True)

    def disable(self):
        """
        Disable input.
        """
        self.setEnabled(False)

    def reset(self):
        """
        Clean up input text, remove focus, and enable input.
        """
        self.setText("")
        self.clearFocus()
        self.enable()
