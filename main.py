import os
import sys
from PyQt5.QtWidgets import QApplication

from src.app import App
from src.login import Login

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

if __name__ == '__main__':
    from sys import exit, argv
    app = QApplication(argv)

    # main_app = App()  # Instantiate the application
    # exit(app.exec_())  # Return control to original event loop

    login = Login()
    login.show()

    # login.exec_() return True if user successfully signed in
    if login.exec_():
        main_app = App()  # Instantiate the application
        exit(app.exec_())  # Return control to original event loop
