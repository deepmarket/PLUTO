from fbs_runtime.application_context.PyQt5 import ApplicationContext

from ..widgets import Frame, Button


class AppMaskUI(Frame):

    clicked_area: Button = None

    def __init__(
        self, parent, cxt: ApplicationContext, width: int, height: int, *args, **kwargs
    ):
        super(AppMaskUI, self).__init__(parent, name="mask")

        # set style sheet
        self.setStyleSheet(cxt.app_style)

        # set main window size
        self.setFixedSize(width, height)

        self.clicked_area = Button(self, name="mask_clicked_area")
        self.clicked_area.setFixedSize(width, height)
        self.clicked_area.move(0, 0)
