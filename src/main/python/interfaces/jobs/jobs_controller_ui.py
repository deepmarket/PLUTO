from abc import ABCMeta, abstractmethod
from collections import OrderedDict
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtCore import pyqtSignal

from ..widgets import (
    Frame,
    HorizontalLayout,
    HorizontalSpacer,
    VerticalSpacer,
    SearchInputFrame,
    Table,
    VerticalLayout,
    ViewButton,
    Label,
)
from ..config import JOBS_MAX_ROW

class JobsControllerUI(Frame):
    """
    This component is controlling interface for jobs tab
    """

    # metaclass for defining abstract base classes
    __metaclass__ = ABCMeta

    title_view: Frame = None
    button_view: Frame = None
    table_view: Frame = None

    add: ViewButton = None
    refresh: ViewButton = None

    running_section: Frame = None
    running_jobs_table: Table = None

    finished_section: Frame = None
    finished_jobs_table: Table = None

    global_hint: Label = None

    def __init__(self, signal: pyqtSignal, cxt: ApplicationContext, *args, **kwargs):
        super(JobsControllerUI, self).__init__(*args, name="view", **kwargs)

        self.cxt = cxt

        self.signal = signal
        self._init_ui()
        self.setStyleSheet(self.cxt.controller_style)

        # self.setStyleSheet(self.cxt.jobs_style)

    def on_add_button_clicked(self):
        self.signal.emit()

    @abstractmethod
    def on_refresh_button_clicked(self):
        pass

    def reset(self):
        # reset table
        self.running_jobs_table.reset()
        self.finished_jobs_table.reset()

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

        title = Label(self.title_view, name="view_title", text="Jobs Overview")
        layout.addWidget(title)

        spacer = HorizontalSpacer()
        layout.addItem(spacer)

        self.global_hint = Label(self.title_view, name="section_hint")
        layout.addWidget(self.global_hint)

    def _init_button_view(self):

        layout = HorizontalLayout(self.button_view, space=15)

        self.add = ViewButton(self.button_view, text="Add New Job", cursor=True)
        layout.addWidget(self.add)

        self.refresh = ViewButton(self.button_view, text="Refresh", cursor=True)
        layout.addWidget(self.refresh)

        spacer = HorizontalSpacer()
        layout.addItem(spacer)

        self.add.clicked.connect(self.on_add_button_clicked)
        self.refresh.clicked.connect(self.on_refresh_button_clicked)

    def _init_table_view(self):

        table_layout = HorizontalLayout(self.table_view, space=1)

        self.running_section = Frame(self.table_view)
        table_layout.addWidget(self.running_section)
        self._init_running_section()

        self.finished_section = Frame(self.table_view)
        table_layout.addWidget(self.finished_section)
        self._init_finished_section()

    def _init_running_section(self):

        layout = VerticalLayout(self.running_section)

        # --------- running jobs table ------------

        header = OrderedDict()
        header[""] = 0

        self.running_jobs_table = Table(
            self.running_section, 
            JOBS_MAX_ROW, 
            header, 
            header_visible=False, 
            row_height=90,
            name="table",
        )
        
        layout.addWidget(self.running_jobs_table)

    def _init_finished_section(self):

        layout = VerticalLayout(self.finished_section)

        # --------- finished jobs table ------------

        header = OrderedDict()
        header[""] = 0

        self.finished_jobs_table = Table(
            self.running_section, 
            JOBS_MAX_ROW, 
            header,
            header_visible=False, 
            row_height=90,
            name="table",
        )
        
        layout.addWidget(self.finished_jobs_table)
        

# class JobsControllerUI(Frame):

#     # metaclass for defining abstract base classes
#     __metaclass__ = ABCMeta

#     search_section: Frame = None
#     table_section: Frame = None

#     # variable
#     table: Table = None
#     search_bar: SearchInputFrame = None
#     refresh_button: ViewButton = None
#     remove_button: ViewButton = None

#     def __init__(self, signal: pyqtSignal, cxt: ApplicationContext, *args, **kwargs):
#         super(JobsControllerUI, self).__init__(*args, **kwargs)

#         self.cxt = cxt
#         self.signal = signal
#         self._init_ui()
#         self.setStyleSheet(self.cxt.jobs_style)

#     def reset(self):
#         # reset input
#         self.search_bar.reset()

#         # reset table
#         self.table.reset()

#     @abstractmethod
#     def on_search_edited(self):
#         pass

#     @abstractmethod
#     def on_refresh_button_clicked(self):
#         pass

#     @abstractmethod
#     def on_remove_button_clicked(self):
#         pass

#     def _init_ui(self):

#         layout = VerticalLayout(self)

#         # --------- table_workspace ------------

#         self.search_section = Frame(self, name="controller")
#         layout.addWidget(self.search_section)
#         self._init_search_section()

#         # --------- table_frame ----------------

#         self.table_section = Frame(self, name="table")
#         layout.addWidget(self.table_section)
#         self._init_table_section()

#     def _init_search_section(self):

#         section_layout = HorizontalLayout(self.search_section)

#         content_frame = Frame(self.search_section)
#         section_layout.addWidget(content_frame)

#         content_layout = HorizontalLayout(content_frame, space=32)

#         line_frame = Frame(content_frame)
#         line_layout = HorizontalLayout(line_frame)
#         content_layout.addWidget(line_frame)

#         self.search_bar = SearchInputFrame(
#             line_frame,
#             hint="Search a job... (Haven't implemented yet)",
#             input_width=600,
#         )
#         line_layout.addWidget(self.search_bar)

#         spacer = HorizontalSpacer()
#         line_layout.addItem(spacer)

#         self.refresh_button = ViewButton(line_frame, text="REFRESH", cursor=True)
#         line_layout.addWidget(self.refresh_button)

#         spacer = HorizontalSpacer()
#         line_layout.addItem(spacer)

#         self.remove_button = ViewButton(line_frame, text="REMOVE", cursor=True)
#         line_layout.addWidget(self.remove_button)

#         self.search_bar.input_field.textChanged.connect(self.on_search_edited)
#         self.refresh_button.clicked.connect(self.on_refresh_button_clicked)
#         self.remove_button.clicked.connect(self.on_remove_button_clicked)

#     def _init_table_section(self):
#         section_layout = VerticalLayout(self.table_section)

#         content_frame = Frame(self.table_section)
#         section_layout.addWidget(content_frame)

#         content_layout = VerticalLayout(content_frame)

#         header = OrderedDict()

#         header["Job ID"] = 180
#         header["Workers #"] = 70
#         header["Cores"] = 70
#         header["Memory"] = 70
#         header["Source File"] = 150
#         header["Input File"] = 150
#         header["Price"] = 80
#         header["Status"] = 80
#         header["Logs"] = 1

#         self.table = Table(
#             content_frame, RESOURCES_MAX_ROW, header, name="table_content_section"
#         )
#         content_layout.addWidget(self.table)
