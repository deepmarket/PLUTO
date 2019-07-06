"""
    helper functions on construct GUI
"""

import os
import re
import datetime
import urllib.request
import json

from PyQt5.QtCore import (Qt, QSize, QRect, QPropertyAnimation, QRectF, QPoint, QTimer, QPointF,
                          QSequentialAnimationGroup, QTimer)
from PyQt5.QtGui import QPixmap, QIcon, QFontDatabase, QPainter, QFont, QColor, QPen, QBrush, QPolygonF, QPainterPath
from PyQt5.QtWidgets import (QDesktopWidget, QPushButton, QLabel, QFrame, QLineEdit, QCheckBox,
                             QVBoxLayout, QHBoxLayout, QStackedLayout, QGraphicsView, QGraphicsScene,
                             QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsPolygonItem, QGraphicsPathItem,
                             QGraphicsTextItem, QGraphicsDropShadowEffect, QDialog, QMainWindow, QSizePolicy,
                             QSpacerItem, QTableWidget, QHeaderView, QAbstractItemView, QTableWidgetItem, QMessageBox)

from uix.stylesheet import *
from uix.config import *


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


# check
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


# check
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


# check
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


# check
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


# check
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


def add_input(widget, height=0, name=None, hint=None, echo=False):
    input_bar = QLineEdit(widget)

    # no focus frame
    input_bar.setAttribute(Qt.WA_MacShowFocusRect, 0)

    if height:
        input_bar.setFixedHeight(height)

    # Set object name
    if name:
        input_bar.setObjectName(name)

    # Set hint on input
    if hint:
        input_bar.setPlaceholderText(hint)

    # password encrypt
    if echo:
        input_bar.setEchoMode(QLineEdit.Password)

    return input_bar


# helper function to add input box
def add_input_box(widget, title, space=0, l_m=0, r_m=0, align=None, hint=None, echo=False):

    # create object
    box = QFrame(widget)
    box_layout = add_layout(box, HORIZONTAL, l_m=l_m, r_m=r_m, space=space)

    # input box title
    box_title = add_label(box, title, align=align)
    box_layout.addWidget(box_title)

    # input
    box_input = add_input(widget, hint=hint, echo=echo)
    box_layout.addWidget(box_input)

    return box, box_title, box_input


# input box for login
def add_login_input_box(widget, title, title_width=160, hint=None, echo=False):

    # create object
    box, box_title, box_input = add_input_box(widget, title, l_m=30, r_m=30, space=9, hint=hint, echo=echo)

    box.setFixedHeight(52)

    box.setObjectName("Login_input_box")

    box_title.setFixedSize(title_width, 52)
    box_title.setObjectName("Login_input_title")

    box_input.setFixedHeight(52)
    box_input.setObjectName("Login_input_input")

    return box, box_input


# type 02 input box for jobs
def add_page_input_box(widget, title, title_width, space, width=258, stylesheet=None, hint=None,
                       echo=False, fix_width=True):

    # create object
    box, box_title, box_input = add_input_box(widget, title, space=space, hint=hint, echo=echo,
                                              align=(Qt.AlignRight | Qt.AlignVCenter))

    box_title.setFixedSize(title_width, 30)
    box_title.setObjectName("Page_input_title")

    box_input.setFixedHeight(30)

    if stylesheet:
        box_input.setStyleSheet(stylesheet)

    if fix_width:
        box.setFixedSize(width, 30)
    else:
        box.setFixedHeight(30)

    return box, box_input


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


# return a greeting
def add_greeting():
    now = datetime.datetime.now()

    if now.hour < 12:
        return "Good morning"
    elif 12 <= now.hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


# return a menu icon
def add_menu_icon(width):

    height = 3
    pix = QPixmap(width, width)
    pix.fill(Qt.transparent)
    painter = QPainter()

    painter.begin(pix)

    painter.setPen(Qt.NoPen)
    painter.setBrush(QBrush(QColor(COLOR_01)))
    painter.drawRect(QRectF(0, 2, width, height))
    painter.drawRect(QRectF(0, height + 2 * 2, width, height))
    painter.drawRect(QRectF(0, height * 2 + 3 * 2, width, height))

    painter.end()

    return QIcon(pix)


# check
# add a section, return frame, and frame_layout
def add_frame(widget, layout=VERTICAL, height=None, width=None, name=None, stylesheet=None,
              t_m=0, b_m=0, l_m=0, r_m=0, space=0):
    section_frame = QFrame(widget)
    if height:
        section_frame.setFixedHeight(height)
    if width:
        section_frame.setFixedWidth(width)
    if stylesheet:
        section_frame.setStyleSheet(stylesheet)
    if name:
        section_frame.setObjectName(name)

    section_layout = add_layout(section_frame, layout, t_m=t_m, b_m=b_m, l_m=l_m, r_m=r_m, space=space)

    return section_frame, section_layout


# return config box
def add_config_box(widget, title, box_width=200):
    box = QFrame(widget)
    box.setFixedWidth(box_width)
    box_layout = add_layout(box, HORIZONTAL, l_m=11, r_m=11)

    title = add_label(box, title, align=Qt.AlignVCenter)
    box_layout.addWidget(title)

    spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
    box_layout.addItem(spacer)

    value = add_label(box, "", align=Qt.AlignVCenter)
    box_layout.addWidget(value)

    return box


# return outer frame, label box and button
def add_price_box(widget, title, box_width=307, box_height=37, space=28):
    frame = QFrame(widget)
    frame.setFixedSize(box_width, box_height)
    frame_layout = add_layout(frame, HORIZONTAL, space=space)

    button = add_button(frame)
    frame_layout.addWidget(button)

    box = QFrame(frame)
    frame_layout.addWidget(box)
    box_layout = add_layout(box, HORIZONTAL, l_m=9, r_m=25)

    title = add_label(box, title)
    box_layout.addWidget(title)

    spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
    box_layout.addItem(spacer)

    value = add_label(box, "0 credit / Hr")
    box_layout.addWidget(value)

    return frame, box, button


# helper function to add widgets in _init_ui() in JobWorkspace() class
def add_labels(layout, frame, texts, style, alignment):
    for text in texts:
        to_add = add_label(frame, text, stylesheet=style, align=alignment)
        layout.addWidget(to_add)


# helper function to transition between scheme highlighting in JobWorkspace() class
def set_frame(widget, num, frame):
    if widget.select_scheme != num:
        # find the previous selected frame
        if widget.select_scheme == 1:
            prev = widget.scheme_01_frame
        elif widget.select_scheme == 2:
            prev = widget.scheme_02_frame
        elif widget.select_scheme == 3:
            prev = widget.scheme_03_frame
        else:
            prev = widget.scheme_04_frame

        # set frame to disable stylesheet
        prev.setStyleSheet(Page_scheme_box_disable)

        # find all QLabel children within the frame
        labels = prev.findChildren(QLabel)

        # set labels to disable stylesheet
        for label in labels:
            label.setStyleSheet(Page_scheme_label_disable)

        # set flag
        widget.select_scheme = num

        # set frame to active stylesheet
        frame.setStyleSheet(Page_scheme_box)

        # find all QLabel children within the frame
        labels = frame.findChildren(QLabel)

        # set labels to enable stylesheet
        for label in labels:
            label.setStyleSheet(Page_scheme_label)


# helper function for add_data() in JobList() class
def add_row(widget, column, data, row):
    for i in range(column):
        widget.setItem(row, i, QTableWidgetItem(data[i]))

        if widget.item(row, i) is not None:
            # not allow user edit ip address
            if i == 1:
                widget.item(row, i).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            widget.item(row, i).setTextAlignment(Qt.AlignCenter)
            widget.item(row, i).setFont(QFont("Helvetica Neue", 12, QFont.Light))


def verify_ip_address(ip_address):
    # get data from master json
    with urllib.request.urlopen("http://" + MASTER_IP + ":8443/json/") as url:
        data = json.loads(url.read().decode())

    # open workers
    # error handle, no worker in data
    if 'workers' not in data:
        return False

    # workers exist, then find ip_address from it
    data = data['workers']
    for dat in data:
        if dat['host'] == ip_address:
            return False

    return True


# this function ask fro the machine config by using ip_address
def load_machine_config(ip_address):
    # get data from master json
    with urllib.request.urlopen("http://" + MASTER_IP + ":8443/json/") as url:
        data = json.loads(url.read().decode())

    # open workers
    # error handle, no worker in data
    if 'workers' not in data:
        return 0, 0

    data = data['workers']
    for dat in data:
        print(dat)
        if dat['host'] == ip_address:
            return dat['cores'] - dat['coresused'], round((dat['memory'] - dat['memoryused'])/1024, 1)

    return 0, 0
