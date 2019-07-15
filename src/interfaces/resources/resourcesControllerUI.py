"""

    This file provides a pure GUI interface for resources.
    This component is controlling interface for resources tab

"""

from collections import OrderedDict

from PyQt5.QtCore import pyqtSignal

from ..widgets import (Frame, SectionTitleFrame,
                        Button, Label, Table,
                        HorizontalLayout, VerticalLayout,
                        HorizontalSpacer, VerticalSpacer)

from ..stylesheet import resources_controller_style
from ..stylesheet.config import RESOURCES_MAX_ROW

class ResourcesControllerUI(Frame):

    title_view      :Frame = None
    button_view     :Frame = None
    table_view      :Frame = None

    add             :Button = None
    refresh         :Button = None
    edit            :Button = None
    remove          :Button = None

    table           :Table = None

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

        header = OrderedDict()

        header["Machine Name"] = 150
        header["IP Address"] = 180
        header["GPUs"] = 100
        header["Cores"] = 100
        header["Ram (GB)"] = 100
        header["Price"] = 120
        header["Status"] = 150

        self.table = Table(self.table_view, RESOURCES_MAX_ROW, header, name="table")
        layout.addWidget(self.table)

        # TODO: test code, remove it later on
        # for i in range(14):
            # self.table.add(["mac", "127.0.0.1", "1", "1", "1", "$15/hr", "ACTIVE"])
