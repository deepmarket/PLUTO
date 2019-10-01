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
        """
        Wrapper object for QLayout
        :param widget: required. defined the parent widget for this layout
        :param l_m: optional. left margin
        :param r_m: optional. right margin
        :param t_m: optional. top margin
        :param b_m: optional. button margin
        :param space: optional. space bettween widget within this layout
        :param name: optional. object name for this layout
        :param align: optional. align in this layout. Reference can be found: https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/core/Qt.AlignmentFlag.html#field_detail
        """
        super(Layout, self).__init__(widget)

        # Set margin and spacing
        self.setContentsMargins(l_m, t_m, r_m, b_m)
        self.setSpacing(space)

        # Set property if given
        name and self.setObjectName(name)
        align and self.setAlignment(align)


class HorizontalLayout(QHBoxLayout, Layout):
    def __init__(self, widget, **kwargs):
        """
        Wrapper object for QHBoxLayout
        :param widget: required. defined the parent widget for this layout
        :param l_m: optional. left margin
        :param r_m: optional. right margin
        :param t_m: optional. top margin
        :param b_m: optional. button margin
        :param space: optional. space bettween widget within this layout
        :param name: optional. object name for this layout
        :param align: optional. align in this layout. Reference can be found: https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/core/Qt.AlignmentFlag.html#field_detail
        """

        super(HorizontalLayout, self).__init__(widget, **kwargs)


class VerticalLayout(QVBoxLayout, Layout):
    def __init__(self, widget, **kwargs):
        """
        Wrapper object for QVBoxLayout
        :param widget: required. defined the parent widget for this layout
        :param l_m: optional. left margin
        :param r_m: optional. right margin
        :param t_m: optional. top margin
        :param b_m: optional. button margin
        :param space: optional. space bettween widget within this layout
        :param name: optional. object name for this layout
        :param align: optional. align in this layout. Reference can be found: https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/core/Qt.AlignmentFlag.html#field_detail
        """
        super(VerticalLayout, self).__init__(widget, **kwargs)


class StackLayout(QStackedLayout, Layout):
    def __init__(self, widget, **kwargs):
        """
        Wrapper object for QStackedLayout
        :param widget: required. defined the parent widget for this layout
        :param l_m: optional. left margin
        :param r_m: optional. right margin
        :param t_m: optional. top margin
        :param b_m: optional. button margin
        :param space: optional. space bettween widget within this layout
        :param name: optional. object name for this layout
        :param align: optional. align in this layout. Reference can be found: https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/core/Qt.AlignmentFlag.html#field_detail
        """
        super(StackLayout, self).__init__(widget, **kwargs)
