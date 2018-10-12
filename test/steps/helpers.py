
from behave import use_step_matcher, given, when, then, step
use_step_matcher("re")


def assert_equal_wrapper(lhs, rhs):
    assert lhs == rhs, f"'{lhs}' does not equal '{rhs}'"


@given(r'the application is in headless mode')
def api_is_up(context):
    from os import environ
    environ['HEADLESS'] = True


@when(r'I spin up the application')
def start_application_execution(context):
    from PyQt5.QtWidgets import QApplication
    if QApplication.instance() is None:
        app = QApplication([])
        context.app_ = app


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