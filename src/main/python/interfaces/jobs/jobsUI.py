
"""

    This file provides a pure GUI interface for resources.
    This component is overall UI manager for resources tab.

"""
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLayout, QSpacerItem, QSizePolicy

from ..widgets import StackLayout, Frame, VerticalLayout, HorizontalLayout, Label, HorizontalSpacer, Button, VerticalSpacer


class JobsUI(Frame):

    _stack = None
    button_frame : Frame = None
    content_frame : Frame = None

    add_view_button = None
    controller_button = None

    def __init__(self, cxt:ApplicationContext, *args, **kwargs):
        super(JobsUI, self).__init__(*args, name="views", **kwargs)

        self.cxt = cxt

        self._init_ui()
        self._stack.setCurrentIndex(0)
        self.setStyleSheet(self.cxt.jobs_style)


    def _init_ui(self):
        # create layout for interface
        window_layout = VerticalLayout(self)

        # create buttom frame
        self.button_frame = Frame(self, name="views_buttons_frame")
        window_layout.addWidget(self.button_frame)
        self._init_button_frame()

        # create content frame
        self.content_frame = Frame(self)
        window_layout.addWidget(self.content_frame)
        self._stack = StackLayout(self.content_frame)

        # connect clicked
        self.add_view_button.clicked.connect(self.on_add_view_button_clicked)
        self.controller_button.clicked.connect(self.on_controller_button_clicked)

    def _init_button_frame(self):

        layout = HorizontalLayout(self.button_frame, space=24)

        self.add_view_button = Button(self.button_frame, text="Add Jobs", name="views_button_active", cursor=True)
        layout.addWidget(self.add_view_button)

        self.controller_button = Button(self.button_frame, text="Job Lists", name="views_button", cursor=True)
        layout.addWidget(self.controller_button)

        spacer = HorizontalSpacer()
        layout.addItem(spacer)

    # set functions, given widget, set to the corresponding index
    def set_add_view(self, widget):
        self._stack.insertWidget(0, widget)

    def set_controller(self, widget):
        self._stack.insertWidget(1, widget)

    # display the widget in the corresponding index, raise error if happened
    def on_add_view_button_clicked(self):
        # set button to enable stylesheet
        self.add_view_button.setObjectName("views_button_active")
        self.controller_button.setObjectName("views_button")
        self.setStyleSheet(self.cxt.jobs_style)
        
        self._stack.setCurrentIndex(0)

    def on_controller_button_clicked(self):
        # set button to enable stylesheet
        self.add_view_button.setObjectName("views_button")
        self.controller_button.setObjectName("views_button_active")
        self.setStyleSheet(self.cxt.jobs_style)
        self._stack.setCurrentIndex(1)
