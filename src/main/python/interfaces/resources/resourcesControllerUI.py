from abc import ABCMeta, abstractmethod
from collections import OrderedDict
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtCore import pyqtSignal

from ..widgets import (
    Frame,
    SectionTitleFrame,
    SearchInputFrame,
    ViewButton,
    Label,
    Table,
    LineEdit,
    HorizontalLayout,
    VerticalLayout,
    HorizontalSpacer,
    VerticalSpacer,
)

from ..config import RESOURCES_MAX_ROW


class ResourcesControllerUI(Frame):
    """
    This component is controlling interface for resources tab
    """

    # metaclass for defining abstract base classes
    __metaclass__ = ABCMeta

    title_view: Frame = None
    button_view: Frame = None
    table_view: Frame = None

    add: ViewButton = None
    refresh: ViewButton = None
    edit: ViewButton = None
    remove: ViewButton = None
    search: SearchInputFrame = None

    table: Table = None

    global_hint: Label = None

    def __init__(self, signal: pyqtSignal, cxt: ApplicationContext, *args, **kwargs):
        super(ResourcesControllerUI, self).__init__(*args, name="view", **kwargs)

        self.cxt = cxt

        self.signal = signal
        self._init_ui()
        self.setStyleSheet(self.cxt.controller_style)

    def on_add_button_clicked(self):
        self.signal.emit()

    @abstractmethod
    def on_refresh_button_clicked(self):
        pass

    @abstractmethod
    def on_edit_button_clicked(self):
        pass

    @abstractmethod
    def on_remove_button_clicked(self):
        pass

    @abstractmethod
    def on_search_edited(self):
        pass

    def reset(self):
        # reset input
        self.search.reset()

        # reset table
        self.table.reset()

        # reset hint
        self.reset_hint()

    def reset_hint(self):
        self.global_hint.reset()

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

        self.add = ViewButton(self.button_view, text="ADD", cursor=True)
        layout.addWidget(self.add)

        self.refresh = ViewButton(self.button_view, text="REFRESH", cursor=True)
        layout.addWidget(self.refresh)

        self.edit = ViewButton(self.button_view, text="EDIT", cursor=True)
        layout.addWidget(self.edit)

        self.remove = ViewButton(self.button_view, text="REMOVE", cursor=True)
        layout.addWidget(self.remove)

        spacer = HorizontalSpacer()
        layout.addItem(spacer)

        self.search = SearchInputFrame(self.button_view, hint="Search a machine...")
        layout.addWidget(self.search)

        self.add.clicked.connect(self.on_add_button_clicked)
        self.refresh.clicked.connect(self.on_refresh_button_clicked)
        self.edit.clicked.connect(self.on_edit_button_clicked)
        self.remove.clicked.connect(self.on_remove_button_clicked)
        self.search.input_field.textChanged.connect(self.on_search_edited)

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
