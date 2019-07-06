"""
 
    This module generate a simple placeholder frame without any contents.
 
"""

from PyQt5 import QtWidgets


class Frame(QtWidgets.QFrame):

    def __init__(self, widget, **kwargs):
        super(Frame, self).__init__(widget)

        if kwargs:
            # Lambda func grab input args
            get_param = lambda x : kwargs.get(x)

            height = get_param("height")
            width = get_param("width")
            name = get_param("name")
            stylesheet = get_param("stylesheet")

            # Set property if given
            height and self.setFixedHeight(height)
            width and self.setFixedWidth(width)
            name and self.setObjectName(name)
            stylesheet and self.setObjectName(name)


