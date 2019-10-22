
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from dashboard import Dashboard
from resources import Resources, ResourcesAddView, ResourcesController 
from jobs import Jobs
from settings import Settings
from behave import use_step_matcher, when, then
from step_helpers import assert_equal, assert_is_not, assert_is_true, assert_is_not_true
use_step_matcher("re")


@then(r'I open the resources window')
def open_resources(context):
    context.app = context.__app.app

    check_type = lambda type_: assert_equal(type(context.app.main_window.stack.currentWidget()), type_)
    assert_is_not(check_type(Resources), True)
    

@when(r'I click on the (Add|Cancel|Next) button')
def add_resources(context, button):
    context.resources_window = context.app.main_window.stack.currentWidget()

    if button == "Add":
        QTest.mouseClick(context.resources_window.controller.add, Qt.LeftButton)
    elif button == "Cancel":
        QTest.mouseClick(context.resources_window.add_view.cancel, Qt.LeftButton)
    elif button == "Next":
        QTest.mouseClick(context.resources_window.add_view.next_page, Qt.LeftButton)


@then(r'the window will switch to (add resource|controller|next) page')
def verify_button(context, page):
    
    if page == "add resource":
        assert_equal(context.resources_window._stack.currentWidget().stack.currentWidget(), context.resources_window._stack.currentWidget().tech_sections)
    elif page == "controller":
        assert_equal(type(context.resources_window._stack.currentWidget()), ResourcesController)
    elif page == "next":
        assert_equal(context.resources_window._stack.currentWidget().stack.currentWidget(), context.resources_window._stack.currentWidget().eco_sections)
        
@then(r'the planning hint text should be "(.*)"')
def verify_planing_input_text(context, text):
    assert_is_not(context.resources_window.add_view.tech_sections, None)

    assert_equal(context.resources_window.add_view.planning_hint.text(), text)

@when(r'I enter "(.*)" in the (machine name|GPUs|Cores|RAM) input box')
def enter_login_input_text(context, text, dialog_box):
    assert_is_not(context.resources_window.add_view.tech_sections, None)

    if dialog_box == "machine name":
        QTest.keyClicks(context.resources_window.add_view.machine_name.input_field, text)
    elif dialog_box == "GPUs":
        QTest.keyClicks(context.resources_window.add_view.cpu_gpu.input_field, text)
    elif dialog_box == "Cores":
        QTest.keyClicks(context.resources_window.add_view.cores.input_field, text)
    elif dialog_box == "RAM":
        QTest.keyClicks(context.resources_window.add_view.ram.input_field, text)


@then(r'the (machine name|GPUs|Cores|RAM) input box text should be "(.*)"')
def verify_login_input_text(context, dialog_box, text):
    assert_is_not(context.resources_window.add_view.tech_sections, None)

    if dialog_box == "machine name":
        assert_equal(context.resources_window.add_view.machine_name.text(), text)
    elif dialog_box == "GPUs":
        assert_equal(context.resources_window.add_view.cpu_gpu.text(), text)
    elif dialog_box == "Cores":
        assert_equal(context.resources_window.add_view.cores.text(), text)
    elif dialog_box == "RAM":
        assert_equal(context.resources_window.add_view.ram.text(), text)
    