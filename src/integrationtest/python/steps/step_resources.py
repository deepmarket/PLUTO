
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QCheckBox
from dashboard import Dashboard
from resources import Resources, ResourcesAddView, ResourcesController 
from interfaces.helper import get_children
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
    

@when(r'I click on the (Add|Cancel|Next|Back) button')
def add_resources(context, button):
    context.resources_window = context.app.main_window.stack.currentWidget()

    if button == "Add":
        QTest.mouseClick(context.resources_window.controller.add, Qt.LeftButton)
    elif button == "Cancel":
        QTest.mouseClick(context.resources_window.add_view.cancel, Qt.LeftButton)
    elif button == "Next":
        QTest.mouseClick(context.resources_window.add_view.next_page, Qt.LeftButton)
    elif button == "Back":
        QTest.mouseClick(context.resources_window.add_view.back, Qt.LeftButton)


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
def enter_planning_input_text(context, text, dialog_box):
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
def verify_planning_input_text(context, dialog_box, text):
    assert_is_not(context.resources_window.add_view.tech_sections, None)

    if dialog_box == "machine name":
        assert_equal(context.resources_window.add_view.machine_name.text(), text)
    elif dialog_box == "GPUs":
        assert_equal(context.resources_window.add_view.cpu_gpu.text(), text)
        # assert_equal(context.resources_window.add_view.current_cpu_gpu.objectName(), "config_frame_green")
    elif dialog_box == "Cores":
        assert_equal(context.resources_window.add_view.cores.text(), text)
    elif dialog_box == "RAM":
        assert_equal(context.resources_window.add_view.ram.text(), text)
    
@then(r'the (Compute|Cores|RAM) config box in machine configuration section should be (Green|Red)')
def verify_valid_machine_input(context, dialog_box, color):
    assert_is_not(context.resources_window.add_view.tech_sections, None)

    color = "config_frame_green" if color == "Green" else "config_frame_red"
    
    if dialog_box == "Compute":
        assert_equal(context.resources_window.add_view.current_cpu_gpu.objectName(), color)
    elif dialog_box == "Cores":
        assert_equal(context.resources_window.add_view.current_cores.objectName(), color)
    elif dialog_box == "RAM":
        assert_equal(context.resources_window.add_view.current_ram.objectName(), color)

@when(r'I click on the (rent immediately|rent schedule|rent reserve) button')
def click_check_box_button(context, button):

    if button == "rent immediately":
        button = context.resources_window.add_view.rent_immediately_box.button
    elif button == "rent schedule":
        button = context.resources_window.add_view.rent_schedule_box.button
    elif button == "rent reserve":
        button = context.resources_window.add_view.rent_reserve_box.button
        
    QTest.mouseClick(button, Qt.LeftButton)


@then(r'the attendance box current select is (rent immediately|rent schedule|rent reserve) box')
def verify_check_box_click(context, check_box):
    assert_is_not(context.resources_window.add_view.eco_sections, None)

    if check_box == "rent immediately":
        assert_equal(context.resources_window.add_view.rent_immediately_box.flag, True)
    elif check_box == "rent schedul":
        assert_equal(context.resources_window.add_view.rent_schedule_box.flag, True)
    elif check_box == "rent reserve":
        assert_equal(context.resources_window.add_view.rent_reserve_box.flag, True)


@when(r'I select (start|end) time at "(.*)" at rent (schedule|reserve) box')
def select_time(context, slot, time, type):
    if type == "schedule":
        widget = context.resources_window.add_view.rent_schedule_box
    elif type == "reserve":
        widget = context.resources_window.add_view.rent_reserve_box
        
    children = get_children(widget, QComboBox)

    if slot == "start":
        combo = children[0]
    elif slot == "end":
        combo = children[1]
    
    num = time.split(" ")

    count = int(num[0])

    if num[1] == "PM":
        count += 12

    QTest.mouseClick(combo, Qt.LeftButton)

    for i in range(count - 1):
        QTest.keyClick(combo, Qt.Key_Down)

    QTest.keyClick(combo, Qt.Key_Enter)
    

@then(r'the (start|end) time at rent (schedule|reserve) box text should be "(.*)"')
def verify_time_select(context, slot, type, time):
    if type == "schedule":
        widget = context.resources_window.add_view.rent_schedule_box
    elif type == "reserve":
        widget = context.resources_window.add_view.rent_reserve_box
        
    children = get_children(widget, QComboBox)

    if slot == "start":
        assert_equal(children[0].currentText(), time)
    elif slot == "end":
        assert_equal(children[1].currentText(), time)
        

@when(r'I select date on "(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)"')
def select_date(context, date):
    weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    index = weekday.index(date)

    children = get_children(context.resources_window.add_view.rent_reserve_box, QCheckBox)

    QTest.mouseClick(children[index], Qt.LeftButton)

@then(r'the select date at rent reserve box text should be "(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)"')
def verify_date_select(context, date):
    weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    index = weekday.index(date)

    children = get_children(context.resources_window.add_view.rent_reserve_box, QCheckBox)

    assert_equal(children[index].isChecked(), True)
    