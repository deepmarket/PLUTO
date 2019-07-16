"""

    The interface implemented at this file provide the following features:
    1. ResourcesWorkspace: Allow user add current machine to resources pool
    2. ResourcesList: View the existing machines that are lent

"""

from enum import Enum, auto
from psutil import cpu_freq, cpu_count, virtual_memory

from api import Api

import util as util
from interfaces.resources import ResourcesUI, ResourcesControllerUI, ResourcesAddViewUI
from interfaces.widgets import Question


class Resources(ResourcesUI):

    def __init__(self, *args, **kwargs):
        super(Resources, self).__init__(*args, **kwargs)

        self.controller = ResourcesController(self._to_add_view_signal)
        self.add_view = ResourcesAddView(self._to_controller_signal)

        self.set_controller(self.controller)
        self.set_add_view(self.add_view)

    def _to_controller(self):
        self.controller.reset()
        super()._to_controller()

    def _to_add_view(self):
        self.add_view.reset()
        super()._to_add_view()

        self.add_view.machine_name.setText("mac")
        self.add_view.cpu_gpu.setText("1")
        self.add_view.cores.setText("1")
        self.add_view.ram.setText("1")


class ResourcesController(ResourcesControllerUI):

    machines : list = None

    def __init__(self, *args, **kwargs):
        super(ResourcesController, self).__init__(*args, **kwargs)

        self._fetch_resources_data()

    def on_refresh_button_clicked(self):
        self.reset()

    def on_edit_button_clicked(self):
        pass

    def on_remove_button_clicked(self):

        # check if table has selection
        # if it does, get the row info
        row = self.table.if_select()

        if row != -1:
            machine_name = self.table.get_cell(row, 0)

            question = f"Are you sure you want to remove <u>{machine_name}</u> from your resources?\n"
            question += "** This action cannot be undone. **"

            dialog = Question(question)

            if dialog.exec_():
                res = self._api_remove_call(f"/resources/{self.machines[row]['_id']}")
                if res:
                    # refresh widget
                    self.reset()

                    # raise success message
                    msg = f"Machine {machine_name} has been removed sucessfully."
                    self.set_hint(self.global_hint, msg)

    def on_search_edited(self):
        pass

    def reset(self):
        super().reset()
        self._fetch_resources_data()

    def _fetch_resources_data(self):
        self.machines = self._api_get_call("/resources")
        for machine in self.machines:
            self.table.add([machine["machine_name"],
                            machine["ip_address"],
                            str(machine["cpus"]),
                            str(machine["cores"]),
                            str(machine["ram"]),
                            str(machine["price"]),
                            machine["status"]])

    def _api_get_call(self, endpoint:str):

        # TODO: move Error to config later on
        class Error:
            CONNECT_ERR = "Fail to communicate with server. Please try later."
            UNKOWN_ERR = "There was an unknown error from the server. Please try again."

        with Api(endpoint) as api:
            status, res = api.get()

            if not res:
                self.set_hint(self.global_hint, Error.CONNECT_ERR)
                return []

            if status == 200:
                return res["resources"]

            if status == 500:
                self.set_hint(self.global_hint, Error.UNKOWN_ERR)
                return []

    # TODO: combine api call helper function together later on
    def _api_remove_call(self, endpoint:str):
        # TODO: move Error to config later on
        class Error:
            CONNECT_ERR = "Fail to communicate with server. Please try later."
            UNKOWN_ERR = "There was an unknown error from the server. Please try again."

        with Api(endpoint) as api:
            status, res = api.delete()

            if not res:
                self.set_hint(self.global_hint, Error.CONNECT_ERR)
                return False

            if status == 200:
                return True

            if status == 500:
                self.set_hint(self.global_hint, Error.UNKOWN_ERR)
                return False

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

    def on_submit_clicked(self):

        # fetch user input
        machine_name = self.machine_name.text()
        ip_address = self.ip_address.text()
        cpu_gpu = self.cpu_gpu.text()
        cores = self.cores.text()
        ram = self.ram.text()

        # TODO: replace this when price section finished
        price = 0

        # pack data
        dat = {
            "machine_name": machine_name,
            "ip_address": ip_address,
            "cpus": cpu_gpu,
            "cores": cores,
            "ram": ram,
            "price": price,
            "status": "ALIVE"
        }

        # api call
        res = self._api_post_call("/resources", dat)

        if res:
            # TODO: fill helper function to run docker here

            # emit signal, back to controller
            super().on_submit_clicked()

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

    def _api_post_call(self, endpoint:str, dat:dict):

        # TODO: move Error to config later on
        class Error:
            E11000_ERR = "This IP address is already in use. Please use a different one."
            UNKOWN_ERR = "There was an unknown error from the server. Please try again."
            CONNECT_ERR = "Fail to communicate with server. Please try later."

        with Api(endpoint) as api:
            status, res = api.post(dat)

            if not res:
                self.set_hint(self.submit_hint, Error.CONNECT_ERR)
                return False

            if status == 200:
                return True

            if status == 500:
                msg = ""
                if res and "error" in res and "errmsg" in res["error"]:
                    msg = res["error"]["errmsg"]
                    if "E11000" in msg:
                            msg = Error.E11000_ERR
                else:
                    msg = Error.UNKOWN_ERR

                self.set_hint(self.submit_hint, msg)
                return False


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
