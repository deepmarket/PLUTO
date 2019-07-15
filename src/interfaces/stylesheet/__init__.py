import os

from ..util import load_path

def read_stylesheet(file_name):
    path = load_path(os.getcwd() + "/interfaces/stylesheet/", file_name)
    return open(path).read() if path else None


# stylesheets
resources_add_view_style = read_stylesheet("resources/add_view.qss")
resources_controller_style = read_stylesheet("resources/controller.qss")
