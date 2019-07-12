"""

    This module generate serveral combination frame based object.

"""

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt

from .frame import Frame
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


class BaseInputFrame(Frame):

    title       : Label = None
    input_field : QLineEdit = None

    def __init__(self, widget, **kwargs):

        super(BaseInputFrame, self).__init__(widget, **kwargs)

        kwargs.pop('name', None)
        kwargs.pop('width', None)

        # Lambda func grab input args
        get_num = lambda x : kwargs.get(x, 0)
        get_param = lambda x : kwargs.get(x)

        title = get_param("title")
        title_width = get_num("title_width")
        title_name = get_param("title_name")

        input_width = get_num("input_width")
        input_name = get_param("input_name")

        # set layout
        layout = HorizontalLayout(self, **kwargs)

        # title
        self.title = Label(self, width=title_width, text=title, name=title_name, **kwargs)
        layout.addWidget(self.title)

        # input
        self.input_field = LineEdit(self, width=input_width, name=input_name, **kwargs)
        layout.addWidget(self.input_field)

    def get_input(self):
        return self.input_field


class LoginInputFrame(BaseInputFrame):

    def __init__(self, widget, **kwargs):
        super(LoginInputFrame, self).__init__(widget, l_m=30, r_m=30, space=9, height=52,
                                            name="Login_input_box",
                                            title_name="Login_input_title",
                                            input_name="Login_input_input",
                                            **kwargs)

        # set default title width if not given
        get_num = lambda x : kwargs.get(x, 0)
        title_width = get_num("title_width")
        not title_width and self.title.setFixedWidth(160)


class TabsInputFrame(BaseInputFrame):

    def __init__(self, widget, **kwargs):
        super(TabsInputFrame, self).__init__(widget, height=30, space=18,
                                            name="view_input",
                                            align=(Qt.AlignRight | Qt.AlignVCenter),
                                            **kwargs)

        # set default frame width if given
        get_num = lambda x : kwargs.get(x, 0)
        get_param = lambda x : kwargs.get(x)

        fix_width = get_param("fix_width")
        width = get_num("width")

        if fix_width is True:
            if not width:
                self.setFixedWidth(285)
            else:
                self.setFixedWidth(width)
