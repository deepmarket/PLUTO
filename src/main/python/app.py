from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtCore import pyqtSignal

from api import Api

from dashboard import Dashboard
from resources import Resources
from jobs import Jobs
from settings import Settings

from interfaces.app import AppUI
from interfaces.widgets import Notification, CreditHistory


class App(AppUI):
    def __init__(
        self, logout_signal: pyqtSignal, cxt: ApplicationContext, *args, **kwargs
    ):
        super(App, self).__init__(cxt, *args, **kwargs)

        self.username = ""
        self.total_balance = 0

        self.logout_signal = logout_signal

        self.update_account()
        self.on_dashboard_clicked()

    def update_account(self):
        # fetch account information
        self._api_get_call()

        # update navigation credit value
        self.navigation.set_credit(self.total_balance)

        # update account username and credit value
        self.account.update_info(self.username, self.total_balance)

    def on_dashboard_clicked(self):
        self.sidebar.on_dashboard_clicked()
        self._sidebar_widget_updated(Dashboard)

    def on_resources_clicked(self):
        self.sidebar.on_resources_clicked()
        self._sidebar_widget_updated(Resources)

    def on_jobs_clicked(self):
        self.sidebar.on_jobs_clicked()
        self._sidebar_widget_updated(Jobs)

    def on_settings_clicked(self):
        self.sidebar.on_settings_clicked()
        self._sidebar_widget_updated(Settings)

    def on_notification_clicked(self):
        popup = Notification(self.cxt)
        popup.exec_()

    # credit history popup
    def on_credit_history_clicked(self):
        popup = CreditHistory(self.cxt)
        popup.exec_()

    def on_about_clicked(self):
        pass

    def on_logout_clicked(self):

        with Api("/auth/logout") as account_api:
            status, res = account_api.post()

            if status == 200:
                self.close()
                self.logout_signal.emit()

    def _sidebar_widget_updated(self, widget=None):
        """
        This is a helper function that is called *manually* by the `clicked` callback function
        attached to each of the sidebar widgets.

        Its purpose is to reset each sidebar widgets style to default and manage the
        widget stack

        :param widget: The clicked on widget that we want to instantiate
        :return: None
        """

        # Deallocate current widget if it exists
        if self.main_window.stack.count():
            self.main_window.stack.currentWidget().setParent(None)

        if widget is not None:
            self.main_window.stack_widget = widget(self.cxt)
            self.main_window.stack.addWidget(self.main_window.stack_widget)
        else:
            # Default to dashboard I guess?
            self.main_window.stack_widget = Dashboard(self.cxt)
            self.main_window.stack.addWidget(self.main_window.stack_widget)

        # notification popup

    def _api_get_call(self):

        # fetch account information
        with Api("/account") as account:
            status, res = account.get()

            if not res or status != 200:
                self.username = "."
                self.total_balance = 0
            else:
                # Insert comma here so we can default to nameless greeting if api fails.
                self.username = res["account"]["firstname"].capitalize()
                self.total_balance = round(res["account"]["credits"], 4)
