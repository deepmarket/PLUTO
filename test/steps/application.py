from src.app import App

from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

from behave import use_step_matcher, given, when, then, step
use_step_matcher("re")


@given(r'the application is in headless mode')
def api_is_up(context):
    from os import environ
    environ['HEADLESS'] = True


@when(r'I wait (\d+) (second|seconds|minute|minutes|hour|hours)')
def wait(context, timeout, denomination):
    from time import sleep
    timeout = int(timeout)

    if "second" in denomination:
        sleep(timeout)
    elif "minute" in denomination:
        timeout *= 60
        sleep(timeout)
    elif "hour" in denomination:
        timeout *= (60 * 60)
        sleep(timeout)


@when(r'I stand up the application')
def open_application(context):
    from PyQt5.QtWidgets import QApplication
    if QApplication.instance() is None:
        app = QApplication([])
        context.app_ = app
        context.app = App()


@when(r'I click on the (dashboard|resources|jobs) tab')
def open_tab(context, tab):
    if tab == "dashboard":
        context.app.on_dashboard_clicked()
    elif tab == "resources":
        # context.app.sidebar.resources
        QTest.mouseClick(context.app.sidebar.resources, Qt.LeftButton)
    elif tab == "jobs":
        context.app.on_jobs_clicked()


@then(r'the current tab should be the (dashboard|resources|jobs) tab')
def verify_tab(context, tab):
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




