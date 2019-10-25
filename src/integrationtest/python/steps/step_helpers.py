
from behave import use_step_matcher, given, when, then, step

from api import Api
from mainapp import MainApp
from main import AppContext


use_step_matcher("re")


def assert_is_true(lhs):
    assert lhs is True, f"'{lhs}' is not true"


def assert_is_not_true(lhs):
    assert lhs is not True, f"'{lhs}' is not true"


def assert_equal(lhs, rhs):
    assert lhs == rhs, f"'{lhs}' does not equal '{rhs}'"


def assert_not_equal(lhs, rhs):
    assert lhs != rhs, f"'{lhs}' equal's '{rhs}'"


def assert_is(lhs, rhs):
    assert lhs is rhs, f"'{lhs}' is '{rhs}'"


def assert_is_not(lhs, rhs):
    assert lhs is not rhs, f"'{lhs}' is not '{rhs}'"


@given(r'the application is in headless mode')
def api_is_up(context):
    from os import environ
    environ['HEADLESS'] = True


@given(r'the user is logged out of the application')
def ensure_user_is_logged_out(context):
    context.ensure_logout = True


@when(r'I spin up the application')
def start_application_execution(context):
    from PyQt5.QtWidgets import QApplication
    if QApplication.instance() is None:
        app = QApplication([])
        context._app = app

    cxt = AppContext()
    if context.ensure_logout:
        with Api(cxt, "logout") as api_logout:
            api_logout.get()

    __app = MainApp(cxt=cxt)
    context.__app = __app


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
