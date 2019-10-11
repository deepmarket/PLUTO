from abc import ABCMeta, abstractmethod
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from ..widgets import (
    Frame,
    HorizontalLayout,
    HorizontalSpacer,
    Label,
    SectionTitleFrame,
    VerticalLayout,
    VerticalSpacer,
    ViewButton,
)
from ..config import VERSION


class SettingsUI(Frame):

    # metaclass for defining abstract base classes
    __metaclass__ = ABCMeta

    logo_section: Frame = None

    content_section: Frame = None
    faq_section: Frame = None
    dashboard_section: Frame = None
    resource_section: Frame = None
    jobs_section: Frame = None

    button_section: Frame = None

    save: ViewButton = None
    cancel: ViewButton = None

    def __init__(self, cxt: ApplicationContext, *args, **kwargs):
        super(SettingsUI, self).__init__(*args, name="settings", **kwargs)

        self.cxt = cxt

        self._init_ui()
        self.setStyleSheet(self.cxt.settings_style)

    @abstractmethod
    def on_save_button_clicked(self):
        pass

    @abstractmethod
    def on_cancel_button_clicked(self):
        pass

    def _init_ui(self):

        window_layout = VerticalLayout(self)

        self.logo_section = Frame(self, name="logo_section")
        window_layout.addWidget(self.logo_section)
        self._init_logo_section()

        self.content_section = Frame(self, name="content_section")
        window_layout.addWidget(self.content_section)
        self._init_content_section()

        self.button_section = Frame(self, name="button_section")
        window_layout.addWidget(self.button_section)
        self._init_button_section()

        self.save.clicked.connect(self.on_save_button_clicked)
        self.cancel.clicked.connect(self.on_cancel_button_clicked)

    def _init_logo_section(self):

        section_layout = HorizontalLayout(self.logo_section)

        title = Label(
            self.logo_section,
            text="Setting",
            name="setting_title",
            align=Qt.AlignVCenter,
        )
        section_layout.addWidget(title)

        spacer = HorizontalSpacer()
        section_layout.addItem(spacer)

        logo_frame = Frame(self.logo_section)
        logo_layout = VerticalLayout(logo_frame, space=8)
        section_layout.addWidget(logo_frame)

        # logo
        logo = Label(logo_frame)
        logo.setPixmap(QPixmap.fromImage(self.cxt.logo))
        logo.setAlignment(Qt.AlignHCenter)
        logo_layout.addWidget(logo)

        # version
        version = Label(
            logo_frame, text=f"PLUTO version: {VERSION}", name="setting_version"
        )
        logo_layout.addWidget(version)

    def _init_content_section(self):

        section_layout = VerticalLayout(self.content_section)

        self.faq_section = Frame(self.content_section)
        section_layout.addWidget(self.faq_section)
        self._init_faq_section()

        self.dashboard_section = Frame(self.content_section)
        section_layout.addWidget(self.dashboard_section)
        self._init_dashboard_section()

        self.resource_section = Frame(self.content_section)
        section_layout.addWidget(self.resource_section)
        self._init_resource_section()

        self.jobs_section = Frame(self.content_section)
        section_layout.addWidget(self.jobs_section)
        self._init_jobs_section()

    def _init_faq_section(self):

        section_layout = VerticalLayout(self.faq_section)

        # title_frame
        title_frame = SectionTitleFrame(self.faq_section, label_one_text="FAQ & Usage")
        section_layout.addWidget(title_frame)

        # setting_content
        content_frame = Frame(self.faq_section)
        content_layout = VerticalLayout(content_frame)
        section_layout.addWidget(content_frame)

        text = """
            To find the instruction of this PLUTO, please view our offical website <a href='https://deepmarket.cs.pdx.edu/' style='color: #6BADDE;'>here</a>.
        """
        label = Label(content_frame, text=text, name="link")
        label.setOpenExternalLinks(True)
        content_layout.addWidget(label)

    def _init_dashboard_section(self):

        section_layout = VerticalLayout(self.dashboard_section)

        # title_frame
        title_frame = SectionTitleFrame(
            self.dashboard_section, label_one_text="Dashboard Setting"
        )
        section_layout.addWidget(title_frame)

        # content_frame
        content_frame = Frame(self.dashboard_section, name="temp")
        content_layout = VerticalLayout(content_frame)
        section_layout.addWidget(content_frame)

        spacer = VerticalSpacer()
        content_layout.addItem(spacer)

    def _init_resource_section(self):

        section_layout = VerticalLayout(self.resource_section)

        # title_frame
        title_frame = SectionTitleFrame(
            self.resource_section, label_one_text="Resource Setting"
        )
        section_layout.addWidget(title_frame)

        # content_frame
        content_frame = Frame(self.resource_section, name="temp")
        content_layout = VerticalLayout(content_frame)
        section_layout.addWidget(content_frame)

        spacer = VerticalSpacer()
        content_layout.addItem(spacer)

    def _init_jobs_section(self):

        section_layout = VerticalLayout(self.jobs_section)

        # title_frame
        title_frame = SectionTitleFrame(
            self.jobs_section, label_one_text="Jobs Setting"
        )
        section_layout.addWidget(title_frame)

        # content_frame
        content_frame = Frame(self.jobs_section, name="temp")
        content_layout = VerticalLayout(content_frame)
        section_layout.addWidget(content_frame)

        spacer = VerticalSpacer()
        content_layout.addItem(spacer)

    def _init_button_section(self):

        section_layout = HorizontalLayout(self.button_section, space=15)

        spacer = HorizontalSpacer()
        section_layout.addItem(spacer)

        self.save = ViewButton(self.button_section, text="SAVE", cursor=True)
        section_layout.addWidget(self.save)

        self.cancel = ViewButton(self.button_section, text="CANCEL", cursor=True)
        section_layout.addWidget(self.cancel)
