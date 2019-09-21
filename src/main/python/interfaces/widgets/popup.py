from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .button import Button
from .frame import Frame
from .label import Label, Paragraph
from .layout import HorizontalLayout, VerticalLayout
from .spacer import VerticalSpacer, HorizontalSpacer


class BaseDialog(QDialog):
    def __init__(self, cxt: ApplicationContext, name: str = "", *args, **kwargs):
        """
        Wrapper for QDialog object.
        :param cxt: required. stylesheet reference object from the out most layer. 
        Please look at it at main.py. Usage: i.e. self.setStyleSheet(cxt.popup_style)
        :param name: optional. the object name for this dialog
        """

        super(BaseDialog, self).__init__(*args, **kwargs)

        # set param if given
        name and self.setObjectName(name)

        # widget optimization
        self.setWindowModality(Qt.ApplicationModal)

        # set stylesheet
        self.setStyleSheet(cxt.popup_style)


class Question(BaseDialog):

    confirm: Button = None
    cancel: Button = None

    def __init__(self, question: str, cxt: ApplicationContext, *args, **kwargs):
        """
        A dialog contains a question and ask "yes" or "no".
        :param question: required. the question want to ask user.
        If you want to it to be multiple lines, user '\n'
        :param cxt: required. stylesheet reference object from the out most layer. 
        Please look at it at main.py. Usage: i.e. self.setStyleSheet(cxt.popup_style)
        There's some stylesheet need to setup when use this widget.
        QDialog#question
        QDialog#question QLabel
        QDialog#question QPushButton 
        QDialog#question QPushButton#cancel
        QDialog#question QPushButton#confirm
        """
        super(Question, self).__init__(cxt, name="question", *args, **kwargs)

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

        self.confirm.clicked.connect(self._on_confirm_clicked)
        self.cancel.clicked.connect(self._on_cancel_clicked)

    def get_confirm(self):
        """
        :return: confirm button
        """
        return self.confirm

    def get_cancel(self):
        """
        :return: cancel button
        """
        return self.cancel

    def _on_confirm_clicked(self):
        """
        The function trigger when confirm button clicked.
        An accept signal would be sent to the outer field.
        Then the dialog close.
        """
        self.accept()
        self.close()

    def _on_cancel_clicked(self):
        """
        The function trigger when cancel button clicked.
        An reject signal would be sent to the outer field.
        Then the dialog close.
        """
        self.reject()
        self.close()
