"""

    This module provides a text/image display.
    No user interaction functionailty is provided.

"""

import os
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

from .frame import Frame
from .layout import VerticalLayout
from ..util import load_path


class Label(QLabel):

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


class Paragraph(Frame):

    def __init__(self, widget, text_list:list, **kwargs):
        super(Paragraph, self).__init__(widget)

        # Lambda func grab input args
        get_num = lambda x : kwargs.get(x, 0)
        get_param = lambda x : kwargs.get(x)

        space = get_num("space")

        layout = VerticalLayout(self, space=space)

        for text in text_list:
            label = Label(self, text=text, **kwargs)
            layout.addWidget(label)


class Image(Label):

    def __init__(self, widget, img:str, **kwargs):
        super(Image, self).__init__(widget)

        # TODO: move this path to config file later on
        path = os.getcwd() + "/src/img/"

        # Lambda func grab input args
        get_num = lambda x : kwargs.get(x, 0)
        get_param = lambda x : kwargs.get(x)

        height = get_num("height")
        width = get_num("width")

        img = get_param("img")
        name = get_param("name")
        align = get_param("align")

        # Set property if given
        name and self.setObjectName(name)
        align and self.setAlignment(align)

        file = load_path(path+img)
        default = load_path(path+"default.jpg")

        pix_map = None

        if file:
            pix_map = QPixmap(file)
        elif default:
            pix_map = QPixmap(default)

        if pix_map:
            # scale to the greatest number
            if width and height: # both param given
                pix_map.scaledToWidth(width) if width >= height else pix_map.scaledToHeight(height)
            else: # either or none param given
                width and pix_map.scaledToWidth(width)
                height and pix_map.scaledToHeight(height)
            self.setPixmap(pix_map)
        else:
            self.setText("Image Not Found.")
