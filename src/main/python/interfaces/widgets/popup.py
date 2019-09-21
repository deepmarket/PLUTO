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

class Notification(BaseDialog):

    def __init__(self, cxt:ApplicationContext, *args, **kwargs):
        super(Notification, self).__init__(cxt, name="notification")

        self.clean = None
        self.done = None
        self.window = None

        self.setFixedSize(724, 510)
        self._init_ui()

    def _init_ui(self):
        section_layout = VerticalLayout(self, t_m=5, b_m=5, l_m=5, r_m=5, space=5)

        # title frame
        title_frame = Frame(self, name="title_frame")
        title_layout = HorizontalLayout(title_frame, space=1)
        section_layout.addWidget(title_frame)

        title = Label(
            title_frame, text="Notification", align=Qt.AlignVCenter
        )
        title_layout.addWidget(title)

        spacer = HorizontalSpacer()
        title_layout.addItem(spacer)

        self.clean = Button(title_frame, text="CLEAN")
        title_layout.addWidget(self.clean)

        self.done = Button(title_frame, text="DONE")
        title_layout.addWidget(self.done)

        # window frame

        self.window = Frame(self)
        section_layout.addWidget(self.window)

        self.done.clicked.connect(self.on_done_clicked)

    def on_done_clicked(self):
        self.accept()
        self.close()


# class CreditHistory(BaseDialog):

#     def __init__(self, cxt:ApplicationContext, *args, **kwargs):
#         super(CreditHistory, self).__init__(*args, **kwargs)

#         self.done = None
#         self.cost = None
#         self.profit = None

#         self._init_geometry()
#         self._init_ui()

#         self.setStyleSheet(cxt.credit_history_style)

#     def _init_geometry(self):
#         # hide title bar
#         # self.setWindowFlags(Qt.FramelessWindowHint)

#         # widget optimization
#         self.setWindowModality(Qt.ApplicationModal)

#         self.setObjectName("Credit")

#         # window size
#         set_base_geometry(self, 724, 510, fixed=True)

#     def _init_ui(self):
#         section_layout = add_layout(self, VERTICAL)

#         title_frame = QFrame(self)
#         title_frame.setObjectName("Credit_title_frame")
#         title_frame.setFixedHeight(100)
#         title_layout = add_layout(title_frame, HORIZONTAL, l_m=40, r_m=40)

#         title = add_label(title_frame, "Recent 30 Days Transit Record", name="Credit_title", align=Qt.AlignVCenter)
#         self.done = add_button(title_frame, "DONE", name="Credit_button")

#         spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         title_layout.addWidget(title)
#         title_layout.addItem(spacer)
#         title_layout.addWidget(self.done)

#         window_frame = QFrame(self)
#         window_layout = add_layout(window_frame, VERTICAL, l_m=5, t_m=5, r_m=5, b_m=5)

#         button_frame = QFrame(window_frame)
#         button_frame.setFixedHeight(33)
#         button_layout = add_layout(button_frame, HORIZONTAL, space=20)

#         self.cost = add_button(button_frame, "COST")
#         self.cost.setObjectName("Credit_section_button_active")

#         self.profit = add_button(button_frame, "PROFIT")
#         self.profit.setObjectName("Credit_section_button")

#         spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         button_layout.addWidget(self.cost)
#         button_layout.addWidget(self.profit)
#         button_layout.addItem(spacer)

#         self.window = QFrame(self)
#         self.window.setObjectName("Credit_window")

#         window_layout.addWidget(button_frame)
#         window_layout.addWidget(self.window)

#         section_layout.addWidget(title_frame)
#         section_layout.addWidget(window_frame)

#         self.done.clicked.connect(self.on_done_clicked)

#     def on_done_clicked(self):
#         self.accept()
#         self.close()
