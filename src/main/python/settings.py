from fbs_runtime.application_context.PyQt5 import ApplicationContext

# from mainview import MainView
from interfaces.settings import SettingsUI
from uix.util import *

class Settings(SettingsUI):

    def __init__(self, cxt:ApplicationContext, *args, **kwargs):
        super(Settings, self).__init__(cxt, *args, **kwargs)

    def on_save_button_clicked(self):

        #TODO: functional implement place here
        pass

    def on_cancel_button_clicked(self):

        #TODO: functional implement place here
        pass
