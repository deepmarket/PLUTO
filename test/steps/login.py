from PyQt5.QtWidgets import QDialog

from src.login import Login

from PyQt5.QtTest import QTest

from behave import use_step_matcher, given, when, then, step

from test.steps.helpers import assert_equal_wrapper as assert_
use_step_matcher("re")


@when(r'I open the login window')
def open_login_window(context):
    # context.login_window = MainApp().login
    context.login_window = Login()
    context.login_window.show()


@when(r'I login in to the application')
def login(context):
    context.login_window.login.username.setText("samgomena@gmail.com")
    context.login_window.login.pwd.setText("password")
    context.login_window.login.login_button.click()


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
    assert context.login_window.result() == QDialog.Accepted
