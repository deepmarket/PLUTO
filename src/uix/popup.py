# popup widget

from src.uix.util import *


# base class
class BaseDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(QDialog, self).__init__(*args, **kwargs)

        # gui property
        self.pos = None

    # mouse graping and window moves
    def mousePressEvent(self, event):
        self.pos = event.globalPos()

    # mouse graping and window moves
    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.pos = event.globalPos()


class Question(BaseDialog):

    def __init__(self, question, *args, **kwargs):
        super(Question, self).__init__(*args, **kwargs)

        self.question = question

        self._init_geometry()
        self._init_ui()

        self.setStyleSheet(question_style)

    def _init_geometry(self):
        # hide title bar
        self.setWindowFlags(Qt.FramelessWindowHint)

        # widget optimization
        self.setWindowModality(Qt.ApplicationModal)

        self.setObjectName("Question_window")

        # window size
        set_base_geometry(self, 400, 155, fixed=True)

    def _init_ui(self):

        window_layout = add_layout(self, VERTICAL, t_m=50, b_m=38, l_m=76, r_m=76)

        question = add_label(self, self.question, name="Question_question", align=Qt.AlignHCenter)

        button_frame = QFrame(self)
        button_layout = add_layout(button_frame, HORIZONTAL, space=35)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_layout.addItem(spacer)

        cancel = add_button(self, "CANCEL", name="Question_button_cancel")
        button_layout.addWidget(cancel)

        confirm = add_button(self, "CONFIRM", name="Question_button_confirm")
        button_layout.addWidget(confirm)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_layout.addItem(spacer)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        window_layout.addWidget(question)
        window_layout.addItem(spacer)
        window_layout.addWidget(button_frame)

        confirm.clicked.connect(self.on_confirm_clicked)
        cancel.clicked.connect(self.on_cancel_clicked)

    def on_confirm_clicked(self):
        self.accept()
        self.close()

    def on_cancel_clicked(self):
        self.reject()
        self.close()


class Notification(BaseDialog):

    def __init__(self, *args, **kwargs):
        super(Notification, self).__init__(*args, **kwargs)

        self.window = None
        self.clean = None
        self.download = None
        self.done = None

        self._init_geometry()
        self._init_ui()

        self.setStyleSheet(notification_style)

    def _init_geometry(self):
        # hide title bar
        self.setWindowFlags(Qt.FramelessWindowHint)

        # widget optimization
        self.setWindowModality(Qt.ApplicationModal)

        self.setObjectName("Notification_window")

        # window size
        set_base_geometry(self, 724, 510, fixed=True)

    def _init_ui(self):
        window_layout = add_layout(self, VERTICAL, t_m=32, b_m=32, l_m=40, r_m=40)

        self.window = QFrame(self)
        self.window.setFixedHeight(645)

        button_frame = QFrame(self)
        button_layout = add_layout(button_frame, HORIZONTAL)

        self.clean = add_button(button_frame, "CLEAN")
        self.download = add_button(button_frame, "DOWNLOAD")
        self.done = add_button(button_frame, "DONE")

        button_layout.addWidget(self.clean)
        button_layout.addWidget(self.download)
        button_layout.addWidget(self.done)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        window_layout.addWidget(self.window)
        window_layout.addItem(spacer)
        window_layout.addWidget(button_frame)

        self.done.clicked.connect(self.on_done_clicked)

    def on_done_clicked(self):
        self.accept()
        self.close()


class CreditHistory(BaseDialog):

    def __init__(self, *args, **kwargs):
        super(CreditHistory, self).__init__(*args, **kwargs)

        self._init_geometry()
        self._init_ui()

        self.setStyleSheet(credit_history_style)

    def _init_geometry(self):
        # hide title bar
        self.setWindowFlags(Qt.FramelessWindowHint)

        # widget optimization
        self.setWindowModality(Qt.ApplicationModal)

        self.setObjectName("Credit_window")

        # window size
        set_base_geometry(self, 724, 510, fixed=True)

    def _init_ui(self):
        pass
