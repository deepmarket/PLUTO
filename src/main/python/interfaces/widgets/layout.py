"""

    This module generate a Qt layout wrapper object to arrange child widgets
    within a widget to ensure that they make good use of the available space.

"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLayout, QHBoxLayout, QVBoxLayout, QStackedLayout, QWidget


class Layout(QLayout):
    def __init__(
        self,
        widget: QWidget,
        l_m: int = 0,
        r_m: int = 0,
        t_m: int = 0,
        b_m: int = 0,
        space: int = 0,
        name: str = "",
        align: Qt = None,
        **kwargs
    ):
        super(Layout, self).__init__(widget)

        # Set margin and spacing
        self.setContentsMargins(l_m, t_m, r_m, b_m)
        self.setSpacing(space)

        # Set property if given
        name and self.setObjectName(name)
        align and self.setAlignment(align)


class HorizontalLayout(QHBoxLayout, Layout):
    def __init__(self, widget, **kwargs):
        super(HorizontalLayout, self).__init__(widget, **kwargs)


class VerticalLayout(QVBoxLayout, Layout):
    def __init__(self, widget, **kwargs):
        super(VerticalLayout, self).__init__(widget, **kwargs)


class StackLayout(QStackedLayout, Layout):
    def __init__(self, widget, **kwargs):
        super(StackLayout, self).__init__(widget, **kwargs)