"""

    This module provides a text/image display.
    No user interaction functionailty is provided.

"""

from PyQt5 import QtWidgets

from .frame import Frame
from .layout import VerticalLayout


class Label(QtWidgets.QLabel):

    def __init__(self, widget, **kwargs):
        super(Label, self).__init__(widget)

        # Lambda func grab input args
        get_num = lambda x : kwargs.get(x, 0)
        get_param = lambda x : kwargs.get(x)

        height = get_num("height")
        width = get_num("width")

        text = get_param("text")
        name = get_param("name")
        stylesheet = get_param("stylesheet")
        align = get_param("align")

        # Set size
        height and self.setFixedHeight(height)
        width and self.setFixedWidth(width)

        # Set property if given
        text and self.setText(text)
        name and self.setObjectName(name)
        stylesheet and self.setObjectName(name)
        align and self.setAlignment(align)


class Paragraph(QtWidgets.QFrame):

    def __init__(self, widget, text_list, **kwargs):
        super(Paragraph, self).__init__(widget)

        # Lambda func grab input args
        get_num = lambda x : kwargs.get(x, 0)
        get_param = lambda x : kwargs.get(x)

        text_list = get_param("text_list")

        space = get_num("space")
        name = get_param("name")
        align = get_param("align")

        layout = VerticalLayout(self, space=space)

        for text in text_list:
            label = Label(self, text, name=name, align=align)
            layout.addWidget(label)


