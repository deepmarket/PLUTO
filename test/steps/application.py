from src.app import App

from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt, pyqtSignal

from behave import use_step_matcher, given, when, then, step

from test.steps.helpers import assert_equal_wrapper as assert_
use_step_matcher("re")


@when(r'I open the application window')
def open_application(context):
    # Create a fake signal to appease the testing gods
    fake_signal = pyqtSignal()
    context.app = App(fake_signal)


@when(r'I click on the (dashboard|resources|jobs) tab')
def open_main_tab(context, tab):
    if tab == "dashboard":
        context.app.on_dashboard_clicked()
    elif tab == "resources":
        # context.app.sidebar.resources
        QTest.mouseClick(context.app.sidebar.resources, Qt.LeftButton)
    elif tab == "jobs":
        context.app.on_jobs_clicked()


@then(r'the current tab should be the (dashboard|resources|jobs) tab')
def verify_main_tab(context, tab):
    from src.dashboard import Dashboard
    from src.resources import Resources
    from src.jobs import Jobs

    check_type = lambda type_: isinstance(context.app.main_window.stack.currentWidget(), type_)

    if tab == "dashboard":
        check_type(Dashboard)
    elif tab == "resources":
        isinstance(context.app.main_window.stack.currentWidget(), Resources)
    elif tab == "jobs":
        isinstance(context.app.main_window.stack.currentWidget(), Jobs)


@when(r'I execute the application')
def execute(context):
    context.app_.exec_()




