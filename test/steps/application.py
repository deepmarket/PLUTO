from src.app import App

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
        context.app = App()


# @when(u'I close the application')
# def close_application(context):
#     from sys import exit
#     exit(context.app)


@then(r'the request should reply with a status of (\d{3})')
@then(r'the request should reply with a status of (\w+)')
def verify_api_request_to(context, status):
    pass

