import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget

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
        """
        Wrapper object for QLabel
        :param widget: required. defined the parent widget for the label
        :param height: optional. given fixed height for label
        :param width: optional. given fixed width for label
        :param text: optional. set label text (i.e. "this is a label")
        :param name: optional. object name fot this label
        :param align: optional. label align. Reference can be found: https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/core/Qt.AlignmentFlag.html#field_detail
        :param stylesheet: optional. apply stylesheet for label widget
        """
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
        """
        Clean up text within label
        :return: this function doesn't return value
        """
        self.setText("")


class Paragraph(Frame):
    def __init__(self, widget: QWidget, text_list: list, space: int = 0, **kwargs):
        """
        Wrapper object for QLabel
        :param widget: required. defined the parent widget for this paragraph widget
        :param text_list: required. array of string for the paragraph. (i.e. ["Sentense one.", "Sentense two."])
        :param space: optional. space between each label.
        :param height: optional. given fixed height fot each label
        :param width: optional. given fixed width fot each label
        :param name: optional. object name fot each label
        :param align: optional. align for each label. Reference can be found: https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/core/Qt.AlignmentFlag.html#field_detail
        :param stylesheet: optional. apply stylesheet for each label
        """

        super(Paragraph, self).__init__(widget)

        layout = VerticalLayout(self, space=space)

        for text in text_list:
            label = Label(self, text=text, **kwargs)
            layout.addWidget(label)
