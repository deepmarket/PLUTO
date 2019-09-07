from fbs_runtime.application_context.PyQt5 import ApplicationContext

from ..widgets import Frame, VerticalLayout, HorizontalLayout, HorizontalSpacer, ViewButton, SearchInputFrame, Table

from ..config import RESOURCES_MAX_ROW
from collections import OrderedDict

class JobsControllerUI(Frame):

    search_section: Frame = None
    table_section: Frame = None

    # variable
    table = None                   
    search_bar = None       
    refresh_button = None          
    remove_button = None     

    def __init__(self, cxt:ApplicationContext, *args, **kwargs):
        super(JobsControllerUI, self).__init__(*args, **kwargs)

        self.cxt = cxt

        self._init_ui()
        self.setStyleSheet(self.cxt.jobs_style)

    def _init_ui(self):
        
        layout = VerticalLayout(self)
        
        # --------- table_workspace ------------

        self.search_section = Frame(self, name="controller")
        layout.addWidget(self.search_section)
        self._init_search_section()

        # --------- table_frame ----------------

        self.table_section = Frame(self, name="table")
        layout.addWidget(self.table_section)
        self._init_table_section()

    def _init_search_section(self):

        section_layout = HorizontalLayout(self.search_section)

        content_frame = Frame (
            self.search_section
        )
        section_layout.addWidget(content_frame)

        content_layout = HorizontalLayout(content_frame, space=32)

        line_frame = Frame(content_frame)
        line_layout = HorizontalLayout(line_frame)
        content_layout.addWidget(line_frame)

        self.search_bar = SearchInputFrame(
            line_frame, hint="Search a job... (Haven't implemented yet)", input_width=600
        )
        line_layout.addWidget(self.search_bar)

        spacer = HorizontalSpacer()
        line_layout.addItem(spacer)

        self.refresh_button = ViewButton(
            line_frame, text="REFRESH", cursor=True
        )
        line_layout .addWidget(self.refresh_button)
        
        spacer = HorizontalSpacer()
        line_layout.addItem(spacer)

        self.remove_button = ViewButton(
            line_frame, text="REMOVE", cursor=True
        )
        line_layout.addWidget(self.remove_button)

    def _init_table_section(self):
        section_layout = VerticalLayout(self.table_section)

        content_frame = Frame (
            self.table_section
        )
        section_layout.addWidget(content_frame)

        content_layout = VerticalLayout(content_frame)

        header = OrderedDict()

        header["Job ID"] = 180
        header["Workers #"] = 70
        header["Cores"] = 70
        header["Memory"] = 70
        header["Source File"] = 150
        header["Input File"] = 150
        header["Price"] = 80
        header["Status"] = 80
        header["Logs"] = 1

        self.table = Table(content_frame, RESOURCES_MAX_ROW, header, name="table_content_section")
        content_layout.addWidget(self.table)