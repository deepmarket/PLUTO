from fbs_runtime.application_context.PyQt5 import ApplicationContext
from app import App
from login import Login
from PyQt5.QtCore import QObject, pyqtSignal


class MainApp(QObject):
    login_signal = pyqtSignal()
    logout_signal = pyqtSignal()

    def __init__(
        self, cxt: ApplicationContext, dont_boot_for_test=True, *args, **kwargs
    ):
        super(QObject, self).__init__(*args, **kwargs)
        self.dont_boot_for_test = dont_boot_for_test
        self.login = None
        self.app = None

        self.cxt = cxt

        self.show_login()
        self.connect_login()
        self.connect_logout()

    def show_login(self):
        self.login = Login(self.login_signal, self.cxt)
        # TODO: Candidate for deprecation; tests should handle testing like a user would use the application
        if self.dont_boot_for_test:
            self.login.show()

    def show_app(self):
        self.app = App(self.logout_signal, self.cxt)
        self.app.show()

    def connect_login(self):
        self.login_signal.connect(self.show_app)

    def connect_logout(self):
        self.logout_signal.connect(self.show_login)
