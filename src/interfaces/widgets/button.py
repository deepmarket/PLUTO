"""
 
    This module generate a QPushButton object.
 
"""

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt


class Button(QPushButton):

    def __init__(self, widget, **kwargs):
        super(Button, self).__init__(widget)

        # Lambda func grab input args
        get_param = lambda x : kwargs.get(x)

        text = get_param("text")
        name = get_param("name")
        stylesheet = get_param("stylesheet")
        cursor = get_param("cursor")
        icon = get_param("icon")
        icon_size = get_param("icon_size")

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
