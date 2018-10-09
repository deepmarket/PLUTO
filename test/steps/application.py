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
    print(tab)
    if tab == "dashboard":
        context.app.on_dashboard_clicked()
    elif tab == "resources":
        print(tab)
        # context.app.sidebar.resources
        QTest.mouseClick(context.app.sidebar.resources, Qt.LeftButton)
    elif tab == "jobs":
        context.app.on_jobs_clicked()


@then(r'the current tab should be the (dashboard|resources|jobs) tab')
def verify_tab(context, tab):
    print(context.app.main_window.stack.currentWidget())
    # if tab is "dashboard":
    #     context.app.sidebar.dashboard.click()
    # elif tab is "resources":
    #     context.app.sidebar.resources.click()
    # elif tab is "jobs":
    #     context.app.sidebar


@when(r'I execute the application')
def execute(context):
    context.app_.exec_()




