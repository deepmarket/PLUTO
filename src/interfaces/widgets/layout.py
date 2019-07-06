"""

    This module generate a Qt layout wrapper object to arrange child widgets
    within a widget to ensure that they make good use of the available space.

"""

from PyQt5 import QtWidgets


class Layout(QtWidgets.QLayout):

    def __init__(self, widget, **kwargs):
        super(Layout, self).__init__(widget)
        
        if kwargs:
            # Lambda func grab input args
            get_num = lambda x : kwargs.get(x, 0)
            get_param = lambda x : kwargs.get(x)

            l_m = get_num("l_m")
            t_m = get_num("t_m")
            r_m = get_num("r_m")
            b_m = get_num("b_m")
            space = get_num("space")

            # Set margin and spacing
            self.setContentsMargins(l_m, t_m, r_m, b_m)
            self.setSpacing(space)

            name = get_param("name")
            align = get_param("align")

            # Set object name if given
            name and self.setObjectName(name)

            # Set child widgets alignment if given
            align and self.setAlignment(align)


class HorizontalLayout(QtWidgets.QHBoxLayout, Layout):
    def __init__(self, widget, **kwargs):
        super(HorizontalLayout, self).__init__(widget, **kwargs)


class VerticalLayout(QtWidgets.QVBoxLayout, Layout):
    def __init__(self, widget, **kwargs):
        super(VerticalLayout, self).__init__(widget, **kwargs)


class StackLayout(QtWidgets.QStackedLayout, Layout):
    def __init__(self, widget, **kwargs):
        super(StackLayout, self).__init__(widget, **kwargs)