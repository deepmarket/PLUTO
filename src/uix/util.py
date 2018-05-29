"""
    helper functions on construct GUI
"""

import os
import re
import datetime

import matplotlib
# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import arange, sin, pi

from PyQt5.QtCore import Qt, QSize, QRect, QPropertyAnimation, QPoint, QTimer, QPointF, QRectF, QSequentialAnimationGroup
from PyQt5.QtGui import QPixmap, QIcon, QFontDatabase, QPainter, QFont, QColor, QPen, QBrush, QPolygonF, QPainterPath
from PyQt5.QtWidgets import (QDesktopWidget, QPushButton, QLabel, QFrame, QLineEdit, QCheckBox,
                             QVBoxLayout, QHBoxLayout, QStackedLayout, QGraphicsView, QGraphicsScene,
                             QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsPolygonItem, QGraphicsPathItem,
                             QGraphicsTextItem, QGraphicsDropShadowEffect, QDialog, QMainWindow, QSizePolicy,
                             QSpacerItem, QTableWidget, QHeaderView, QAbstractItemView, QTableWidgetItem, QMessageBox)

from src.uix.stylesheet import *


# load icon
def load_image(filename, image_type):
    icon_path = os.getcwd() + "/src/img/"
    return icon_path + filename + image_type


# load font
def load_font():
    dir_path = os.getcwd() + "/src/font/"

    # robust check, if directory exist
    if os.path.isdir(dir_path):

        # read all ttf files within directory
        font_list = os.listdir(dir_path)
        font_list = list(filter(lambda x: x.endswith('.ttf'), font_list))

        # load font
        for font in font_list:
            font_path = dir_path + font
            db = QFontDatabase()
            db.addApplicationFont(font_path)


# initial widget window size
def set_base_geometry(widget, width, height, x=None, y=None, title=None, fixed=False):

    if title:
        widget.setWindowTitle(title)

    # set window init size
    widget.resize(width, height)

    # set window resize constrains
    if fixed:
        widget.setFixedSize(width, height)
    else:
        widget.setMinimumSize(width, height)

    # set window init position
    if x is None and y is None:
        cp = QDesktopWidget()
        widget.move(cp.availableGeometry().center().x() - widget.width() * 0.5,
                    cp.availableGeometry().center().y() - widget.height() * 0.5)
    elif x is None and y is not None:
        cp = QDesktopWidget()
        widget.move(cp.availableGeometry().center().x() - widget.width() * 0.5, y)
    elif x is not None and y is None:
        cp = QDesktopWidget()
        widget.move(x, cp.availableGeometry().center().y() - widget.height() * 0.5)
    else:
        widget.move(x, y)


# create a layout object
def add_layout(widget, layout_type, l_m=0, t_m=0, r_m=0, b_m=0, space=0, name=None, align=None):

    # Set layout type
    if layout_type == VERTICAL:
        layout = QVBoxLayout(widget)
    elif layout_type == HORIZONTAL:
        layout = QHBoxLayout(widget)
    elif layout_type == STACK:
        layout = QStackedLayout(widget)
    else:
        layout = QHBoxLayout(widget)

    # Margin and spacing
    layout.setContentsMargins(l_m, t_m, r_m, b_m)
    layout.setSpacing(space)

    # Set object name
    if name:
        layout.setObjectName(name)

    # Set children align
    if align:
        layout.setAlignment(align)

    return layout


# create a QPushbutton object
def add_button(widget, text=None, name=None, stylesheet=None, icon=None, icon_size=None, change_cursor=True):

    # Create object
    button = QPushButton(widget)

    # Set text on button
    if text:
        button.setText(text)

    # Set object name
    if name:
        button.setObjectName(name)

    if stylesheet:
        button.setStyleSheet(stylesheet)

    # case on whether this button has icon
    if icon:
        button.setIcon(QIcon(icon))
        if icon_size:
            button.setIconSize(QSize(icon_size, icon_size))

    # change cursor
    if change_cursor:
        button.setCursor(Qt.PointingHandCursor)

    return button


# create a QLabel object
def add_label(widget, text, width=0, height=0, name=None, align=None, stylesheet= None):

    # Create object
    label = QLabel(widget)

    if text is not "":
        label.setText(text)

    # Set object name
    if name:
        label.setObjectName(name)

    # Set align
    if align:
        label.setAlignment(align)

    # set width (if necessary)
    if width:
        label.setFixedWidth(width)

    # set height (if necessary)
    if height:
        label.setFixedHeight(height)

    if stylesheet:
        label.setStyleSheet(stylesheet)

    return label


# create a widget with a list of text to QLabel object
def add_paragraph(widget, text_list, name=None, align=None, space=0):

    # create object
    box = QFrame(widget)

    # add layout
    box_layout = add_layout(box, VERTICAL, space=space)

    for text in text_list:
        label = add_label(box, text, name=name, align=align)
        box_layout.addWidget(label)

    return box


# create an image object (QLabel)
def add_image(widget, img_name, img_type, width=0, height=0, name=None, align=None):

    img_name = load_image(img_name, img_type)

    # robust check, if valid file name
    if not os.path.isfile(img_name):
        img_name = os.getcwd() + "/src/img/default.jpg"

    label = add_label(widget, "", name=name, align=align)

    dpm = 300 / 0.0254  # ~300 DPI

    pix_map = QPixmap(img_name)

    # Optional, resize window to image size
    if width and not height:
        pix_map = pix_map.scaledToWidth(width)
    elif not width and height:
        pix_map = pix_map.scaledToHeight(height)
    elif width and height:
        if width >= height:
            pix_map = pix_map.scaledToWidth(width)
        else:
            pix_map = pix_map.scaledToHeight(height)

    label.setPixmap(pix_map)

    return label


# helper function to add input box
def add_input_box(widget, title, layout, space, align=None, hint=None, echo=False):

    # create object
    box = QFrame(widget)
    box_layout = add_layout(box, layout, space=space)

    # input box title
    box_title = add_label(box, title, align=align)

    # input
    box_input = QLineEdit()

    # no focus frame
    box_input.setAttribute(Qt.WA_MacShowFocusRect, 0)

    # Set hint on input
    if hint:
        box_input.setPlaceholderText(hint)

    # password encrypt
    if echo:
        box_input.setEchoMode(QLineEdit.Password)

    box_layout.addWidget(box_title)
    box_layout.addWidget(box_input)

    return box, box_title, box_input


# type 01 input box for login
def add_input_box_01(widget, title, hint=None, echo=False):

    layout = VERTICAL
    space = 9

    # create object
    box, box_title, box_input = add_input_box(widget, title, layout, space=space, hint=hint, echo=echo)

    box_title.setObjectName("Login_input_title")
    box_input.setObjectName("Login_input_input")

    return box, box_input


# type 02 input box for jobs
def add_input_box_02(widget, title, hint=None, echo=False, width=260, fix_width=True):

    layout = HORIZONTAL
    space = 18

    # create object
    box, box_title, box_input = add_input_box(widget, title, layout, space=space, hint=hint, echo=echo,
                                              align=(Qt.AlignRight | Qt.AlignVCenter))

    box_title.setFixedSize(90, 22)
    box_title.setObjectName("Page_input_title_01")

    box_input.setFixedHeight(22)
    box_input.setObjectName("Page_input_input_01")

    if fix_width:
        box.setFixedSize(width, 22)
    else:
        box.setFixedHeight(22)

    return box, box_input


# type 02 input box for resources
def add_input_box_03(widget, title, hint=None, echo=False, width=210, fix_width=True):

    layout = HORIZONTAL
    space = 18

    # create object
    box, box_title, box_input = add_input_box(widget, title, layout, space=space, hint=hint, echo=echo,
                                              align=(Qt.AlignRight | Qt.AlignVCenter))

    box_title.setFixedSize(80, 22)
    box_title.setObjectName("Page_input_title_02")

    box_input.setFixedHeight(22)
    box_input.setObjectName("Page_input_input_02")

    if fix_width:
        box.setFixedSize(width, 22)
    else:
        box.setFixedHeight(22)

    return box, box_input


# create a checkbox object with a checkbox and description
def add_checkbox(widget, title, title_type=LABEL, space=10, align=None, check=False):

    # Create object
    box = QFrame(widget)
    box_layout = add_layout(box, HORIZONTAL, space=space, align=align)

    # checkbox
    checkbox = QCheckBox(box)
    checkbox.setObjectName("Login_check_box_check")

    # checkbox property
    checkbox.setCursor(Qt.PointingHandCursor)
    if check:
        checkbox.setChecked(True)

    # description
    if title_type is QPUSHBUTTON:
        box_title = add_button(box, title, name="Login_check_box_title_button")
    else:
        box_title = add_label(box, title, name="Login_check_box_title_label", align=Qt.AlignVCenter)

    box_layout.addWidget(checkbox)
    box_layout.addWidget(box_title)

    if title_type is QPUSHBUTTON:
        return box, checkbox, box_title
    else:
        return box, checkbox


# create a moving animation
def add_move_animation(widget, start_x, start_y, end_x, end_y, duration=230):

    # create object
    animation = QPropertyAnimation(widget, b"geometry")

    # set duration
    animation.setDuration(duration)

    # set start/end value
    animation.setStartValue(QRect(start_x, start_y, widget.width(), widget.height()))
    animation.setEndValue(QRect(end_x, end_y,  widget.width(), widget.height()))

    return animation


# add graph scene for drawing
def add_graph_scene(widget, width=None, height=None, name=None):
    view = QGraphicsView(widget)
    scene = QGraphicsScene()

    if widget and height:
        view.setFixedSize(width, height)
    elif width and not height:
        view.setFixedWidth(width)
    elif not width and height:
        view.setFixedHeight(height)
    else:
        pass

    if name:
        view.setObjectName(name)
    view.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing)
    view.setScene(scene)

    return view, scene

