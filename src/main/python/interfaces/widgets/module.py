from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QComboBox, QCheckBox

from .button import Button, RadioButton
from .frame import Frame
from .groupbox import GroupBox
from .label import Label
from .layout import HorizontalLayout, VerticalLayout
from .lineedit import LineEdit
from .spacer import HorizontalSpacer

from ..helper import get_children


class BaseTwoLabelFrame(Frame):

    label_one: Label = None
    label_two: Label = None

    def __init__(
        self,
        widget: QWidget,
        label_one_name: str = "",
        label_two_name: str = "",
        label_one_text: str = "",
        label_two_text: str = "",
        **kwargs,
    ):
        """
        A frame object contains two label child widget.
        Base class object, don't use directly on the implementation.
        :param widget: required. the parent widget for this frame.
        :param label_one_name: optional. given name to control style for label one
        :param label_two_name: optional. given name to control style for label two
        :param label_one_text: optional. the text on label one.
        :param label_two_text: optional. the text on label two.
        :param align: optional. label align. Reference can be found: https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/core/Qt.AlignmentFlag.html#field_detail
        """
        super(BaseTwoLabelFrame, self).__init__(widget, **kwargs)

        kwargs.pop("name", None)

        layout = HorizontalLayout(self)

        self.label_one = Label(self, name=label_one_name, **kwargs)
        self.set_label_one_text(label_one_text)
        layout.addWidget(self.label_one)

        spacer = HorizontalSpacer()
        layout.addItem(spacer)

        self.label_two = Label(self, name=label_two_name, **kwargs)
        self.set_label_two_text(label_two_text)
        layout.addWidget(self.label_two)

    def set_label_one_text(self, text: str):
        """
        Set the given text to label one.
        :return: this function doesn't return value
        """
        self.label_one.setText(text)

    def set_label_two_text(self, text: str):
        """
        Set the given text to label two.
        :return: this function doesn't return value
        """
        self.label_two.setText(text)

    def get_label_one(self):
        """
        :return: the label one object, not the text within it.
        """
        return self.label_one

    def get_label_two(self):
        """
        :return: the label two object, not the text within it.
        """
        return self.label_two


class SectionTitleFrame(BaseTwoLabelFrame):
    def __init__(
        self, 
        widget: QWidget, 
        label_one_text: str ="",
        label_two_text: str ="",
        ):
        """
        Title frame for section.
        label one used for title, label two used for hint.
        :param widget: required. the parent widget for this frame
        :param label_one_text: optional. the text on label one.
        :param label_two_text: optional. the text on label two.
        """
        super(SectionTitleFrame, self).__init__(
            widget,
            name="section_title_frame",
            label_one_name="section_title",
            label_two_name="section_hint",
            label_one_text=label_one_text,
            label_two_text=label_two_text,
            align=Qt.AlignVCenter,
        )


class ConfigFrame(BaseTwoLabelFrame):
    def __init__(self, widget: QWidget, **kwargs):
        """
        
        """
        super(ConfigFrame, self).__init__(
            widget, name="config_frame", align=Qt.AlignVCenter, **kwargs
        )

    def setTitle(self, text: str):
        super().set_label_one_text(text)

    def title(self):
        return self.label_one.text()

    def setText(self, text: str):
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


class ParamFrame(Frame):

    dat: Label = None

    def __init__(self, widget: QWidget, dat: str = 0, label: str = "", **kwargs):
        """
        Dashboard data widget, contain two labels
        dat is the data (i.e. "1")
        label is the param label (i.e. "running")
        :param widget: required. the parent widget for this widget
        :param dat: data content for this widget
        :param label: label for this data
        """
        super(ParamFrame, self).__init__(widget)

        layout = VerticalLayout(self, space=2)

        self.dat = Label(self, name="dashboard_param_dat", text=dat, align=Qt.AlignLeft)
        layout.addWidget(self.dat)

        label = Label(
            self, name="dashboard_param_label", text=label, align=Qt.AlignLeft
        )
        layout.addWidget(label)

    def set_dat(self, text: str):
        self.dat.setText(text)

    def get_dat(self):
        return self.dat.text()


class EstimateFrame(Frame):

    in_out: str = ""
    unit: str = "Credits"
    credit: Label = None

    def __init__(
        self, widget: QWidget, title: str = "", in_out: str = "", credit: str = ""
    ):
        """
        Dashboard estimate widget.
        :param widget: required. the parent widget for this widget
        :param title: widget label (i.e. "estimate profit:")
        :param in_out: "+" or "-"
        :param credit: credit need to be present (i.e. "15")
        """
        super(EstimateFrame, self).__init__(widget)

        layout = HorizontalLayout(self, space=30)

        left = Frame(self)
        left_layout = VerticalLayout(left)
        layout.addWidget(left)

        title = Label(
            self, name="dashboard_estimate_title", text=title, align=Qt.AlignLeft
        )
        left_layout.addWidget(title)

        subtitle = Label(
            self,
            name="dashboard_estimate_subtitle",
            text="(within next 24 hrs)",
            align=Qt.AlignLeft,
        )
        left_layout.addWidget(subtitle)

        self.in_out = in_out
        credit = Label(
            self,
            name="dashboard_estimate_credit",
            text=f"{self.in_out} {credit} {self.unit}",
            align=(Qt.AlignRight | Qt.AlignVCenter),
        )
        layout.addWidget(credit)

    def set_credit(self, text: str):
        self.credit.setText(f"{self.in_out} {text} {self.unit}")

    def get_credit(self, text: str):
        self.credit.text()


class BaseInputFrame(Frame):

    title: Label = None
    input_field: LineEdit = None
    layout: HorizontalLayout = None

    def __init__(
        self,
        widget: QWidget,
        title: str = "",
        title_width: int = 0,
        title_name: str = "",
        title_align: Qt = None,
        input_width: int = 0,
        input_name: str = "",
        input_align: Qt = None,
        **kwargs,
    ):

        super(BaseInputFrame, self).__init__(widget, **kwargs)

        # set layout
        self.layout = HorizontalLayout(self, **kwargs)

        kwargs.pop("name", None)
        kwargs.pop("width", None)
        kwargs.pop("align", None)
        kwargs.pop("space", None)

        # title
        self.title = Label(
            self,
            width=title_width,
            text=title,
            name=title_name,
            align=title_align,
            **kwargs,
        )
        self.layout.addWidget(self.title)

        # input
        self.input_field = LineEdit(
            self, width=input_width, name=input_name, align=input_align, **kwargs
        )
        self.layout.addWidget(self.input_field)

    def get_input(self):
        return self.input_field

    def setText(self, text: str):
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
    def __init__(self, widget: QWidget, title_width: int = 150, **kwargs):
        super(LoginInputFrame, self).__init__(
            widget,
            l_m=30,
            r_m=30,
            space=9,
            height=52,
            name="login_input",
            title_width=title_width,
            **kwargs,
        )


class ViewInputFrame(BaseInputFrame):
    """
        This widget can be used on all of the subpage,
        i.e. Job tab, Resources tab etc.
    """

    def __init__(
        self,
        widget: QWidget,
        height: int = 30,
        width: int = 285,
        fix_width: bool = False,
        space: int = 18,
        **kwargs,
    ):
        super(ViewInputFrame, self).__init__(
            widget, height=height, space=space, name="view_input", **kwargs
        )

        if fix_width is True:
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
    def __init__(
        self, widget: QWidget, height: int = 30, input_width: int = 210, **kwargs
    ):
        super(SearchInputFrame, self).__init__(
            widget, height=height, input_width=input_width, name="view_search", **kwargs
        )

    def reset(self):
        self.setObjectName("view_search")
        super().reset()


class AttendanceBox(Frame):
    layout: HorizontalLayout = None
    button: Button = None
    frame: Frame = None
    flag: bool = False

    def __init__(self, widget: QWidget, *args, height: int = 38, **kwargs):

        # lambda func grab if given

        super(AttendanceBox, self).__init__(
            widget,
            *args,
            name="attendance_box",
            align=(Qt.AlignRight | Qt.AlignVCenter),
        )

        self.flag = False

        self.layout = HorizontalLayout(self)

        self.button = Button(self, cursor=True)
        self.layout.addWidget(self.button)

        self.frame = Frame(self)
        self.layout.addWidget(self.frame)

    def check(self):
        self.setObjectName("attendance_box")
        self.button.setText("•")
        self.flag = True

        # set combo box enabled
        children = get_children(self.frame, QComboBox)
        for child in children:
            child.setEnabled(True)

        # set check box enabled
        children = get_children(self.frame, QCheckBox)
        for child in children:
            child.setEnabled(True)

    def uncheck(self):
        self.setObjectName("attendance_box_uncheck")
        self.button.setText("")
        self.flag = False

        # set combo box disabled
        children = get_children(self.frame, QComboBox)
        for child in children:
            child.setEnabled(False)

        # set check box disabled
        children = get_children(self.frame, QCheckBox)
        for child in children:
            child.setEnabled(False)

    def disable(self):
        self.setObjectName("attendance_box_disable")

        # set combo box disabled
        children = get_children(self.frame, QComboBox)
        for child in children:
            child.setEnabled(False)

        # set check box disabled
        children = get_children(self.frame, QCheckBox)
        for child in children:
            child.setEnabled(False)

        self.button.setText("")
        self.button.disable()


class PriceBox(GroupBox):

    layout: HorizontalLayout = None
    button: Button = None
    label: Label = None
    input_field: ViewInputFrame = None

    def __init__(
        self, widget: QWidget, *args, label: str = "", height: int = 38, **kwargs
    ):

        # lambda func grab if given

        super(PriceBox, self).__init__(
            widget, *args, name="price_box", align=(Qt.AlignRight | Qt.AlignVCenter)
        )

        self.layout = HorizontalLayout(self)

        self.button = Button(self, name="check_button")
        self.layout.addWidget(self.button)

        self.input_field = ViewInputFrame(
            self, height=height, input_align=Qt.AlignRight, **kwargs
        )
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

    def setText(self, price: int):
        self.input_field.setText(str(price))


class Scheme(Frame):
    def __init__(
        self,
        widget: QWidget,
        label: str,
        event_func,
        name: str = "",
        label_name: str = "",
        **kwargs,
    ):
        """
        create a single scheme
        :param widget: parent widget
        :param label: time slot
        :param event_func: trigger function for the mousePress event
        :param name: optional, given the name for styling
        :param label_name: optional, given the label name
        """

        super(Scheme, self).__init__(widget, name=name, **kwargs)

        layout = VerticalLayout(self, space=16)

        self.time = label
        self.cpu_price = 0
        self.gpu_price = 0
        self.memory_price = 0
        self.disk_space_price = 0
        self.unit = "Credit/Hr"

        label = Label(self, text=self.time, name=label_name, align=Qt.AlignHCenter)
        layout.addWidget(label)

        self.cpu = Label(
            self,
            text=f"{self.cpu_price} {self.unit}",
            name=label_name,
            align=Qt.AlignHCenter,
        )
        layout.addWidget(self.cpu)

        self.gpu = Label(
            self,
            text=f"{self.gpu_price} {self.unit}",
            name=label_name,
            align=Qt.AlignHCenter,
        )
        layout.addWidget(self.gpu)

        self.memory = Label(
            self,
            text=f"{self.memory_price} {self.unit}",
            name=label_name,
            align=Qt.AlignHCenter,
        )
        layout.addWidget(self.memory)

        self.disk_space = Label(
            self,
            text=f"{self.disk_space_price} {self.unit}",
            name=label_name,
            align=Qt.AlignHCenter,
        )
        layout.addWidget(self.disk_space)

        self.mousePressEvent = event_func

    def update_cpu(self, cpu_price):
        self.cpu_price = cpu_price
        self.cpu.setText(f"{self.cpu_price} {self.unit}")

    def update_gpu(self, gpu_price):
        self.gpu_price = gpu_price
        self.gpu.setText(f"{self.gpu_price} {self.unit}")

    def get_info(self):
        return [
            self.time,
            self.cpu_price,
            self.gpu_price,
            self.memory_price,
            self.disk_space_price,
        ]


class ViewButton(Button):
    def __init__(self, widget: QWidget, **kwargs):
        super(ViewButton, self).__init__(widget, name="view_button", **kwargs)

    def enable(self):
        self.setObjectName("view_button")
        super().enable()

    def disable(self):
        self.setObjectName("view_button_disable")
        super().disable()
