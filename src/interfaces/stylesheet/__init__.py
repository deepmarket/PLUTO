import os

from ..util import load_path

def read_stylesheet(file_name):
    path = load_path(os.getcwd() + "/interfaces/stylesheet/", file_name)
    ret = None
    with open(path) as file:
        ret = file.read()
    return ret


def read_icon(file_name):
    return load_path(os.getcwd() + "/img/", file_name)


# stylesheets
popup_style = read_stylesheet("popup.qss")

resources_add_view_style = read_stylesheet("resources/add_view.qss")
resources_controller_style = read_stylesheet("resources/controller.qss")
