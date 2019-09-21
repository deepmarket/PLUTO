from fbs_runtime.application_context.PyQt5 import ApplicationContext

from ..widgets import (
    Frame, 
    Button, 
    VerticalLayout, 
    VerticalSpacer, 
    HorizontalLayout, 
    HorizontalSpacer,
    Label,
)

from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor

class AppAccountUI(Frame):            

    username: str = ""
    credit: int = 15                    
    credit_history: Button = None          
    notification: Button = None            
    setting_button: Button = None          
    logout: Button = None                  

    title_section: Frame = None
    button_section: Frame = None

    def __init__(self, parent, cxt:ApplicationContext, width: int, height: int, *args, **kwargs):
        super(AppAccountUI, self).__init__(parent, name="account")

        self._init_ui(width, height)

        self.setStyleSheet(cxt.app_style)
    
    def _init_ui(self, width: int, height: int):

        self.setFixedSize(width, height)

        # shadow
        effect = QGraphicsDropShadowEffect()
        effect.setBlurRadius(20)
        effect.setXOffset(0)
        effect.setYOffset(0)
        effect.setColor(QColor("#91A4AD"))

        self.setGraphicsEffect(effect)

        window_layout = VerticalLayout(self)

        self.title_section = Frame(self, name="account_title")
        window_layout.addWidget(self.title_section)
        self._init_title_section()

        self.button_section = Frame(self, name="account_button_frame")
        window_layout.addWidget(self.button_section)
        self._init_button_section()

        spacer = VerticalSpacer()
        window_layout.addItem(spacer)

        self.logout_section = Frame(self)
        window_layout.addWidget(self.logout_section)
        self._init_logout_section()

    def _init_title_section(self):

        section_layout = HorizontalLayout(self.title_section)

        user = Label(
            self.title_section, text="TEST", name="account_username", align=Qt.AlignVCenter
        )
        section_layout.addWidget(user)

        spacer = HorizontalSpacer()
        section_layout.addItem(spacer)

        credit = Label(
            self.title_section, text=f"Credits: {self.credit}", name="account_credit", align=Qt.AlignVCenter
        )
        section_layout.addWidget(credit)

    def _init_button_section(self):

        section_layout = VerticalLayout(self.button_section, space=18)

        self.notification = Button(
            self.button_section, text="Notifications", name="account_button", cursor=True
        )
        section_layout.addWidget(self.notification)

        self.credit_history = Button(
            self.button_section, text="Credit History", name="account_button", cursor=True
        )

        section_layout.addWidget(self.credit_history)

        self.about = Button(
            self.button_section, text="About", name="account_button", cursor=True
        )
        section_layout.addWidget(self.about)

    def _init_logout_section(self):

        section_layout = HorizontalLayout(self.logout_section)

        spacer = HorizontalSpacer()
        section_layout.addItem(spacer)

        self.logout = Button(
            self.logout_section, text="Logout", name="account_logout", cursor=True
        )
        section_layout.addWidget(self.logout)
