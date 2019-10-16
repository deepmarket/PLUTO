
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from dashboard import Dashboard
from resources import Resources
from jobs import Jobs
from settings import Settings
from behave import use_step_matcher, when, then
from step_helpers import assert_equal, assert_is_not, assert_is_true, assert_is_not_true
use_step_matcher("re")


@when(r'I open the resources window')
def open_application(context):
    context.resources_window = context.__app.resources
    assert_is_not(context.app, None)


@when(r'I click on the Add button')
def add_resources(context, button):
    assert_is_not(context.login_window, None)

    QTest.mouseClick(context.app.resources.add, Qt.LeftButton)

@then(r'the window will switch to add resource page')
def verify_add_button(context):
    assert_equal(context.resources_window.add_view.result(), QDialog.Accepted)

@when(r'I click on the Submit button')
def submit_resource(context, button):
    assert_is_not(context.login_window.add_view, None)

    QTest.mouseClick(context.app.resources.add_view.submit, Qt.LeftButton)