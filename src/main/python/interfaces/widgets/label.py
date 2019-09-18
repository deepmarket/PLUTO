import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtGui import QPixmap

from .frame import Frame
from .layout import VerticalLayout


class Label(QLabel):
    def __init__(
        self,
        widget: QWidget,
        height: int = 0,
        width: int = 0,
        text: str = "",
        name: str = "",
        align: Qt = None,
        stylesheet=None,
        **kwargs
    ):
        super(Label, self).__init__(widget)

        # Set size
        height and self.setFixedHeight(height)
        width and self.setFixedWidth(width)

        # Set property if given
        text and self.setText(text)
        name and self.setObjectName(name)
        stylesheet and self.setObjectName(name)
        align and self.setAlignment(align)

    def reset(self):
        self.setText("")


class Paragraph(Frame):
    def __init__(self, widget: QWidget, text_list: list, space: int = 0, **kwargs):
        super(Paragraph, self).__init__(widget)

        layout = VerticalLayout(self, space=space)

        for text in text_list:
            label = Label(self, text=text, **kwargs)
            layout.addWidget(label)


class Image(Label):
    def __init__(
        self, widget: QWidget, img: str, height: int = 0, width: int = 0, **kwargs
    ):
        super(Image, self).__init__(widget, height=height, width=width, **kwargs)

        # TODO: move this path to config file later on
        path = os.getcwd() + "/src/img/"

        file = load_path(path + img)
        default = load_path(path + "default.jpg")

        pix_map = None

        if file:
            pix_map = QPixmap(file)
        elif default:
            pix_map = QPixmap(default)

        if pix_map:
            # scale to the greatest number
            if width and height:  # both param given
                pix_map.scaledToWidth(
                    width
                ) if width >= height else pix_map.scaledToHeight(height)
            else:  # either or none param given
                width and pix_map.scaledToWidth(width)
                height and pix_map.scaledToHeight(height)
            self.setPixmap(pix_map)
        else:
            self.setText("Image Not Found.")
