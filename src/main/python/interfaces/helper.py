from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import QLineEdit, QLabel
from PyQt5.QtGui import QPixmap, QIcon, QPainter, QBrush, QColor

time = [f"{i} AM" for i in range(1, 13)] + [f"{i} PM" for i in range(1, 13)]
weekday = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]


def get_children(widget, child_type, *args):
    """
    Find all matched child widgets belong to the type (or with given object name)

    :param widget: parent widget
    :param child_type: destinated child widgets type
    :args: optional, the name that child widgets currently have
    :return: list of all matched child widgets
    """
    # if None, children = []
    return [child for child in widget.findChildren(child_type, *args)]


def switch_scheme(widget, curr_scheme):
    """
    Switch the schme highlight when click scheme
    :param widget: parent widget
    :param curr_scheme: trigger function for the mousePress event
    """
    frames = [
        widget.scheme_01_frame,
        widget.scheme_02_frame,
        widget.scheme_03_frame,
        widget.scheme_04_frame,
    ]

    for frame in frames:
        # set frame to disable stylesheet
        frame.setObjectName("scheme_disable")

        # find all QLabel children within the frame
        labels = get_children(frame, QLabel)

        # set labels to disable stylesheet
        for label in labels:
            label.setObjectName("scheme_label_disable")

    # set frame to active stylesheet
    curr_scheme.setObjectName("scheme")

    # find all QLabel children within the frame
    labels = get_children(curr_scheme, QLabel)

    # set labels to enable stylesheet
    for label in labels:
        label.setObjectName("scheme_label")


# return a menu icon
def menu_icon(width):
    """
    Generate menu icon
    :return: QIcon object, which contains icon logo
    """

    height = 3
    pix = QPixmap(width, width)
    pix.fill(Qt.transparent)
    painter = QPainter()

    painter.begin(pix)

    painter.setPen(Qt.NoPen)
    painter.setBrush(QBrush(QColor("#6C7E8E")))
    painter.drawRect(QRectF(0, 2, width, height))
    painter.drawRect(QRectF(0, height + 2 * 2, width, height))
    painter.drawRect(QRectF(0, height * 2 + 3 * 2, width, height))

    painter.end()

    return QIcon(pix)
