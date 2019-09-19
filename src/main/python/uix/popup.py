# popup widget

from uix.util import *
from fbs_runtime.application_context.PyQt5 import ApplicationContext


# base class
class BaseDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(QDialog, self).__init__(*args, **kwargs)

        self._init_geometry()

    def _init_geometry(self):
        # widget optimization
        self.setWindowModality(Qt.ApplicationModal)

        self.setObjectName("Question_window")

    #     # gui property
    #     self.pos = None
    #
    # # mouse graping and window moves
    # def mousePressEvent(self, event):
    #     self.pos = event.globalPos()
    #
    # # mouse graping and window moves
    # def mouseMoveEvent(self, event):
    #     delta = QPoint(event.globalPos() - self.pos)
    #     self.move(self.x() + delta.x(), self.y() + delta.y())
    #     self.pos = event.globalPos()


class Question(BaseDialog):

    def __init__(self, question, cxt:ApplicationContext, *args, **kwargs):
        super(Question, self).__init__(*args, **kwargs)

        self.question = question

        self._init_geometry()
        self._init_ui()

        self.setStyleSheet(cxt.question_style)

    def _init_geometry(self):
        # hide title bar
        # self.setWindowFlags(Qt.FramelessWindowHint)

        # window size
        # set_base_geometry(self, 400, 155, fixed=True)
        pass

    def _init_ui(self):

        window_layout = add_layout(self, VERTICAL, t_m=35, b_m=35, l_m=65, r_m=65, space=20)

        question = add_label(self, self.question, name="Question_question")
        window_layout.addWidget(question)

        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        window_layout.addItem(spacer)

        button_frame, button_layout = add_frame(self, layout=HORIZONTAL)
        window_layout.addWidget(button_frame)

        cancel = add_button(self, "CANCEL", name="Question_button_cancel")
        button_layout.addWidget(cancel)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_layout.addItem(spacer)

        confirm = add_button(self, "CONFIRM", name="Question_button_confirm")
        button_layout.addWidget(confirm)

        confirm.clicked.connect(self.on_confirm_clicked)
        cancel.clicked.connect(self.on_cancel_clicked)

    def on_confirm_clicked(self):
        self.accept()
        self.close()

    def on_cancel_clicked(self):
        self.reject()
        self.close()


class Notification(BaseDialog):

    def __init__(self, cxt:ApplicationContext, *args, **kwargs):
        super(Notification, self).__init__(*args, **kwargs)

        self.clean = None
        self.done = None
        self.window = None

        self._init_geometry()
        self._init_ui()

        self.setStyleSheet(cxt.notification_style)

    def _init_geometry(self):
        # hide title bar
        # self.setWindowFlags(Qt.FramelessWindowHint)

        # widget optimization
        self.setWindowModality(Qt.ApplicationModal)

        self.setObjectName("Notification")

        # window size
        set_base_geometry(self, 724, 510, fixed=True)

    def _init_ui(self):
        section_layout = add_layout(self, VERTICAL)

        title_frame = QFrame(self)
        title_frame.setObjectName("Notification_title_frame")
        title_frame.setFixedHeight(100)
        title_layout = add_layout(title_frame, HORIZONTAL, l_m=40, r_m=40)

        title = add_label(title_frame, "Notification", name="Notification_title", align=Qt.AlignVCenter)

        self.clean = add_button(title_frame, "CLEAN", name="Notification_button")
        self.done = add_button(title_frame, "DONE", name="Notification_button")

        spacer_01 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        spacer_02 = QSpacerItem(1, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        title_layout.addWidget(title)
        title_layout.addItem(spacer_01)
        title_layout.addWidget(self.clean)
        title_layout.addItem(spacer_02)
        title_layout.addWidget(self.done)

        window_frame = QFrame(self)
        window_layout = add_layout(window_frame, VERTICAL, l_m=5, t_m=5, r_m=5, b_m=5)

        self.window = QFrame(self)
        self.window.setObjectName("Notification_window")

        window_layout.addWidget(self.window)

        section_layout.addWidget(title_frame)
        section_layout.addWidget(window_frame)

        self.done.clicked.connect(self.on_done_clicked)

    def on_done_clicked(self):
        self.accept()
        self.close()


class CreditHistory(BaseDialog):

    def __init__(self, cxt:ApplicationContext, *args, **kwargs):
        super(CreditHistory, self).__init__(*args, **kwargs)

        self.done = None
        self.cost = None
        self.profit = None

        self._init_geometry()
        self._init_ui()

        self.setStyleSheet(cxt.credit_history_style)

    def _init_geometry(self):
        # hide title bar
        # self.setWindowFlags(Qt.FramelessWindowHint)

        # widget optimization
        self.setWindowModality(Qt.ApplicationModal)

        self.setObjectName("Credit")

        # window size
        set_base_geometry(self, 724, 510, fixed=True)

    def _init_ui(self):
        section_layout = add_layout(self, VERTICAL)

        title_frame = QFrame(self)
        title_frame.setObjectName("Credit_title_frame")
        title_frame.setFixedHeight(100)
        title_layout = add_layout(title_frame, HORIZONTAL, l_m=40, r_m=40)

        title = add_label(title_frame, "Recent 30 Days Transit Record", name="Credit_title", align=Qt.AlignVCenter)
        self.done = add_button(title_frame, "DONE", name="Credit_button")

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        title_layout.addWidget(title)
        title_layout.addItem(spacer)
        title_layout.addWidget(self.done)

        window_frame = QFrame(self)
        window_layout = add_layout(window_frame, VERTICAL, l_m=5, t_m=5, r_m=5, b_m=5)

        button_frame = QFrame(window_frame)
        button_frame.setFixedHeight(33)
        button_layout = add_layout(button_frame, HORIZONTAL, space=20)

        self.cost = add_button(button_frame, "COST")
        self.cost.setObjectName("Credit_section_button_active")

        self.profit = add_button(button_frame, "PROFIT")
        self.profit.setObjectName("Credit_section_button")

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        button_layout.addWidget(self.cost)
        button_layout.addWidget(self.profit)
        button_layout.addItem(spacer)

        self.window = QFrame(self)
        self.window.setObjectName("Credit_window")

        window_layout.addWidget(button_frame)
        window_layout.addWidget(self.window)

        section_layout.addWidget(title_frame)
        section_layout.addWidget(window_frame)

        self.done.clicked.connect(self.on_done_clicked)

    def on_done_clicked(self):
        self.accept()
        self.close()
