"""

    This file contains all helper function for ui aspect implementation.
    Any functional helper function for interactive component can be found at another util.py file.

"""

import os

from PyQt5.QtWidgets import QLineEdit, QLabel

from PyQt5.QtCore import Qt


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
