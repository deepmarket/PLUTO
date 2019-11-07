
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

from behave import use_step_matcher, when, then

from src.integrationtest.python.steps.step_helpers import assert_equal, assert_is_not, assert_is_true, assert_is_not_true
use_step_matcher("re")


@when(r'I click on the resources (workspace|list) view tab')
def click_resources_list_view(context, tab):
    tab = getattr(context.app.main_window.stack, f"{tab}_button", None)
    assert_is_not(tab, None)

    QTest.mouseClick(context.app.main_window.stack.list_button, Qt.LeftButton)
