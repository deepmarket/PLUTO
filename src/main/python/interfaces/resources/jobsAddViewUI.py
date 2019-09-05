from fbs_runtime.application_context.PyQt5 import ApplicationContext

from ..widgets import StackLayout, Frame, Label, VerticalLayout

class JobsAddViewUI(Frame):
    def __init__(self, cxt:ApplicationContext, *args, **kwargs):
        super(JobsAddViewUI, self).__init__(*args, name="view", **kwargs)

        self.cxt = cxt

        self._init_ui()
        self.setStyleSheet("background-color: red;")

    def _init_ui(self):
        layout = VerticalLayout(self)
        
        label = Label(self, text="Add View")
        layout.addWidget(label)