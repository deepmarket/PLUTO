"""
 
    This module generate a QPushButton object.
 
"""

from PyQt5 import QtWidgets, QtGui, QtCore


class Button(QtWidgets.QPushButton):

    def __init__(self, widget, **kwargs):
        super(Button, self).__init__(widget)

        if kwargs:
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
            cursor is True and self.setCursor(QtCore.Qt.PointingHandCursor)

            # Set icon if given
            if icon:
                self.setIcon(QtGui.QIcon(icon))
                if icon_size:
                    self.setIconSize(QtCore.QSize(icon_size, icon_size))
