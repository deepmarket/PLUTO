from fbs_runtime.application_context import ApplicationContext
from os import environ
from PyQt5.QtWidgets import QApplication

from mainapp import MainApp

# Removed by sgomena on 1/29/19 after directory structure refactoring
# sys.path.append(path.join(path.dirname(__file__), '..'))


class AppContext(ApplicationContext):
    def run(self):
        # app = QApplication(argv)
        # Save reference to main application so it's not garbage collected
        dont_garbage_collect_me = MainApp()
        return self.app.exec_()


if __name__ == '__main__':
    from sys import exit, argv

    # Enable headless for testing
    if environ.get('HEADLESS'):
        argv += ['-platform', 'minimal']

    appctxt = AppContext()
    exit_code = appctxt.run()
    exit(exit_code)
