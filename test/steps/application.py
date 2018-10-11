from main import Login
from src.app import App

from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

from behave import use_step_matcher, given, when, then, step

from test.steps.helpers import assert_equal_wrapper as assert_
use_step_matcher("re")


@when(r'I open the login dialog')
def open_login_window(context):
    context.login_window = Login()
    context.login_window.show()


@when(r'I enter "(.*)" in the (username|password) input box')
def enter_login_input_text(context, text, dialog_box):
    if dialog_box == "username":
        context.login_window.login.username.setText(text)
    elif dialog_box == "password":
        context.login_window.login.pwd.setText(text)


@then(r'the (username|password) input box text should be "(.*)"')
def verify_login_input_text(context, dialog_box, text):
    if dialog_box == "username":
        assert context.login_window.login.username.text() == text
    elif dialog_box == "password":
        assert context.login_window.login.pwd.text() == text


@when(r'I click the login button')
def click_the_button(context, ):
    context.login_window.login.login_button.click()


@then(r'the login hint text should be "(.*)"')
def verify_login_input_text(context, text):
    assert_(context.login_window.login.login_hint.text(), text)


@then(r'I should be able to log in to the application')
def verify_can_log_in(context):
    assert context.login_window.exec_()


@when(r'I open the application window')
def open_application(context):
        context.app = App()


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




