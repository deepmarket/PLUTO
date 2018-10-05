from os import environ, path
import sys
from PyQt5.QtWidgets import QApplication

from src.app import App
from src.login import Login

sys.path.append(path.join(path.dirname(__file__), '..'))

if __name__ == '__main__':
    from sys import exit, argv

    # Enable headless for testing
    if environ.get('HEADLESS'):
        argv += ['-platform', 'minimal']

    app = QApplication(argv)

    login = Login()
    login.show()

    # login.exec_() return True if user successfully signed in
    if login.exec_():
        main_app = App()  # Instantiate the application

        app.exec_()
        # exit(app.exec_())  # Return control to original event loop
