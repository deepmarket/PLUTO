from fbs_runtime.application_context.PyQt5 import ApplicationContext

from src.main.python.api import Api
from src.main.python.util import add_greeting

from src.main.python.interfaces.dashboard import DashboardUI


class Dashboard(DashboardUI):

    username: str = ""
    total_balance: int = 0
    # estimated_profit: int = 0
    # estimated_cost: int = 0
    running_machines: int = 0
    dead_machine: int = 0
    finished_jobs = 0
    running_jobs = 0
    killed_jobs = 0

    def __init__(self, cxt: ApplicationContext, *args, **kwargs):
        super(Dashboard, self).__init__(cxt, *args, **kwargs)

        self.cxt = cxt
        self.update_account()

    def update_account(self):

        # fetch account information
        self._api_get_call()

        # fill greeting
        greeting = add_greeting() + ", " + self.username
        self.greeting.setText(greeting)

        # fill total balance credit
        balance_credit = f"{self.total_balance} credits"
        self.balance_credit.setText(balance_credit)

        resources_running = f"{self.running_machines}"
        self.resources_running.set_dat(resources_running)

        resources_dead = f"{self.dead_machine}"
        self.resources_dead.set_dat(resources_dead)

        jobs_running = f"{self.running_jobs}"
        self.jobs_running.set_dat(jobs_running)

        jobs_finish = f"{self.finished_jobs}"
        self.jobs_finish.set_dat(jobs_finish)

        jobs_kill = f"{self.killed_jobs}"
        self.jobs_kill.set_dat(jobs_kill)

    def _api_get_call(self):

        # fetch account information
        with Api(self.cxt, "/account") as account:
            status, res = account.get()

            if not res or status != 200:
                self.username = "."
                self.total_balance = 0
            else:
                # Insert comma here so we can default to nameless greeting if api fails.
                self.username = res["account"]["firstname"].capitalize()
                self.total_balance = round(res["account"]["credits"], 4)

        # fetch resources information
        with Api(self.cxt, "/resources") as resources:
            status, res = resources.get()

            if not res or status != 200:
                self.running_machines = 0
                self.dead_machine = 0
            else:
                for rsrc in res["resources"]:
                    status = str(rsrc["status"]).upper()

                    if status == "ALIVE":
                        self.running_machines += 1
                    else:
                        self.dead_machine += 1

        # fetch job information
        with Api(self.cxt, "/jobs") as jobs:
            status, res = jobs.get()

            if not res or status != 200:
                self.running_jobs = 0
                self.finished_jobs = 0
                self.running_jobs = 0
            else:
                for job in res["jobs"]:
                    status = str(job["status"]).upper()

                    if status == "FINISHED":
                        self.finished_jobs += 1
                    elif status == "RUNNING" or status == "SCHEDULED":
                        self.running_jobs += 1
                    else:
                        self.killed_jobs += 1
