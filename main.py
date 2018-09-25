import os
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from src.app import App
from src.login import Login

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

if __name__ == '__main__':
    from sys import exit, argv
    argv += ['-platform', 'minimal']
    app = QApplication(argv)
    app.aboutToQuit.connect(exit)
    # for testing
    # main_app = App()  # Instantiate the application
    # exit(app.exec_())  # Return control to original event loop

    # self-update function, can be used later on
    # timer = QTimer()
    # timer.timeout.connect(main_app.update)
    # timer.start(10000)

    while True:
        flag = False

        login = Login()
        login.show()

        # login.exec_() return True if user successfully signed in
        if login.exec_():
            main_app = App()  # Instantiate the application

            app.exec_()
            # exit(app.exec_())  # Return control to original event loop
        else:
            flag = True

        if flag is True:
            break

