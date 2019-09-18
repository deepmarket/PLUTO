from PyQt5.QtWidgets import QLineEdit, QWidget
from PyQt5.QtCore import Qt


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
        self.setEnabled(True)

    def disable(self):
        self.setEnabled(False)

    def reset(self):
        self.setText("")
        self.clearFocus()
        self.enable()
