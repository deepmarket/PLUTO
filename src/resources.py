"""

    The interface implemented at this file provide the following features:
    1. ResourcesWorkspace: Allow user add current machine to resources pool
    2. ResourcesList: View the existing machines that are lent

"""

# from psutil import cpu_freq, cpu_count, virtual_memory

# from mainview import MainView
# from uix.util import *
# from uix.config import *
# from uix.popup import Question
# from api import Api

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
        super()._to_add_view()


class ResourcesController(ResourcesControllerUI):

    def __init__(self, *args, **kwargs):
        super(ResourcesController, self).__init__(*args, **kwargs)


class ResourcesAddView(ResourcesAddViewUI):

    def __init__(self, *args, **kwargs):
        super(ResourcesAddView, self).__init__(*args, **kwargs)
