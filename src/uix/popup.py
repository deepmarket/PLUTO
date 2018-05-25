# popup widget

from src.uix.util import *


class Question(QMessageBox):

    def __init__(self, question, *args, **kwargs):
        super(QMessageBox, self).__init__(*args, **kwargs)

        self.question = question

        self._init_geometry()
        self._init_ui()
        self.setStyleSheet(question_style)

    def _init_geometry(self):
        pass

    def _init_ui(self):
        pass

    def ask(self, widget, confirmation="Confirm"):
        confirm = self.question(widget, confirmation, self.question,
                                QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        return confirm == QMessageBox.Yes


# # Dynamic methods for tables in resources.py and jobs.py
# def confirm(self, message_dialog: str, confirmation_message: str = "Confirm"):
#     confirm: bool = QMessageBox.question(self, confirmation_message, message_dialog,
#                                          QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
#     return confirm == QMessageBox.Yes
#
#
# def remove_row(self, idx):
#     confirm_removal: bool = self.confirm("Are you sure you want to remove this?")
#
#     if confirm_removal:
#         print(f"Removing row {idx + 1}")
#         self.tableWidget.removeRow(idx)
#     else:
#         pass