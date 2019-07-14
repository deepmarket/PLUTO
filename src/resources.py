"""

    The interface implemented at this file provide the following features:
    1. ResourcesWorkspace: Allow user add current machine to resources pool
    2. ResourcesList: View the existing machines that are lent

"""

from enum import Enum, auto
from psutil import cpu_freq, cpu_count, virtual_memory

# from mainview import MainView
# from uix.util import *
# from uix.config import *
# from uix.popup import Question
# from api import Api

import util as util
from interfaces.resources import ResourcesUI, ResourcesControllerUI, ResourcesAddViewUI


class Resources(ResourcesUI):

    def __init__(self, *args, **kwargs):
        super(Resources, self).__init__(*args, **kwargs)

        self.controller = ResourcesController(self._to_add_view_signal)
        self.add_view = ResourcesAddView(self._to_controller_signal)

        self.set_controller(self.controller)
        self.set_add_view(self.add_view)

    def _to_controller(self):
        super()._to_controller()

    def _to_add_view(self):
        self.add_view.reset()
        super()._to_add_view()


class ResourcesController(ResourcesControllerUI):

    def __init__(self, *args, **kwargs):
        super(ResourcesController, self).__init__(*args, **kwargs)


class ResourcesAddView(ResourcesAddViewUI):

    available_cpu_gpu               : int = 0
    available_cores                 : int = 0
    available_ram                   : int = 0

    def __init__(self, *args, **kwargs):
        super(ResourcesAddView, self).__init__(*args, **kwargs)

        self._fetch_ip_address()
        self._fetch_machine_config()

    def on_machine_name_edit(self):
        self._machine_name_check()

    def on_cpu_gpu_edit(self):
        self._cpu_gpu_check()

    def on_cores_edit(self):
        self._cores_check()

    def on_ram_edit(self):
        self._ram_check()

    def on_next_page_clicked(self):

        if not self._planning_check():
            return
        super().on_next_page_clicked()

    def reset(self):
        super().reset()
        self.available_cpu_gpu = 0
        self.available_cores = 0
        self.available_ram = 0

        self._fetch_ip_address()
        self._fetch_machine_config()

    def _fetch_ip_address(self):
        # get ip address for local machine
        ip_address = util.get_ip_address()

        # insert ip address to input field
        self.ip_address.setText(ip_address)

        # disable input field
        self.disable_section(self.verification_section)

    def _fetch_machine_config(self):

        # Processor's speed in gHz
        self.available_cpu_gpu = round(cpu_freq().current/1000, 1)

        # Logical cores on the machine
        self.available_cores = cpu_count(logical=False)

        # Total installed RAM
        self.available_ram = round(virtual_memory().total/(pow(1024, 3)), 1)

        self.set_config_text(self.current_cpu_gpu, f"{self.available_cpu_gpu} GHz")
        self.set_config_text(self.current_cores, f"{self.available_cores}")
        self.set_config_text(self.current_ram, f"{self.available_ram} GB")

    def _planning_check(self):
        # clean up hint
        self.reset_hint()

        # have to call function individually in order to raise hint
        if not self._machine_name_check(): return False
        if not self._cpu_gpu_check(): return False
        if not self._cores_check(): return False
        if not self._ram_check(): return False

        return True

    def _machine_name_check(self):
        # clean up hint
        self.reset_hint()

        if self.machine_name.text() is "":
            self.set_hint(self.planning_hint, "Please enter a machine name.")
            return False
        return True

    def _cpu_gpu_check(self):
        # clean up hint
        self.reset_hint()

        # set error message
        class Res(Enum):
            EMPTY_ERROR = "Please enter number of GPUs."
            RANGE_ERROR = "Input for GPUs is out of range."
            INT_ERROR = "Please enter an interger input"
            SUCCESS = auto()

        # check if input is acceptable
        res = util.config_input_check(self.cpu_gpu.text(), self.available_cpu_gpu, Res)

        if res is not Res.SUCCESS:
            self.set_hint(self.planning_hint, res.value)
            self.set_config_red(self.current_cpu_gpu)
            return False

        self.set_config_green(self.current_cpu_gpu)
        return True

    def _cores_check(self):
        # clean up hint
        self.reset_hint()

        # set error message
        class Res(Enum):
            EMPTY_ERROR = "Invalid number of cores."
            RANGE_ERROR = "Cores is out of range."
            INT_ERROR = "Please enter an interger input"
            SUCCESS = auto()

        # check if input is acceptable
        res = util.config_input_check(self.cores.text(), self.available_cores, Res)

        if res is not Res.SUCCESS:
            self.set_hint(self.planning_hint, res.value)
            self.set_config_red(self.current_cores)
            return False

        self.set_config_green(self.current_cores)
        return True

    def _ram_check(self):
        # clean up hint
        self.reset_hint()

        # set error message
        class Res(Enum):
            EMPTY_ERROR = "Please enter number of RAM."
            RANGE_ERROR = "Amount of RAM is out of range."
            INT_ERROR = "Please enter an interger input"
            SUCCESS = auto()

        # check if input is acceptable
        res = util.config_input_check(self.ram.text(), self.available_ram, Res)

        if res is not Res.SUCCESS:
            self.set_hint(self.planning_hint, res.value)
            self.set_config_red(self.current_ram)
            return False

        self.set_config_green(self.current_ram)
        return True
