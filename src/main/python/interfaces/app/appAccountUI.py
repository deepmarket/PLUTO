from fbs_runtime.application_context.PyQt5 import ApplicationContext
from ..widgets import Frame

from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor

class AppAccountUI(Frame):            

    def __init__(self, parent, cxt:ApplicationContext, width: int, height: int, *args, **kwargs):
        super(AppAccountUI, self).__init__(parent, name="account")

        self._init_ui(width, height)

        self.setStyleSheet(cxt.app_style)
    
    def _init_ui(self, width: int, height: int):

        self.setFixedSize(width, height)

        # shadow
        effect = QGraphicsDropShadowEffect()
        effect.setBlurRadius(20)
        effect.setXOffset(0)
        effect.setYOffset(0)
        effect.setColor(QColor("#91A4AD"))

        self.setGraphicsEffect(effect)