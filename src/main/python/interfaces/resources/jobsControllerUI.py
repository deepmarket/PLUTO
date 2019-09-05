from fbs_runtime.application_context.PyQt5 import ApplicationContext

from ..widgets import StackLayout, Frame, VerticalLayout, Label

class JobsControllerUI(Frame):
    def __init__(self, cxt:ApplicationContext, *args, **kwargs):
        super(JobsControllerUI, self).__init__(*args, name="view", **kwargs)

        self.cxt = cxt

        self._init_ui()
        self.setStyleSheet("background-color: blue;")

    def _init_ui(self):
        layout = VerticalLayout(self)
        
        label = Label(self, text="Job Controller")
        layout.addWidget(label)