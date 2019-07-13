"""

    This file contains all helper function for ui aspect implementation.
    Any functional helper function for interactive component can be found at another util.py file.

"""

import os


"""
    Find a file in a given path string
    reference: https://github.com/yahoo/TensorFlowOnSpark/blob/e2f5cc45f95812d163e75b6ddb9c4661261d3bb0/tensorflowonspark/util.py#L57

    :param path: base path of the file
    :param file: the name of the file, include postfix
    :return: if exist file, return the path of the file, otherwise, return False
"""
def load_path(path, file):
    for p in path.split(os.pathsep):
        candidate = os.path.join(p, file)
    if os.path.exists(candidate) and os.path.isfile(candidate):
        return candidate
    return False

"""
    Find all child widgets belong to the type (or with given object name)
    Replace old object name to given new object name.

    :param widget: parent widget
    :param child_type: destinated child widgets type
    :param new_name: the object name that would be set the matched children
    :param old_name: optional, the name that child widgets currently have
    :return None
"""
def change_objects_name(widget, child_type, new_name:str, *args):
    # if None, children = []
    children = [child for child in widget.findChildren(child_type, *args)]

    for child in children:
        child.setObjectName(new_name)
