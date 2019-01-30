from os import environ, path
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog

from src.app import App
from src.login import Login

sys.path.append(path.join(path.dirname(__file__), '..'))

if __name__ == '__main__':
    from sys import exit, argv

    # Enable headless for testing
    if environ.get('HEADLESS'):
        argv += ['-platform', 'minimal']

    def show_login():
        login = Login()
        # result = login.show()

        # login.exec_() return True if user successfully signed in
        if login.exec_():
            main_app = App()  # Instantiate the application

            app.exec_()


    app = QApplication(argv)
    app.aboutToQuit.connect(show_login)

    show_login()
