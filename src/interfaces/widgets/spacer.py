"""

    This module provides blank space in a layout.

"""

from PyQt5.QtWidgets import QSpacerItem, QSizePolicy


class Spacer(QSpacerItem):

    def __init__(self, **kwargs):
        super(Spacer, self).__init__(0, 0)

        # Lambda func grab input args
        get_num = lambda x : kwargs.get(x, 0)
        get_param = lambda x : kwargs.get(x)

        horizontal = get_param("horizontal")
        vertical = get_param("vertical")

        height = get_num("height")
        width = get_num("width")

        horizontal and self.changeSize(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        vertical and self.changeSize(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # changeSize(w, h, hPolicy, vPolicy)
        height and self.changeSize(self.sizeHint().width(), height, self.sizePolicy().horizontalPolicy(), QSizePolicy.Fixed)
        width and self.changeSize(width, self.sizeHint().height(), QSizePolicy.Fixed, self.sizePolicy().verticalPolicy())


class HorizontalSpacer(Spacer):

    def __init__(self, **kwargs):
        super(HorizontalSpacer, self).__init__(horizontal=True)

        # Lambda func grab input args
        get_num = lambda x : kwargs.get(x, 0)

        width = get_num("width")
        width and self.changeSize(width, self.sizeHint().height(), QSizePolicy.Fixed, self.sizePolicy().verticalPolicy())


class VerticalSpacer(Spacer):

    def __init__(self, **kwargs):
        super(VerticalSpacer, self).__init__(vertical=True)

        # Lambda func grab input args
        get_num = lambda x : kwargs.get(x, 0)

        height = get_num("height")
        height and self.changeSize(self.sizeHint().width(), height, self.sizePolicy().horizontalPolicy(), QSizePolicy.Fixed)
    