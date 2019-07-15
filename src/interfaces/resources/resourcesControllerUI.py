"""

    This file provides a pure GUI interface for resources.
    This component is controlling interface for resources tab

"""

from PyQt5.QtCore import pyqtSignal

from ..widgets import (Frame, SectionTitleFrame,
                        Button, Label,
                        HorizontalLayout, VerticalLayout,
                        HorizontalSpacer, VerticalSpacer)

from ..stylesheet import resources_controller_style

class ResourcesControllerUI(Frame):

    title_view      :Frame = None
    button_view     :Frame = None
    table_view      :Frame = None

    add             :Button = None
    refresh         :Button = None
    edit            :Button = None
    remove          :Button = None

    global_hint     :Label = None

    def __init__(self, signal:pyqtSignal, *args, **kwargs):
        super(ResourcesControllerUI, self).__init__(*args, name="view", **kwargs)

        self.signal = signal
        self._init_ui()
        self.setStyleSheet(resources_controller_style)


    def on_add_button_clicked(self):
        self.signal.emit()

    def on_edit_button_clicked(self):
        pass

    def on_remove_button_clicked(self):
        pass

    def on_refresh_button_clicked(self):
        pass

    def _init_ui(self):

        window_layout = VerticalLayout(self)

        self.title_view = Frame(self, name="view_title_frame")
        window_layout.addWidget(self.title_view)
        self._init_title_view()

        self.button_view = Frame(self, name="view_buttons_frame")
        window_layout.addWidget(self.button_view)
        self._init_button_view()

        self.table_view = Frame(self, name="view_table_frame")
        window_layout.addWidget(self.table_view)
        self._init_table_view()

    def _init_title_view(self):
        layout = HorizontalLayout(self.title_view)

        title = Label(self.title_view, name="view_title", text="Resource Overview")
        layout.addWidget(title)

        spacer = HorizontalSpacer()
        layout.addItem(spacer)

        self.global_hint = Label(self.title_view, name="section_hint")
        layout.addWidget(self.global_hint)

    def _init_button_view(self):

        layout = HorizontalLayout(self.button_view, space=15)

        self.add = Button(self, text="ADD", name="view_button", cursor=True)
        layout.addWidget(self.add)

        self.refresh = Button(self, text="REFRESH", name="view_button", cursor=True)
        layout.addWidget(self.refresh)

        self.edit = Button(self, text="EDIT", name="view_button", cursor=True)
        layout.addWidget(self.edit)

        self.remove = Button(self, text="REMOVE", name="view_button", cursor=True)
        layout.addWidget(self.remove)

        spacer = HorizontalSpacer()
        layout.addItem(spacer)

        self.add.clicked.connect(self.on_add_button_clicked)

    def _init_table_view(self):

        layout = VerticalLayout(self.table_view)

        spacer = VerticalSpacer()
        layout.addItem(spacer)
