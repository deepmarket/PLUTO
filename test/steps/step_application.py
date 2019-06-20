
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

from behave import use_step_matcher, when, then

from test.steps.step_helpers import assert_equal, assert_is_not, assert_is_true, assert_is_not_true
use_step_matcher("re")


@when(r'I open the application window')
def open_application(context):
    context.app = context.__app.app
    assert_is_not(context.app, None)


@when(r'I click on the (dashboard|resources|jobs|settings) tab')
def open_main_tab(context, tab):
    # Get tab by attribute name; if the attribute name changes, this will fail
    tab = getattr(context.app.sidebar, tab, None)
    QTest.mouseClick(tab, Qt.LeftButton)


@then(r'the current tab should be the (dashboard|resources|jobs|settings) tab')
def verify_main_tab(context, tab):
    from dashboard import Dashboard
    from resources import Resources
    from jobs import Jobs
    from settings import Settings

    check_type = lambda type_: assert_equal(type(context.app.main_window.stack.currentWidget()), type_)

    if tab == "dashboard":
        check_type(Dashboard)
    elif tab == "resources":
        check_type(Resources)
    elif tab == "jobs":
        check_type(Jobs)
    elif tab == "settings":
        check_type(Settings)


@when(r'I logout of the application')
def logout_of_application(context):
    QTest.mouseClick(context.app.navigation.menu_button, Qt.LeftButton)
    QTest.mouseClick(context.app.account.logout, Qt.LeftButton)


@then(r'the (application|login) window should be (visible|hidden)')
def verify_window_visibility(context, window, visibility):
    # Define assertion helper based on visibility request
    vis_check = assert_is_true if visibility == "visible" else assert_is_not_true

    if window == "application":
        vis_check(context.app.isVisible())
    elif window == "login":
        vis_check(context.login_window.isVisible())

