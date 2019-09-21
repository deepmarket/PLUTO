from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.Qt import Qt, QSize

from ..widgets import Frame, HorizontalLayout, HorizontalSpacer, Label, Button
from ..helper import menu_icon

from ..config import MENU_ICON_SIZE

class AppNavigationUI(Frame):

    credit: Label = None
    credit_prefix: str = "CREDITS: "

    menu_button: Button = None

    def __init__(self, parent, cxt:ApplicationContext, width: int, height: int, *args, **kwargs):
        super(AppNavigationUI, self).__init__(parent, name="navigation")

        self._init_ui(width, height)

        self.setStyleSheet(cxt.app_style)
    
    def set_credit(self, text: str):
        self.credit.setText(f"{self.credit_prefix}{text}")

    def _init_ui(self, width: int, height: int):

        self.setFixedSize(width, height)

        window_layout = HorizontalLayout(self, align=Qt.AlignVCenter, space=16)

        spacer = HorizontalSpacer()
        window_layout.addItem(spacer)

        self.credit = Label(self, text=f"{self.credit_prefix}ERROR", name="navigation_credit")
        window_layout.addWidget(self.credit)

        self.menu_button = Button(
            self, name="navigation_button", cursor=True, icon=menu_icon(MENU_ICON_SIZE), icon_size=MENU_ICON_SIZE
        )
        window_layout.addWidget(self.menu_button)

        spacer = HorizontalSpacer(width=18)
        window_layout.addItem(spacer)
