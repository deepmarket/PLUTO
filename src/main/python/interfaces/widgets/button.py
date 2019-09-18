from PyQt5.QtWidgets import QPushButton, QRadioButton, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt


class Button(QPushButton):
    def __init__(
        self,
        widget: QWidget,
        text: str = "",
        name: str = "",
        cursor: bool = False,
        stylesheet=None,
        icon=None,
        icon_size: int = 0,
        **kwargs
    ):
        """
        :param widget: required. defined the parent widget for this button
        """

        super(Button, self).__init__(widget)

        # Set property if given
        text and self.setText(text)
        name and self.setObjectName(name)
        stylesheet and self.setObjectName(name)
        cursor is True and self.setCursor(Qt.PointingHandCursor)

        # Set icon if given
        if icon:
            self.setIcon(QIcon(icon))
            if icon_size:
                self.setIconSize(QSize(icon_size, icon_size))

    def enable(self):
        self.setEnabled(True)

    def disable(self):
        self.setEnabled(False)


class RadioButton(QRadioButton):
    def __init__(self, widget: QWidget, *args, name: str = "", **kwargs):
        super(RadioButton, self).__init__(widget, *args)

        # Set property if given
        name and self.setObjectName(name)
