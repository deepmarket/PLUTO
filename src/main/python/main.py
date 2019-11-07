from os import environ, path

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from fbs_runtime.application_context import cached_property

from PyQt5.QtGui import QImage

from mainapp import MainApp

# Removed by sgomena on 1/29/19 after directory structure refactoring
# sys.path.append(path.join(path.dirname(__file__), '..'))


class AppContext(ApplicationContext):
    def __init__(self, *args, **kwargs):
        super(AppContext, self).__init__(*args, **kwargs)
        # Save reference to main application so it's not garbage collected
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
    def add_view_style(self):
        return self.load_style("resources_add_view.qss")

    @cached_property
    def controller_style(self):
        return self.load_style("resources_controller.qss")

    @cached_property
    def popup_style(self):
        return self.load_style("popup.qss")

    @cached_property
    def jobs_style(self):
        return self.load_style("jobs.qss")

    @cached_property
    def settings_style(self):
        return self.load_style("settings.qss")

    @cached_property
    def logo(self):
        return QImage(self.get_resource("logo.png"))

    @cached_property
    def question_style(self):
        return self.load_style("question.qss")

    @cached_property
    def credential_store(self):
        store_name: str = "store"
        try:
            # Get abs path to the store; platform independent
            store: str = self.get_resource(store_name)
        except FileNotFoundError:
            # TODO: At this point we cannot create the file so we'll need to handle this somehow
            store: str = "store"
            pass

        finally:
            return store

    def run(self):
        return self.app.exec_()

    def load_style(self, path):
        try:
            file_path = self.get_resource(path)
            with open(file_path) as f:
                return f.read()
        except:
            raise


if __name__ == "__main__":
    from sys import exit, argv

    # Enable headless for testing
    if environ.get("HEADLESS"):
        argv += ["-platform", "minimal"]

    appctxt = AppContext()
    exit_code = appctxt.run()
    exit(exit_code)
