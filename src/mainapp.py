
from app import App
from login import Login
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QDialog


class MainApp(QObject):
    login_signal = pyqtSignal()
    logout_signal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(QObject, self).__init__(*args, **kwargs)
        self.login = None
        self.app = None
        self.show_login()
        self.connect_login()
        self.connect_logout()

    def show_login(self):
        self.login = Login(self.login_signal)
        self.login.show()

    def show_app(self):
        self.app = App(self.logout_signal)
        self.app.show()

    def connect_login(self):
        self.login_signal.connect(self.show_app)

    def connect_logout(self):
        self.logout_signal.connect(self.show_login)

