from abc import ABCMeta, abstractmethod
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtCore import pyqtSignal, Qt

from ..widgets import (
    Frame,
    HorizontalLayout,
    HorizontalSpacer,
    Label,
    Scheme,
    StackLayout,
    SectionTitleFrame,
    VerticalLayout,
    VerticalSpacer,
    ViewButton,
    Button,
    ViewInputFrame,
)
from ..helper import switch_scheme

class JobsAddViewUI(Frame):
    """
    This component provides a workflow style interface to add current machine to job pool.
    """

    # metaclass for defining abstract base classes
    # Reference can be found here: https://docs.python.org/2/library/abc.html#abc.abstractmethod
    __metaclass__ = ABCMeta

    signal: pyqtSignal = None

    title_view: Frame = None
    stack_view: Frame = None
    stack: StackLayout = None
    button_view: Frame = None

    tech_sections: Frame = None
    eco_sections: Frame = None

    cancel: ViewButton = None
    back: ViewButton = None
    next_page: ViewButton = None
    submit: ViewButton = None

    global_hint: Label = None
    details_hint: Label = None

    details_section: Frame = None

    plan_section: Frame = None
    hint_button: Button = None

    # variable
    job_name: ViewInputFrame = None
    workers: ViewInputFrame = None
    cores: ViewInputFrame = None
    memory: ViewInputFrame = None

    def __init__(self, signal: pyqtSignal, cxt: ApplicationContext, *args, **kwargs):
        super(JobsAddViewUI, self).__init__(*args, name="view", **kwargs)

        self.cxt = cxt

        self.signal = signal
        self._init_ui()
        self._to_tech_section()
        self.setStyleSheet(self.cxt.jobs_add_view_style)

    def on_cancel_clicked(self):
        self.signal.emit()

    def on_back_clicked(self):
        self._to_tech_section()

    def on_next_page_clicked(self):
        # self._to_eco_section()
        pass

    def on_submit_clicked(self):
        # self.signal.emit()
        pass

    def _to_tech_section(self):
        self.stack.setCurrentWidget(self.tech_sections)

        self.next_page.setVisible(True)
        self.submit.setVisible(False)
        self.back.setVisible(False)

    def reset_hint(self):
        self.global_hint.reset()

    def _init_ui(self):

        window_layout = VerticalLayout(self)

        self.title_view = Frame(self, name="view_title_frame")
        window_layout.addWidget(self.title_view)
        self._init_title_view()

        self.stack_view = Frame(self, name="view_stack_frame")
        window_layout.addWidget(self.stack_view)
        self._init_stack_view()

        self.button_view = Frame(self, name="view_buttons_frame")
        window_layout.addWidget(self.button_view)
        self._init_button_view()

    def _init_title_view(self):

        layout = HorizontalLayout(self.title_view)

        title = Label(self.title_view, name="view_title", text="Add New Job")
        layout.addWidget(title)

        spacer = HorizontalSpacer()
        layout.addItem(spacer)

        self.global_hint = Label(self.title_view, name="section_hint")
        layout.addWidget(self.global_hint)

    def _init_stack_view(self):

        self.stack = StackLayout(self.stack_view)

        self.tech_sections = Frame(self.stack_view)
        self.stack.insertWidget(0, self.tech_sections)

        # self.eco_sections = Frame(self.stack_view)
        # self.stack.insertWidget(1, self.eco_sections)

        self._init_tech_sections()
        # self._init_eco_sections()    

    def _init_button_view(self):

        layout = HorizontalLayout(self.button_view, space=15)

        self.cancel = ViewButton(self.button_view, text="CANCEL", cursor=True)
        layout.addWidget(self.cancel)

        spacer = HorizontalSpacer()
        layout.addItem(spacer)

        self.back = ViewButton(self.button_view, text="BACK", cursor=True)
        layout.addWidget(self.back)

        self.next_page = ViewButton(self.button_view, text="NEXT", cursor=True)
        layout.addWidget(self.next_page)

        self.submit = ViewButton(self.button_view, text="SUBMIT", cursor=True)
        layout.addWidget(self.submit)

        # --------- binding event to function ---------

        self.cancel.clicked.connect(self.on_cancel_clicked)
        self.back.clicked.connect(self.on_back_clicked)
        self.next_page.clicked.connect(self.on_next_page_clicked)
        self.submit.clicked.connect(self.on_submit_clicked)

    def _init_tech_sections(self):
        sections_layout = VerticalLayout(self.tech_sections)

        self.details_section = Frame(self.tech_sections, name="section")
        sections_layout.addWidget(self.details_section)
        self._init_details_section()

        spacer = VerticalSpacer()
        sections_layout.addItem(spacer)

    def _init_details_section(self):
        section_layout = VerticalLayout(self.details_section)

        # title frame
        title_frame = SectionTitleFrame(
            self.details_section, label_one_text="Jobs Detail"
        )

        section_layout.addWidget(title_frame)
        self.details_hint = title_frame.get_label_two()

        # frame: two line frame contains inputs
        content_frame = Frame(self.details_section, name="details_content_frame")
        section_layout.addWidget(content_frame)

        content_layout = VerticalLayout(content_frame, space=18)

        # line_frame: job_name, workers
        line_frame = Frame(content_frame)
        content_layout.addWidget(line_frame)
        line_layout = HorizontalLayout(line_frame)

        self.job_name = ViewInputFrame(
            line_frame, title="Job Name:", title_width=113, fix_width=True
        )
        line_layout.addWidget(self.job_name)

        self.workers = ViewInputFrame(
            line_frame, title="Workers #:", title_width=113, fix_width=True
        )
        line_layout.addWidget(self.workers)

        # line_frame: memory, cores
        line_frame = Frame(content_frame)
        content_layout.addWidget(line_frame)
        line_layout = HorizontalLayout(line_frame)

        self.memory = ViewInputFrame(
            line_frame, title="Memory:", title_width=113, fix_width=True
        )
        line_layout.addWidget(self.memory)

        self.cores = ViewInputFrame(
            line_frame, title="Cores #:", title_width=113, fix_width=True
        )
        line_layout.addWidget(self.cores)

        # plan section
        self.plan_section = Frame(self.tech_sections, name="plan_content_frame")
        section_layout.addWidget(self.plan_section)
        self._init_plan_section()

    def _init_plan_section(self):
        section_layout = HorizontalLayout(self.plan_section)

        content = Label(self.plan_section, text="You are choosing: ", name="plan_label")
        section_layout.addWidget(content)

        plan = Label(self.plan_section, text="small model", name="plan_label")
        section_layout.addWidget(plan)

        spacer = HorizontalSpacer()
        section_layout.addItem(spacer)

        self.hint_button = Button(
            self.details_section, 
            text="What is Model?",
            name="hint_button", 
            cursor=True,
        )
        section_layout.addWidget(self.hint_button)

# class JobsAddViewUI(Frame):

#     # metaclass for defining abstract base classes
#     __metaclass__ = ABCMeta

#     pricing_scheme_section: Frame = None
#     job_submission_section: Frame = None

#     scheme_01_frame: Frame = None
#     scheme_02_frame: Frame = None
#     scheme_03_frame: Frame = None
#     scheme_04_frame: Frame = None

#     available_cpu: str = ""
#     available_gpu: str = ""
#     available_memory: str = ""
#     available_disk: str = ""

#     select_scheme: int = 1

#     pricing_scheme_hint: Label = None
#     submission_hint: Label = None

#     # variable
#     workers: ViewInputFrame = None
#     cores: ViewInputFrame = None
#     memory: ViewInputFrame = None
#     source_file: ViewInputFrame = None
#     input_file: ViewInputFrame = None
#     expect_time: ViewInputFrame = None

#     def __init__(self, signal: pyqtSignal, cxt: ApplicationContext, *args, **kwargs):
#         super(JobsAddViewUI, self).__init__(*args, name="view", **kwargs)

#         self.cxt = cxt
#         self.signal = signal
#         self._init_ui()
#         self.setStyleSheet(self.cxt.jobs_style)

#     def enable_scheme_01_frame(self, event):
#         switch_scheme(self, self.scheme_01_frame)
#         self.reload_stylesheet()
#         self.select_scheme = 1

#     def enable_scheme_02_frame(self, event):
#         switch_scheme(self, self.scheme_02_frame)
#         self.reload_stylesheet()
#         self.select_scheme = 2

#     def enable_scheme_03_frame(self, event):
#         switch_scheme(self, self.scheme_03_frame)
#         self.reload_stylesheet()
#         self.select_scheme = 3

#     def enable_scheme_04_frame(self, event):
#         switch_scheme(self, self.scheme_04_frame)
#         self.reload_stylesheet()
#         self.select_scheme = 4

#     def reload_stylesheet(self):
#         self.setStyleSheet(self.cxt.jobs_style)

#     @abstractmethod
#     def on_submit_clicked(self):
#         pass

#     @abstractmethod
#     def on_worker_edit(self):
#         pass

#     @abstractmethod
#     def on_core_edit(self):
#         pass

#     @abstractmethod
#     def on_memory_edit(self):
#         pass

#     @abstractmethod
#     def on_source_edit(self):
#         pass

#     @abstractmethod
#     def on_input_edit(self):
#         pass

#     def _init_ui(self):

#         layout = VerticalLayout(self)

#         self.pricing_scheme_section = Frame(self, name="section")
#         layout.addWidget(self.pricing_scheme_section)
#         self._init_pricing_scheme_section()

#         self.job_submission_section = Frame(self, name="section")
#         layout.addWidget(self.job_submission_section)
#         self._init_job_submission_section()

#         spacer = VerticalSpacer()
#         layout.addItem(spacer)

#     def _init_pricing_scheme_section(self):

#         section_layout = VerticalLayout(self.pricing_scheme_section)

#         title_frame = SectionTitleFrame(
#             self.pricing_scheme_section, label_one_text="Pricing Scheme"
#         )

#         section_layout.addWidget(title_frame)
#         self.pricing_scheme_hint = title_frame.get_label_two()

#         content_frame = Frame(self.pricing_scheme_section, name="scheme_content_frame")

#         section_layout.addWidget(content_frame)

#         content_layout = HorizontalLayout(content_frame)

#         # --------- left_section ------------

#         left_frame = Frame(content_frame, name="left")
#         content_layout.addWidget(left_frame)

#         left_layout = HorizontalLayout(left_frame, space=10)

#         scheme_frame = Frame(left_frame, name="scheme_title")
#         left_layout.addWidget(scheme_frame)

#         # --------- scheme_title_section ------------

#         scheme_layout = VerticalLayout(scheme_frame, space=16)

#         schemes = ["Time:", "CPU:", "GPU:", "Memory:", "Disk Space:"]

#         for scheme in schemes:
#             label = Label(
#                 scheme_frame,
#                 text=scheme,
#                 name="scheme_label_disable",
#                 align=Qt.AlignRight,
#             )
#             scheme_layout.addWidget(label)

#         # --------- scheme_01_frame ------------

#         self.scheme_01_frame = Scheme(
#             left_frame,
#             "12:00 AM - 5:59 AM",
#             self.enable_scheme_01_frame,
#             name="scheme",
#             label_name="scheme_label",
#         )
#         left_layout.addWidget(self.scheme_01_frame)

#         # --------- scheme_02_frame ------------

#         self.scheme_02_frame = Scheme(
#             left_frame,
#             "6:00 AM - 11:59 AM",
#             self.enable_scheme_02_frame,
#             name="scheme_disable",
#             label_name="scheme_label_disable",
#         )
#         left_layout.addWidget(self.scheme_02_frame)

#         # --------- scheme_03_frame ------------

#         self.scheme_03_frame = Scheme(
#             left_frame,
#             "12:00 PM - 5:59 PM",
#             self.enable_scheme_03_frame,
#             name="scheme_disable",
#             label_name="scheme_label_disable",
#         )
#         left_layout.addWidget(self.scheme_03_frame)

#         # --------- scheme_04_frame ------------

#         self.scheme_04_frame = Scheme(
#             left_frame,
#             "6:00 PM - 11:59 PM",
#             self.enable_scheme_04_frame,
#             name="scheme_disable",
#             label_name="scheme_label_disable",
#         )
#         left_layout.addWidget(self.scheme_04_frame)

#         space = HorizontalSpacer()
#         left_layout.addItem(space)

#         # --------- right_section: title, available cpu, gpu, memory, disk_space ------------

#         right_frame = Frame(content_frame, name="right")
#         content_layout.addWidget(right_frame)

#         right_layout = VerticalLayout(right_frame, space=16)

#         title = Label(right_frame, text="Available Resources", name="available_title")
#         right_layout.addWidget(title)

#         self.available_cpu = Label(right_frame, text="CPU #: 0", name="available_label")
#         right_layout.addWidget(self.available_cpu)

#         self.available_gpu = Label(right_frame, text="GPU #: 0", name="available_label")
#         right_layout.addWidget(self.available_gpu)

#         self.available_memory = Label(
#             right_frame, text="Memory: 0 GB", name="available_label"
#         )
#         right_layout.addWidget(self.available_memory)

#         self.available_disk = Label(
#             right_frame, text="Disk Space: 0 GB", name="available_label"
#         )
#         right_layout.addWidget(self.available_disk)

#     def _init_job_submission_section(self):

#         section_layout = VerticalLayout(self.job_submission_section)

#         title_frame = SectionTitleFrame(
#             self.pricing_scheme_section, label_one_text="Job Submission"
#         )

#         section_layout.addWidget(title_frame)
#         self.submission_hint = title_frame.get_label_two()

#         content_frame = Frame(
#             self.job_submission_section, name="submission_content_frame"
#         )

#         section_layout.addWidget(content_frame)

#         content_layout = VerticalLayout(content_frame, space=20)

#         line_frame = Frame(content_frame)
#         line_layout = HorizontalLayout(line_frame)
#         content_layout.addWidget(line_frame)

#         # --------- line_frame: workers, cores, memory ------------

#         self.workers = ViewInputFrame(
#             line_frame,
#             title="Workers #:",
#             title_width=70,
#             width=258,
#             fix_width=True,
#             title_align=(Qt.AlignRight | Qt.AlignVCenter),
#         )
#         line_layout.addWidget(self.workers)

#         self.cores = ViewInputFrame(
#             line_frame,
#             title="Cores #:",
#             title_width=70,
#             width=258,
#             fix_width=True,
#             title_align=(Qt.AlignRight | Qt.AlignVCenter),
#         )
#         line_layout.addWidget(self.cores)

#         self.memory = ViewInputFrame(
#             line_frame,
#             title="Memory:",
#             title_width=70,
#             width=258,
#             fix_width=True,
#             title_align=(Qt.AlignRight | Qt.AlignVCenter),
#         )
#         line_layout.addWidget(self.memory)

#         self.workers.input_field.textChanged.connect(self.on_worker_edit)
#         self.cores.input_field.textChanged.connect(self.on_core_edit)
#         self.memory.input_field.textChanged.connect(self.on_memory_edit)

#         # --------- source_file and input_file ------------

#         self.source_file = ViewInputFrame(
#             content_frame,
#             title="Source file:",
#             title_width=70,
#             title_align=(Qt.AlignRight | Qt.AlignVCenter),
#         )
#         content_layout.addWidget(self.source_file)

#         self.input_file = ViewInputFrame(
#             content_frame,
#             title="Input file:",
#             title_width=70,
#             title_align=(Qt.AlignRight | Qt.AlignVCenter),
#         )
#         content_layout.addWidget(self.input_file)

#         self.source_file.input_field.textChanged.connect(self.on_source_edit)
#         self.input_file.input_field.textChanged.connect(self.on_input_edit)

#         # --------- line_frame: submission_hint, spacer, submit_button ------------

#         line_frame = Frame(content_frame)
#         line_layout = HorizontalLayout(line_frame)
#         content_layout.addWidget(line_frame)

#         self.expect_time = ViewInputFrame(
#             line_frame,
#             title="Estimated\ntime:\n",
#             title_width=70,
#             title_align=(Qt.AlignRight | Qt.AlignVCenter),
#             hint="(Optional)",
#         )
#         line_layout.addWidget(self.expect_time)

#         spacer = HorizontalSpacer()
#         line_layout.addItem(spacer)

#         self.submit_button = ViewButton(line_frame, text="SUBMIT", cursor=True)
#         line_layout.addWidget(self.submit_button)

#         self.submit_button.clicked.connect(self.on_submit_clicked)
