
from app import App
from login import Login
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class MainApp(QObject):
    logout = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(QObject, self).__init__(*args, **kwargs)
        self.main_app = None
        self.connect_logout()
        self.show_login()

    def show_login(self):
        login = Login()

        login_ok = login.exec_()
        if login_ok:
            # Instantiate the application
            self.main_app = App(self.logout)
            self.main_app.show()
        # Do we care about this case?
        # else:
        #     pass

    def connect_logout(self):
        self.logout.connect(self.show_login)

