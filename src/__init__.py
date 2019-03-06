
# This allows test modules to import the `src` module properly
from sys import path as sys_path
from os import path as os_path
sys_path.append(os_path.join(os_path.dirname(__file__), '.'))
