from PyQt5.QtWidgets import QDialog

from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

from behave import use_step_matcher, when, then

from src.integrationtest.python.steps.step_helpers import assert_equal, assert_is_not, assert_is

use_step_matcher("re")

