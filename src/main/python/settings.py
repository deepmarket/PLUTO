"""
    The following items can be interacted:

    TODO
    class SettingsOverview:

    class SettingsWorkspace:

"""

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from mainview import MainView
from uix.util import *

class Settings(MainView):

    def __init__(self, cxt:ApplicationContext, *args, **kwargs):
        super(Settings, self).__init__(*args, **kwargs)

        self.workspace = None

        self.cxt = cxt
        self._init_ui()
        self.setStyleSheet(self.cxt.settings_style)

    def _init_ui(self):
        self.setObjectName("Settings")

        section_layout = add_layout(self, VERTICAL, b_m=8)

        window_frame = QFrame(self)
        section_layout.addWidget(window_frame)
        self.stack = add_layout(window_frame, STACK)


        self.workspace = SettingsWorkspace(window_frame, self.cxt)

        self.stack.addWidget(self.workspace)


class SettingsWorkspace(QFrame):

    def __init__(self, parent, cxt:ApplicationContext, *args, **kwargs):
        super(SettingsWorkspace, self).__init__(parent, *args, **kwargs)

        self.cxt = cxt
        self._init_ui()
        self.setStyleSheet(self.cxt.settings_style)

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

