"""
    The following items can be interacted:

    TODO
    class SettingsOverview:

    class SettingsWorkspace:

"""

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from mainview import MainView
from uix.util import *


page_style = """

    #Page_sub_page {
        background-color: white;
    }
    
    #Page_machine_config {
        background-color: #D6EFEF;
    }
    
    #Page_resource_planning {
        background-color: #F4F8F9;
    }
    
    #Page_resource_submission {
        background-color: #F4F8F9;
    }
    
    #Page_scheme {
        background-color: #F4F8F9;
    }
    
    #Page_available_resources {
        background-color: #D6EFEF;
    }
    
    #Page_job_submission {
        background-color: #F4F8F9;
    }
    
    #Page_section_title {
        font-family: "Helvetica Neue";
        font-size: 20px;
        font-weight: 100;
        color: #6C7E8E;
    }
    
    #Page_section_title_small {
        font-family: "Helvetica Neue";
        font-size: 16px;
        font-weight: 300;
        color: #6C7E8E;
    }
    
    #Page_hint {
        font-family: "Helvetica Neue";
        font-size: 12px;
        font-weight: 300;
        color: red;
    }
    
    #Page_hint_small {
        font-family: "Helvetica Neue";
        font-size: 11px;
        font-weight: 300;
        color: red;
    }

    #Page_input_frame {
        background-color: white;
    }

    #Page_input_title {
        font-family: "Helvetica Neue";
        font-size: 13px;
        font-weight: 300;
        color: #6C7E8E;
    }
    
    #Page_button {
        border: None;
        background-color: #6C7E8E;
        height: 30px;
        width: 120px;
        font-family: "Helvetica Neue";
        font-size: 12px;
        font-weight: 300;
        color: white;
    }

    #Page_available_title {
        font-family: "Helvetica Neue";
        font-size: 12px;
        font-weight: 500;
        color: #6C7E8E;
    }
    
    #Page_available_label {
        font-family: "Helvetica Neue";
        font-size: 11px;
        font-weight: 500;
        color: #6C7E8E;
    }
    
    #Page_table_workspace {
        background-color: white;
    }

    #Page_table_test {
        background-color: yellow;
    }
    
    #Page_table_workspace_search {
        border: None;
        background-color: #F7F7F7;
        padding: 0 20px;
        font-family: "Helvetica Neue";
        font-size: 13px;
        font-weight: 200;
        color: black;
    }
    
    #Page_table_workspace_button {
        border: None;
        background-color: #6C7E8E;
        height: 35px;
        width: 90px;
        font-family: "Helvetica Neue";
        font-size: 13px;
        font-weight: 200;
        color: white;
    }
    
    #Page_table {
        border: none;
        background-color: white;
        alternate-background-color: #FAFAFA;
    }
    
    #Page_table QHeaderView::section {
        border: none;
        background-color: #6C7E8E;
        height: 35px;
        font-family: "Helvetica Neue";
        font-size:13px;
        font-weight: 100;
        color: white;
    }
"""

class Settings(MainView):

    def __init__(self, cxt:ApplicationContext, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)

        self.workspace = None

        self._init_ui()
        self.setStyleSheet(page_style)

    def _init_ui(self):
        self.setObjectName("Settings")

        section_layout = add_layout(self, VERTICAL, b_m=8)

        window_frame = QFrame(self)
        section_layout.addWidget(window_frame)
        self.stack = add_layout(window_frame, STACK)

        self.workspace = SettingsWorkspace()

        self.stack.addWidget(self.workspace)


class SettingsWorkspace(QFrame):

    def __init__(self, *args, **kwargs):
        super(QFrame, self).__init__(*args, **kwargs)

        self._init_ui()
        self.setStyleSheet(page_style)

    def _init_ui(self):

        self.setObjectName("Page_sub_page")
        window_layout = add_layout(self, VERTICAL, t_m=10, l_m=50, r_m=46, space=30)

        section_frame, section_layout = add_frame(self, height=78, space=18)
        window_layout.addWidget(section_frame)

        line_frame, line_layout = add_frame(section_frame, layout=VERTICAL, r_m=3)
        section_layout.addWidget(line_frame)

        title = add_label(line_frame, "General Settings", name="Page_section_title", align=Qt.AlignVCenter)
        line_layout.addWidget(title)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

        version_label = add_label(line_frame, f"PLUTO version {VERSION}", name="Version_label", align=Qt.AlignVCenter)
        line_layout.addWidget(version_label)

        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        line_layout.addItem(spacer)

