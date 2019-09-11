from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLayout, QSpacerItem, QSizePolicy

from ..widgets import StackLayout, Frame, VerticalLayout, HorizontalLayout, Label, HorizontalSpacer, Button, VerticalSpacer

class LoginUI(Frame):

    _to_login_signal = pyqtSignal()

    login_frame: Frame = None
    create_frame: Frame = None

    def __init__(self, login_signal:pyqtSignal, cxt:ApplicationContext, *args, **kwargs):
        super(LoginUI, self).__init__(*args, **kwargs)

        self.login_signal = login_signal

        self.cxt = cxt
