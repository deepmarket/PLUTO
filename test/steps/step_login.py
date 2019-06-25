from PyQt5.QtWidgets import QDialog

from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

from behave import use_step_matcher, when, then

from test.steps.step_helpers import assert_equal, assert_is_not, assert_is
use_step_matcher("re")


@when(r'I open the login window')
def open_login_window(context):
    context.login_window = context.__app.login
    context.current_window = "login"


@when(r'I login in to the application')
def login(context):
    assert_is_not(context.login_window, None)

    QTest.keyClicks(context.login_window.login.username, "samgomena@gmail.com")
    QTest.keyClicks(context.login_window.login.password, "password")

    QTest.mouseClick(context.login_window.login.login_button, Qt.LeftButton)


@when(r'I enter "(.*)" in the (username|password) input box')
def enter_login_input_text(context, text, dialog_box):
    assert_is_not(context.login_window, None)

    if dialog_box == "username":
        QTest.keyClicks(context.login_window.login.username, text)
    elif dialog_box == "password":
        QTest.keyClicks(context.login_window.login.password, text)


@then(r'the (username|password) input box text should be "(.*)"')
def verify_login_input_text(context, dialog_box, text):
    assert_is_not(context.login_window, None)

    if dialog_box == "username":
        assert_equal(context.login_window.login.username.text(), text)
    elif dialog_box == "password":
        assert_equal(context.login_window.login.password.text(), text)


@when(r'I click the (log in|create an account|login here|create account) button')
def click_login_window_button(context, btn):
    assert_is_not(context.login_window, None)

    if btn == "log in":
        QTest.mouseClick(context.login_window.login.login_button, Qt.LeftButton)
    elif btn == "create an account":
        QTest.mouseClick(context.login_window.login.to_create_button, Qt.LeftButton)
        context.current_window = "account"
    elif btn == "back to login":
        QTest.mouseClick(context.login_window.create.to_login_button, Qt.LeftButton)
        context.current_window = "login"
    elif btn == "create account":
        QTest.mouseClick(context.login_window.create.create_button, Qt.LeftButton)


@then(r'the login hint text should be "(.*)"')
def verify_login_input_text(context, text):
    assert_is_not(context.login_window, None)

    assert_equal(context.login_window.login.login_hint.text(), text)


@then(r'I should be able to log in to the application')
def verify_can_log_in(context):
    assert_equal(context.login_window.result(), QDialog.Accepted)
