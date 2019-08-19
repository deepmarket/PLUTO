from fbs_runtime.application_context.PyQt5 import ApplicationContext
from fbs_runtime.application_context import cached_property
from os import environ

from mainapp import MainApp

# Removed by sgomena on 1/29/19 after directory structure refactoring
# sys.path.append(path.join(path.dirname(__file__), '..'))


class AppContext(ApplicationContext):

    def __init__(self, *args, **kwargs):
        super(AppContext, self).__init__(*args, **kwargs)
        self.mainapp = MainApp(self)

    @cached_property
    def dashboard_style(self):
        return self.load_style("dashboard.qss")

    @cached_property
    def app_style(self):
        return self.load_style("app.qss")

    @cached_property
    def login_style(self):
        return self.load_style("login.qss")

    @cached_property
    def credit_history_style(self):
        return self.load_style("credit_history.qss")

    @cached_property
    def notification_style(self):
        return self.load_style("notification.qss")

    @cached_property
    def add_view_style(self):
        return self.load_style("popup.qss")

    @cached_property
    def controller_style(self):
        return self.load_style("controller.qss")
    
    @cached_property
    def popup_style(self):
        return self.load_style("popup.qss")

    # def __init__(self):
    #     popup_style = self.get_resource("popup.qss")
    #     resources_add_view_style = self.get_resource("add_view.qss")
    #     resources_controller_style = self.get_resource("controller.qss")

    def run(self):
        # Save reference to main application so it's not garbage collected
        # dont_garbage_collect_me = MainApp(self)
        return self.app.exec_()

    def load_style(self, path):
        try:
            file_path = self.get_resource(path)
            with open(file_path) as f:
                return f.read()
        except FileNotFoundError:
            err = "%s is not found." % path
            raise FileNotFoundError(err)

if __name__ == '__main__':
    from sys import exit, argv

    # check we're in correct directory
    # if os.path.abspath(os.getcwd()).split(os.sep)[-1] != "PLUTO":
    #     exit("Must be in the root project directory to run main app!")

    # Enable headless for testing
    if environ.get('HEADLESS'):
        argv += ['-platform', 'minimal']

    appctxt = AppContext()
    exit_code = appctxt.run()
    exit(exit_code)
