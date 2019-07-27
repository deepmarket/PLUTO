"""

    This file present a set of popup widgets.

"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .button import Button
from .frame import Frame
from .label import Label, Paragraph
from .layout import HorizontalLayout, VerticalLayout
from .spacer import VerticalSpacer, HorizontalSpacer

from ..stylesheet import popup_style


class BaseDialog(QDialog):

    def __init__(
        self,
        *args,
        name: str = "",
        **kwargs
    ):

        super(BaseDialog, self).__init__(*args, **kwargs)

        # set param if given
        name and self.setObjectName(name)

        # widget optimization
        self.setWindowModality(Qt.ApplicationModal)

        # set stylesheet
        self.setStyleSheet(popup_style)


class Question(BaseDialog):

    confirm : Button = None
    cancel  : Button = None

    def __init__(
        self,
        question:str,
        *args,
        **kwargs
    ):
        super(Question, self).__init__(*args, name="question", **kwargs)

        window_layout = VerticalLayout(self, t_m=35, b_m=35, l_m=65, r_m=65, space=20)

        paragraph = question.split("\n")
        question = Paragraph(self, paragraph, space=5, align=Qt.AlignLeft)
        window_layout.addWidget(question)

        button_frame = Frame(self)
        window_layout.addWidget(button_frame)
        button_layout = HorizontalLayout(button_frame)

        self.cancel = Button(button_frame, text="CANCEL", name="cancel")
        button_layout.addWidget(self.cancel)

        spacer = HorizontalSpacer()
        button_layout.addItem(spacer)

        self.confirm = Button(button_frame, text="CONFIRM", name="confirm")
        button_layout.addWidget(self.confirm)

        self.confirm.clicked.connect(self.on_confirm_clicked)
        self.cancel.clicked.connect(self.on_cancel_clicked)

    def on_confirm_clicked(self):
        self.accept()
        self.close()

    def on_cancel_clicked(self):
        self.reject()
        self.close()

    def get_confirm(self):
        return self.confirm

    def get_cancel(self):
        return self.cancel
