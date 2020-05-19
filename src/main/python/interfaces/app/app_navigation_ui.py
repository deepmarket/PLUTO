from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtCore import Qt, QSize

from ..widgets import Frame, HorizontalLayout, HorizontalSpacer, Label, Button
from ..config import MENU_ICON_SIZE
from ..helper import menu_icon


class AppNavigationUI(Frame):
    """
    This file initializes the UI for
    Application Navigation.
    """

    credit: Label = None
    credit_prefix: str = "CREDITS: "

    menu_button: Button = None

    def __init__(
        self, parent, cxt: ApplicationContext, width: int, height: int, *args, **kwargs
    ):
        super(AppNavigationUI, self).__init__(parent, name="navigation")

        self._init_ui(width, height)

        self.setStyleSheet(cxt.app_style)

    def set_credit(self, text: str):
        """
        This function sets text for Credit
        :param text:
        :return:
        """
        self.credit.setText(f"{self.credit_prefix}{text}")

    def _init_ui(self, width: int, height: int):
        """
        This function initializes the navigation UI
        Sets the width, height and specified in the input.
        Creates and adds navigation button.
        :param width:
        :param height:
        :return:
        """

        self.setFixedSize(width, height)

        window_layout = HorizontalLayout(self, align=Qt.AlignVCenter, space=16)

        spacer = HorizontalSpacer()
        window_layout.addItem(spacer)

        self.credit = Label(
            self, text=f"{self.credit_prefix}ERROR", name="navigation_credit"
        )
        window_layout.addWidget(self.credit)

        self.menu_button = Button(
            self,
            name="navigation_button",
            cursor=True,
            icon=menu_icon(MENU_ICON_SIZE),
            icon_size=MENU_ICON_SIZE,
        )
        window_layout.addWidget(self.menu_button)

        spacer = HorizontalSpacer(width=18)
        window_layout.addItem(spacer)
