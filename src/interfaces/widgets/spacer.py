"""

    This module provides blank space in a layout.

"""

from PyQt5.QtWidgets import QSpacerItem, QSizePolicy


class Spacer(QSpacerItem):
    def __init__(
        self,
        horizontal: bool = False,
        vertical: bool = False,
        height: int = 0,
        width: int = 0,
        **kwargs
    ):
        super(Spacer, self).__init__(0, 0)

        horizontal and self.changeSize(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        vertical and self.changeSize(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # changeSize(w, h, hPolicy, vPolicy)
        height and self.changeSize(
            self.sizeHint().width(),
            height,
            self.sizePolicy().horizontalPolicy(),
            QSizePolicy.Fixed,
        )
        width and self.changeSize(
            width,
            self.sizeHint().height(),
            QSizePolicy.Fixed,
            self.sizePolicy().verticalPolicy(),
        )


class HorizontalSpacer(Spacer):
    def __init__(self, **kwargs):
        super(HorizontalSpacer, self).__init__(horizontal=True, **kwargs)


class VerticalSpacer(Spacer):
    def __init__(self, **kwargs):
        super(VerticalSpacer, self).__init__(vertical=True, **kwargs)
