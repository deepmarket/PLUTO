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
        Wrapper object for QPushButton.
        :param widget: required. defined the parent widget for this button
        :param text: optional. label text on the button
        :param name: optional. object name for the button
        :param cursor: optional. whether change cursor style when hover button
        :param stylesheet: optional. given stylesheet to the button
        :param icon: optional. set icon to button. Reference: https://www.tutorialspoint.com/pyqt/pyqt_qpushbutton_widget.htm
        :param icon_size: optional. the size of the icon given to the button.
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
        """
        Enable button.
        :return: this function doesn't return value
        """
        self.setEnabled(True)

    def disable(self):
        """
        Disable button.
        :return: this function doesn't return value
        """
        self.setEnabled(False)


class RadioButton(QRadioButton):
    def __init__(self, widget: QWidget, *args, name: str = "", **kwargs):
        """
        Wrapper object for QRadioButton.
        :param: widget: required. the parent widget for this button.
        :param: name: optional. object name for this button.
        """
        super(RadioButton, self).__init__(widget, *args)

        # Set property if given
        name and self.setObjectName(name)
