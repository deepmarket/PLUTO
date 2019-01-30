from os import environ
from PyQt5.QtWidgets import QApplication

from mainapp import MainApp

# Removed by sgomena on 1/29/19 after directory structure refactoring
# sys.path.append(path.join(path.dirname(__file__), '..'))


if __name__ == '__main__':
    from sys import exit, argv

    # Enable headless for testing
    if environ.get('HEADLESS'):
        argv += ['-platform', 'minimal']

    app = QApplication(argv)
    # Save reference to main application so it's not garbage collected
    dont_garbage_collect_me = MainApp()
    exit(app.exec_())

