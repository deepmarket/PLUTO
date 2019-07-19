"""

    This module generate serveral combination frame based object.

"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from .button import Button, RadioButton
from .frame import Frame
from .groupbox import GroupBox
from .label import Label
from .layout import HorizontalLayout
from .lineedit import LineEdit
from .spacer import HorizontalSpacer


class BaseTwoLabelFrame(Frame):

    label_one : Label = None
    label_two : Label = None

    def __init__(self, widget, **kwargs):
        super(BaseTwoLabelFrame, self).__init__(widget, **kwargs)

        kwargs.pop('name', None)
        get_param = lambda x : kwargs.get(x)

        label_one_name = get_param("label_one_name")
        label_two_name = get_param("label_two_name")

        label_one_text = get_param("label_one_text")
        label_two_text = get_param("label_two_text")

        layout = HorizontalLayout(self)

        self.label_one = Label(self, name=label_one_name, **kwargs)
        self.set_label_one_text(label_one_text)
        layout.addWidget(self.label_one)

        spacer = HorizontalSpacer()
        layout.addItem(spacer)

        self.label_two = Label(self, name=label_two_name, **kwargs)
        self.set_label_two_text(label_two_text)
        layout.addWidget(self.label_two)

    def set_label_one_text(self, text:str):
        self.label_one.setText(text)

    def set_label_two_text(self, text:str):
        self.label_two.setText(text)

    def get_label_one(self):
        return self.label_one

    def get_label_two(self):
        return self.label_two


class SectionTitleFrame(BaseTwoLabelFrame):

    def __init__(self, widget, **kwargs):
        super(SectionTitleFrame, self).__init__(widget,
                                                name="section_title_frame",
                                                label_one_name="section_title",
                                                label_two_name="section_hint",
                                                align=Qt.AlignVCenter, **kwargs)


class ConfigFrame(BaseTwoLabelFrame):

    def __init__(self, widget, **kwargs):
        super(ConfigFrame, self).__init__(widget, name="config_frame",
                                          align=Qt.AlignVCenter, **kwargs)

    def setTitle(self, text:str):
        super().set_label_one_text(text)

    def title(self):
        return self.label_one.text()

    def setText(self, text:str):
        super().set_label_two_text(text)

    def text(self):
        return self.label_two.text()

    def green(self):
        self.setObjectName("config_frame_green")

    def red(self):
        self.setObjectName("config_frame_red")

    def reset(self):
        super().set_label_two_text("-")
        self.setObjectName("config_frame")


class BaseInputFrame(Frame):

    title       : Label = None
    input_field : LineEdit = None
    layout      : HorizontalLayout = None

    def __init__(self, widget, **kwargs):

        super(BaseInputFrame, self).__init__(widget, **kwargs)

        # Lambda func grab input args
        get_param = lambda x : kwargs.get(x)

        title = get_param("title")
        title_width = get_param("title_width")
        title_name = get_param("title_name")

        input_width = get_param("input_width")
        input_name = get_param("input_name")
        input_align = get_param("input_align")

        # set layout
        self.layout = HorizontalLayout(self, **kwargs)

        kwargs.pop('name', None)
        kwargs.pop('width', None)
        kwargs.pop('align', None)

        # title
        self.title = Label(self, width=title_width, text=title, name=title_name, **kwargs)
        self.layout.addWidget(self.title)

        # input
        self.input_field = LineEdit(self, width=input_width, name=input_name, align=input_align, **kwargs)
        self.layout.addWidget(self.input_field)

    def get_input(self):
        return self.input_field

    def setText(self, text:str):
        self.input_field.setText(text)

    def text(self):
        return self.input_field.text()

    def enable(self):
        self.input_field.enable()

    def disable(self):
        self.input_field.disable()

    def reset(self):
        self.input_field.reset()


class LoginInputFrame(BaseInputFrame):

    def __init__(self, widget, **kwargs):
        super(LoginInputFrame, self).__init__(widget, l_m=30, r_m=30, space=9, height=52,
                                            name="Login_input_box",
                                            title_name="Login_input_title",
                                            input_name="Login_input_input",
                                            **kwargs)

        # set default title width if not given
        get_param = lambda x : kwargs.get(x, 0)
        title_width = get_param("title_width")
        not title_width and self.title.setFixedWidth(160)


class TabsInputFrame(BaseInputFrame):

    def __init__(self, widget, **kwargs):

        # lambda func grab if given
        get_param = lambda x : kwargs.get(x)

        height = get_param("height")
        height = 30 if not height else height
        kwargs.pop('height', None)

        super(TabsInputFrame, self).__init__(widget, height=height, space=18,
                                            name="view_input",
                                            align=(Qt.AlignRight | Qt.AlignVCenter),
                                            **kwargs)

        fix_width = get_param("fix_width")
        width = get_param("width")

        if fix_width is True:
            width = 285 if not width else width
            self.setFixedWidth(width)


    def enable(self):
        self.setObjectName("view_input")
        super().enable()

    def disable(self):
        self.setObjectName("view_input_disable")
        super().disable()

    def reset(self):
        self.setObjectName("view_input")
        super().reset()


class SearchInputFrame(BaseInputFrame):

    def __init__(self, widget, **kwargs):

        # lambda func grab if given
        get_param = lambda x : kwargs.get(x)

        height = get_param("height")
        height = 30 if not height else height

        super(SearchInputFrame, self).__init__(widget, height=height,
                                                name="view_search",
                                                **kwargs)

        # set default title width if not given
        input_width = get_param("input_width")
        not input_width and self.input_field.setFixedWidth(210)

    def reset(self):
        self.setObjectName("view_search")
        super().reset()

class PriceBox(GroupBox):

    layout : HorizontalLayout = None
    button : RadioButton = None
    label  : Label = None
    input_field : TabsInputFrame = None

    def __init__(self, widget:QWidget, *args, **kwargs):

        # lambda func grab if given
        get_param = lambda x : kwargs.get(x)

        super(PriceBox, self).__init__(widget, *args,
                                       name="price_box",
                                       align=(Qt.AlignRight | Qt.AlignVCenter))

        # get param
        label = get_param("label")
        height = get_param("height")

        height = 38 if not height else height
        kwargs.pop('height', None)

        self.layout = HorizontalLayout(self)

        self.button = Button(self, name="check_button")
        self.layout.addWidget(self.button)

        self.input_field = TabsInputFrame(self, height=height, input_align=Qt.AlignRight, **kwargs)
        self.layout.addWidget(self.input_field)

        self.label = Label(self, text=label, height=height, **kwargs)
        self.layout.addWidget(self.label)

    def check(self):
        self.setChecked(True)
        self.button.setText("•")

    def uncheck(self):
        self.setChecked(False)
        self.button.setText("")

    def disable(self):
        self.setObjectName("price_box_disable")
        self.setChecked(False)

        self.button.setText("")
        self.button.disable()

        self.input_field.disable()
        self.input_field.setText("-")

    def setText(self, price:int):
        self.input_field.setText(str(price))

class ViewButton(Button):

    def __init__(self, widget:QWidget, **kwargs):
        super(ViewButton, self).__init__(widget, name="view_button", **kwargs)

    def enable(self):
        self.setObjectName("view_button")
        super().enable()

    def disable(self):
        self.setObjectName("view_button_disable")
        super().disable()
