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
        """
        Base spacer object, wrapper for QSpacerItem
        :param horizontal: optional. whether spacer expand horizontally
        :param vertical: optional. whether spacer expand vertically
        :param height: optional. overwrite the spacer to expand vertical with fixed height
        :param width: optional. overwrite the spacer to expand horizontal with fixed width
        """
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
        if width != 0:
            self.changeSize(
                width,
                self.sizeHint().height(),
                QSizePolicy.Fixed,
                self.sizePolicy().verticalPolicy(),
            )


class HorizontalSpacer(Spacer):
    def __init__(self, **kwargs):
        """
        Spacer object expand horizontally.
        :param height: optional. overwrite the spacer to expand vertical with fixed height
        :param width: optional. overwrite the spacer to expand horizontal with fixed width
        :param vertical: optional. whether spacer expand horizontally as well
        """
        super(HorizontalSpacer, self).__init__(horizontal=True, **kwargs)


class VerticalSpacer(Spacer):
    def __init__(self, **kwargs):
        """
        Spacer object expand vertically.
        :param height: optional. overwrite the spacer to expand vertical with fixed height
        :param width: optional. overwrite the spacer to expand horizontal with fixed width
        :param horizontal: optional. whether spacer expand vertically as well
        """
        super(VerticalSpacer, self).__init__(vertical=True, **kwargs)
