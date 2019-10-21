
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from dashboard import Dashboard
from resources import Resources, ResourcesAddView
from jobs import Jobs
from settings import Settings
from behave import use_step_matcher, when, then
from step_helpers import assert_equal, assert_is_not, assert_is_true, assert_is_not_true
use_step_matcher("re")


@then(r'I open the resources window')
def open_resources(context):
    context.app = context.__app.app

    check_type = lambda type_: assert_equal(type(context.app.main_window.stack.currentWidget()), type_)
    assert_is_not(check_type(Resources), True)
    

@when(r'I click on the Add button')
def add_resources(context):
    context.resources_window = context.app.main_window.stack.currentWidget()

    QTest.mouseClick(context.resources_window.controller.add, Qt.LeftButton)

@then(r'the window will switch to add resource page')
def verify_add_button(context):
    check_type = lambda type_: assert_equal(type(context.resources_window._stack.currentWidget()), type_)

    assert_is_not(check_type(ResourcesAddView), True)
    
    
"""
@when(r'I click on the Submit button')
def submit_resource(context, button):
    assert_is_not(context.login_window.add_view, None)

    QTest.mouseClick(context.app.resources.add_view.submit, Qt.LeftButton)
"""