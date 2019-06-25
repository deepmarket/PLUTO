from fbs_runtime.application_context import ApplicationContext
from sentry_sdk import init as sentry_init
from os import environ

from mainapp import MainApp

# Removed by sgomena on 1/29/19 after directory structure refactoring
# sys.path.append(path.join(path.dirname(__file__), '..'))

# This adds error logging to sentry to the application
sentry_init("https://808ef6c5e4d44f8da61403d525199d15@sentry.io/1487972")


class AppContext(ApplicationContext):
    def run(self):
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
