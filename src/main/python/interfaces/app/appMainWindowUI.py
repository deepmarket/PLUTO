from fbs_runtime.application_context.PyQt5 import ApplicationContext
from ..widgets import Frame, StackLayout


class AppMainWindowUI(Frame):

    stack = None  # stack layout
    stack_widget = None  # current widget

    def __init__(
        self, parent, cxt: ApplicationContext, width: int, height: int, *args, **kwargs
    ):
        super(AppMainWindowUI, self).__init__(parent, name="main_window")

        # set style sheet
        self.setStyleSheet(cxt.app_style)

        # set main window size
        self.setFixedSize(width, height)

        # initial main window layout
        self.stack = StackLayout(self)
