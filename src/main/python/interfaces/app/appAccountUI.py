from fbs_runtime.application_context.PyQt5 import ApplicationContext
from ..widgets import Frame

class AppAccountUI(Frame):            

    def __init__(self, parent, cxt:ApplicationContext, width: int, height: int, *args, **kwargs):
        super(AppAccountUI, self).__init__(parent)

        self.width = width
        self.height = height

        self._init_ui()

        self.setStyleSheet(cxt.app_style)
    
    def _init_ui(self):

        self.setFixedSize(self.width, self.height)