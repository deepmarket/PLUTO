from enum import Enum, auto
from fbs_runtime.application_context.PyQt5 import ApplicationContext

from api import Api
from util import job_input_check

from interfaces.jobs import JobsUI, JobsAddViewUI, JobsControllerUI
from interfaces.widgets import Question


class Jobs(JobsUI):
    def __init__(self, cxt: ApplicationContext, *args, **kwargs):
        super(Jobs, self).__init__(cxt, *args, **kwargs)

        self.cxt = cxt

        self.add_view = JobsAddView(self._to_controller_signal, self.cxt)
        self.controller = JobsController(self._to_add_view_signal, self.cxt)

        self.set_add_view(self.add_view)
        self.set_controller(self.controller)

        self.on_add_view_button_clicked()

    def _to_add_view(self):
        # self.add_view.reset()
        super()._to_add_view()

    def _to_controller(self):
        self.controller.reset()
        super()._to_controller()


class JobsAddView(JobsAddViewUI):
    def __init__(self, *args, **kwargs):
        super(JobsAddView, self).__init__(*args, **kwargs)

    # input data format: [job_id, workers, cores, memory, price, status, logs]
    def on_submit_clicked(self):

        if not self._submission_check():
            return

        workers_cnt = self.workers.text()
        cores_cnt = self.cores.text()
        memory_cnt = self.memory.text()
        source_files = self.source_file.text()
        input_files = self.input_file.text()
        expected_time = self.expect_time.text()
        price = "0.005"
        # price = (float(cores) * float(workers)) * PRICING_CONSTANT

        dat = {
            "timeslot_id": self.select_scheme - 1,
            "workers": workers_cnt,
            "cores": cores_cnt,
            "memory": memory_cnt,
            "source_files": [source_files],
            "input_files": [input_files],
            "price": price,
            "expected_time": expected_time,
            "customer_id": "customer_id",
        }

        # find the selected frame
        if self.select_scheme == 1:
            frame = self.scheme_01_frame
        elif self.select_scheme == 2:
            frame = self.scheme_02_frame
        elif self.select_scheme == 3:
            frame = self.scheme_03_frame
        else:
            frame = self.scheme_04_frame

        # get text
        text = frame.get_info()

        from random import choices
        from string import ascii_uppercase, digits

        job_id = "J"
        job_id += "".join(choices(ascii_uppercase + digits, k=6))

        question = f"""
            Job '{job_id}' will be charged for using:
            {text[1]} per CPU/hr, {text[2]} per GPU/hr, and {text[3]} per GB/hr of memory.
            \n
            It will run between {text[0]}.
            
            Do you want to submit this job at the aforementioned rate and time?
        """

        question = Question(question, self.cxt)

        if question.exec_():
            res = self._api_post_call("/jobs", dat)

            if res:
                self.signal.emit()

    def on_worker_edit(self):
        self._on_worker_check()

    def on_core_edit(self):
        self._on_core_check()

    def on_memory_edit(self):
        self._on_memory_check()

    def on_source_edit(self):
        self._on_source_check()

    def on_input_edit(self):
        self._on_input_check()

    def _submission_check(self):

        # clean up hint
        self.submission_hint.reset()

        # have to call function individually in order to raise hint
        if not self._on_worker_check():
            return False
        if not self._on_core_check():
            return False
        if not self._on_memory_check():
            return False
        if not self._on_source_check():
            return False
        if not self._on_input_check():
            return False

        return True

    def _on_worker_check(self):
        # clean up hint
        self.submission_hint.reset()

        class Res(Enum):
            EMPTY_ERROR = "Please enter value of WORKER."
            INT_ERROR = "Please enter an interger input"
            SUCCESS = auto()

        # check if input is acceptable
        res = job_input_check(self.workers.text(), Res)

        if res is not Res.SUCCESS:
            self.submission_hint.setText(res.value)

            return False

        return True

    def _on_core_check(self):
        # clean up hint
        self.submission_hint.reset()

        class Res(Enum):
            EMPTY_ERROR = "Please enter value of CORES."
            INT_ERROR = "Please enter an interger input"
            SUCCESS = auto()

        # check if input is acceptable
        res = job_input_check(self.cores.text(), Res)

        if res is not Res.SUCCESS:
            self.submission_hint.setText(res.value)

            return False

        return True

    def _on_memory_check(self):

        # clean up hint
        self.submission_hint.reset()

        class Res(Enum):
            EMPTY_ERROR = "Please enter value of MEMORY."
            INT_ERROR = "Please enter an interger input"
            SUCCESS = auto()

        # check if input is acceptable
        res = job_input_check(self.memory.text(), Res)

        if res is not Res.SUCCESS:
            self.submission_hint.setText(res.value)

            return False

        return True

    def _on_source_check(self):

        # clean up hint
        self.submission_hint.reset()

        if self.source_file.text() is "":
            self.submission_hint.setText("Please enter a source file.")
            return False
        return True

    def _on_input_check(self):

        # clean up hint
        self.submission_hint.reset()

        if self.input_file.text() is "":
            self.submission_hint.setText("Please enter a input file.")
            return False
        return True

    def _api_post_call(self, endpoint: str, dat: dict):
        with Api(endpoint) as api:
            status, res = api.post(dat)
            return res and status == 200


class JobsController(JobsControllerUI):
    def __init__(self, *args, **kwargs):
        super(JobsController, self).__init__(*args, **kwargs)

    def on_search_edited(self):
        pass

    def on_refresh_button_clicked(self):
        self.reset()

    def on_remove_button_clicked(self):

        # check if table has selection
        # if it does, get the row info
        row = self.table.if_select()

        if row != -1:
            job_id = self.table.get_cell(row, 0)

            question = f"Are you sure you want to remove <u>{job_id}</u> from your resources?\n"
            question += "** This action cannot be undone. **"

            dialog = Question(question, self.cxt)

            if dialog.exec_():
                res = self._api_remove_call(f"/jobs/{self.jobs[row]['_id']}")
                if res:
                    # refresh widget
                    self.reset()

    def _api_remove_call(self, endpoint: str):

        with Api(endpoint) as api:
            status, res = api.delete()

            if not res:
                return False

            if status == 200:
                return True

            if status == 500:
                return False

    def reset(self):
        super().reset()
        self._fetch_job_data()

    def _fetch_job_data(self):
        self.jobs = self._api_get_call("/jobs")
        for job in self.jobs:
            self.table.add(
                [
                    job["_id"],
                    job["workers"],
                    job["cores"],
                    job["memory"],
                    str(job["source_files"][0] + "..."),
                    str(job["input_files"][0] + "..."),
                    str(job["price"]),
                    job["status"],
                    "-",
                ]
            )

    def _api_get_call(self, endpoint: str):

        with Api(endpoint) as api:
            status, res = api.get()

            if not res:
                return []

            if status == 200:
                return res["jobs"]

            if status == 500:
                return []
