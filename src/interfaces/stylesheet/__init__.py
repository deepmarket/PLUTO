import os

from ..util import load_path

def read_stylesheet(file_name):
    path = load_path(os.getcwd() + "/interfaces/stylesheet/", file_name)
    return open(path).read() if path else None

# stylesheets
resources_style = read_stylesheet("resources.qss")