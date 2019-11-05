from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from dashboard import Dashboard
from resources import Resources, ResourcesAddView, ResourcesController 
from jobs import Jobs, JobsAddView, JobsController
from settings import Settings
from behave import use_step_matcher, when, then
from step_helpers import assert_equal, assert_is_not, assert_is_true, assert_is_not_true
use_step_matcher("re")

@then(r'I open the jobs window')
def open_resources(context):
    context.app = context.__app.app

    check_type = lambda type_: assert_equal(type(context.app.main_window.stack.currentWidget()), type_)
    assert_is_not(check_type(Jobs), True)

"""
@when(r'I click on the (Add Jobs|Job Lists) button')
def add_jobs(context, button):
    context.jobs_window = context.app.main_window.stack.currentWidget()

    if button == "Add Jobs":
        QTest.mouseClick(context.jobs_window.add_view_button, Qt.LeftButton)
    elif button == "Job Lists":
        QTest.mouseClick(context.jobs_window.controller_button, Qt.LeftButton)

@then(r'the window will switch to (add jobs|job lists) page')
def verify_button(context, page):
    if page == "add jobs":
        assert_equal(type(context.jobs_window._stack.currentWidget()), JobsAddView)
    elif page == "job lists":
        assert_equal(type(context.jobs_window._stack.currentWidget()), JobsController)
"""
