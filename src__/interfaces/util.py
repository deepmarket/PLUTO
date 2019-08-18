"""

    This file contains all helper function for ui aspect implementation.
    Any functional helper function for interactive component can be found at another util.py file.

"""

import os

from PyQt5.QtWidgets import QLineEdit


def load_path(path, _file):
    """
    Find a file in a given path string
    reference: https://github.com/yahoo/TensorFlowOnSpark/blob/e2f5cc45f95812d163e75b6ddb9c4661261d3bb0/tensorflowonspark/util.py#L57

    :param path: base path of the file
    :param _file: the name of the file, include postfix
    :return: if exist file, return the path of the file, otherwise, return False
    """
    for p in path.split(os.pathsep):
        candidate = os.path.join(p, _file)
        if os.path.exists(candidate) and os.path.isfile(candidate):
            return candidate
    return False


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
