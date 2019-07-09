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