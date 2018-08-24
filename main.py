import os
import sys
from PyQt5.QtWidgets import QApplication

from src.app import App

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

if __name__ == '__main__':
    from sys import exit, argv
    app = QApplication(argv)

    main_app = App()  # Instantiate the application
    exit(app.exec_())  # Return control to original event loop

