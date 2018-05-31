# UI Palette
COLOR_01 = "#6C7E8E"
COLOR_02 = "#91A4AD"
COLOR_03 = "#F4F8F9"
COLOR_04 = "#657FEB"
COLOR_05 = "#7DCC54"
COLOR_06 = "#FFFFFF"
COLOR_07 = "#D0DBE0"

# System Environment variable
QT_AUTO_SCREEN_SCALE_FACTOR = 1
QT_SCALE_FACTOR = 2

# Align standard
VERTICAL = "VERTICAL"
HORIZONTAL = "HORIZONTAL"
STACK = "STACK"

# Direction
LEFT = "LEFT"
RIGHT = "RIGHT"
CENTER = "CENTER"

# Image type
PNG = ".png"
JPG = ".jpg"
JPEG = ".jpeg"
SVG = ".svg"

# Type
LABEL = "QLabel"
QLINEEDIT = "QLineEdit"
QPUSHBUTTON = "QPushButton"

# Plot type
ELLIPSE = "QGraphicsEllipseItem"
LINE = "QGraphicsLineItem"
POLYGON = "QGraphicsPolygonItem"
TEXT = "QGraphicsTextItem"


login_style = """

    #Login {
        border: None;
        background: #F4F8F9;
    }
    
    #Login_login_title {
        background-color: white;
        font-family: "Helvetica Neue";
        font-size: 32px;
        font-weight: 50;
        color: #6C7E8E;
    }
    
    #Login_create_title {
        font-family: "Helvetica Neue";
        font-size: 25px;
        font-weight: 50;
        color: #6C7E8E;
    }
    
    #Login_prologue {
        font-family: "Helvetica Neue";
        font-size: 12px;
        font-weight: 50;
        color: #6C7E8E;
    }
    
    #Login_input_box {
        border: none;
        background-color: white;
    }
    
    #Login_input_title_01 {
        font-family: "Helvetica Neue";
        font-size: 15px;
        font-weight: 100;
        color: #6C7E8E;
    }
    
    #Login_input_input_01 {
        border: none;
        font-family: "Helvetica Neue";
        font-weight: 200;
        font-size: 14px;
    }
    
    #Login_input_title_02 {
        font-family: "Helvetica Neue";
        font-size: 13px;
        font-weight: 100;
        color: #6C7E8E;
    }
    
    #Login_input_input_02 {
        border: none;
        font-family: "Helvetica Neue";
        font-weight: 200;
        font-size: 12px;
    }
    
    #Login_hint {
        padding-left: 15px;
        font-family: "Helvetica Neue";
        font-size: 13px;
        font-weight: 200;
        color: #FF4500;
    }
    
    #Login_large_button {
        border: none;
        background-color: #6C7E8E;
        height: 48px;
        font-family: "Helvetica Neue";
        font-size: 16px;
        font-weight: 100;
        color: white;
    }
    
    #Login_switch_description {
        background-color: white;
        padding-right: 10px;
        font-family: "Helvetica Neue";
        font-size: 14px;
        font-weight:100;
        color: #6C7E8E;
    }
    
    #Login_switch_button {
        border: None;
        background-color: white;
        padding-left: 10px;
        height: 63px;
        text-align: left;
        font-family: "Helvetica Neue";
        font-size: 14px;
        font-weight: 200;
        color: #2F0FFF;
    }

"""

app_style = """

    #App_sidebar {
        background-color: #FEFEFE;
        border-right: 1px solid #E7EEF0;
    }
    
    #App_navigation {
        background-color: white;
    }
    
    #App_main_window {
        background-color: #F4F8F9;
    }
    
    #App_mask {
        background-color: rgba(255, 255, 255, 150);
    }
    
    #App_sidebar_title {
        font-family: "Helvetica Neue";
        font-size: 22px;
        font-weight: 500;
        color: #505A5F;
    }

    #App_navigation_button {
        border: None;
    }
    
    #App_navigation_credit {
        font-family: "Helvetica Neue";
        font-size: 11px;
        font-weight: 100;
        color: #505A5F;
    }
    
    #App_mask_clicked_area {
        border: none;
    }
    
    #App_account {
        background-color: white;
    }

    #App_title_frame {
        border: none;
        border-bottom: 1px solid #D5D5D5;
    }

    #App_account_username {
        font-family: "Helvetica Neue";
        font-size: 12px;
        font-weight: 500;
        color: #6C7E8E;
    }
    
    #App_account_credit {
        font-family: "Helvetica Neue";
        font-size: 11px;
        font-weight: 100;
        color: #505A5F;
    }
    
    #App_account_button {
        border: none;
        font-family: "Helvetica Neue";
        font-size: 10px;
        font-weight: 200;
        color: #6C7E8E;
        text-align: left;
    }
    
    #App_account_logout {
        border: none;
        border-radius: 3px;
        background-color: #6C7E8E;
        height: 25px;
        width: 85px;
        font-family: "Helvetica Neue";
        font-size: 11px;
        font-weight: 200;
        color: white;
    }

"""

app_sidebar_button = f"""
    border: None;
    height: 20px;
    padding-left: 15px;
    font-family: "Helvetica Neue";
    font-size: 13px;
    font-weight: 300;
    color: {COLOR_02};
    text-align: left;
"""

app_sidebar_button_active = f"""
    border: None;
    border-left: 2px solid {COLOR_01};
    height: 20px;
    padding-left: 15px;
    font-family: "Helvetica Neue";
    font-size: 13px;
    font-weight: 300;
    color: {COLOR_01};
    text-align: left;
"""

dashboard_style = """

    #Dashboard_overview {
        background-color: white;
    }
    
    #Dashboard_performance {
        background-color: white;
    }
    
    #Dashboard_resources_spec {
        background-color: white;
    }

    #Dashboard_greeting {
        font-family: "Helvetica Neue";
        font-size: 26px;
        font-weight: 50;
        color: #505A5F;
    }

    #Dashboard_username {
        font-family: "Helvetica Neue";
        font-size: 22px;
        font-weight: 100;
        color: #505A5F;
    }

    #Dashboard_add_dashlet {
        border: none;
        border-radius: 4px;
        height: 26px;
        width: 125px;
        background-color: #6C7E8E;
        font-family: "Helvetica Neue";
        font-size: 13px;
        font-weight: 100;
        color: white;
    }
    
    #Dashboard_section_title {
        font-family: "Helvetica Neue";
        font-size: 16px;
        font-weight: 100;
        color: #505A5F;
    }
    
    #Dashboard_section_switch {
    
    }
    
    #Dashboard_section_context {
        font-family: "Helvetica Neue";
        font-size: 10px;
        font-weight: 100;
        color: #505A5F;
    }
    
    #Dashboard_view {
        border: none;
        background: transparent;
    }
"""

page_style = """

    #Page_input_frame {
        background-color: white;
    }

    #Page_input_title_01 {
        font-family: "Helvetica Neue";
        font-size: 13px;
        font-weight: 300;
        color: #6C7E8E;
    }
    
    #Page_input_title_02 {
        font-family: "Helvetica Neue";
        font-size: 10px;
        font-weight: 200;
        color: #6C7E8E;
    }
    
    #Page_input_input_01 {
        border: None;
        background-color: #F7F7F7;
        padding: 0 1px;
        font-family: "Helvetica Neue";
        font-size: 12px;
        font-weight: 200;
        color: black;
    }
    
    #Page_input_input_02 {
        border: None;
        background-color: #F7F7F7;
        padding: 0 1px;
        font-family: "Helvetica Neue";
        font-size: 10px;
        font-weight: 200;
        color: black;
    }
    
    #Page_hint {
        font-family: "Helvetica Neue";
        font-size: 9px;
        font-weight: 300;
        color: red;
    }
    
    #Page_button_small {
        border: None;
        border-radius: 3px;
        background-color: #6C7E8E;
        height: 20px;
        width: 90px;
        font-family: "Helvetica Neue";
        font-size: 8px;
        font-weight: 500;
        color: white;
    }
    
    #Page_table {
        border: none;
        background-color: white;
        alternate-background-color: #FAFAFA;
    }
    
    #Page_table QHeaderView::section {
        border: none;
        background-color: #6C7E8E;
        height: 35px;
        font-family: "Helvetica Neue";
        font-size:13px;
        font-weight: 100;
        color: white;
    }
    
    #Page_machine_spec {
        border: none;
        border-radius: 3px;
        background-color: #F4F8F9;
    }
    
    #Page_machine_spec_title {
        font-family: "Helvetica Neue";
        font-size:10px;
        font-weight: 300;
        color: #6C7E8E;
    }
"""

page_menu_button_active = f"""
    border: None;
    border-bottom: 2px solid {COLOR_01};
    width: 90px;
    height: 33px;
    font-family: "Helvetica Neue";
    font-size: 11px;
    font-weight: 100;
    color: {COLOR_01};
"""

Page_machine_spec_label = f"""
    font-family: "Helvetica Neue";
    font-size: 8px;
    font-weight: 200;
    color: {COLOR_01};
"""

Page_machine_spec_label_red = f"""
    font-family: "Helvetica Neue";
    font-size: 8px;
    font-weight: 500;
    color: red;
"""

Page_machine_spec_label_green = f"""
    font-family: "Helvetica Neue";
    font-size: 8px;
    font-weight: 400;
    color: #95E637;
"""

question_style = """

    #Question_window {
        border: none;
        background-color: #F4F8F9;
    }

    #Question_question {
        font-family: "Helvetica Neue";
        font-size: 14px;
        font-weight: 100;
        color: #6C7E8E;
    }
    
    #Question_button_confirm {
        border: none;
        border-radius: 3px;
        background-color: #0069D9;
        height: 25px;
        width: 90px;
        font-family: "Helvetica Neue";
        font-size: 9px;
        font-weight: 400;
        color: white;
    }
    
    #Question_button_cancel {
        border: none;
        border-radius: 3px;
        background-color: #B9CCDD;
        height: 25px;
        width: 90px;
        font-family: "Helvetica Neue";
        font-size: 9px;
        font-weight: 400;
        color: white;
    }

"""

notification_style = """

    #Notification {
        border: none;
        background-color: #F4F8F9;
    }
    
    #Notification_title_frame {
        background-color: white;
    }
    
    #Notification_title {
        font-family: "Helvetica Neue";
        font-size: 17px;
        font-weight: 100;
        color: #6C7E8E;
    }
    
    #Notification_button {
        border: none;
        background-color: #6C7E8E;
        height: 27px;
        width: 180px;
        font-family: "Helvetica Neue";
        font-size: 9px;
        font-weight: 200;
        color: white;
    }
    
    #Notification_window {
        border: none;
        background-color: white;
    }

"""

credit_style = """

    #Credit {
        border: none;
        background-color: #F4F8F9;
    }
    
    #Credit_title_frame {
        background-color: white;
    }

    #Credit_title {
        font-family: "Helvetica Neue";
        font-size: 17px;
        font-weight: 100;
        color: #6C7E8E;
    }
    
    #Credit_button {
        border: none;
        border-radius: 3px;
        background-color: #6C7E8E;
        height: 27px;
        width: 150px;
        font-family: "Helvetica Neue";
        font-size: 9px;
        font-weight: 200;
        color: white;
    }
    
    #Credit_window {
        border: none;
        background-color: white;
    }

"""

Credit_section_button_active = f"""
    border: None;
    border-bottom: 2px solid {COLOR_01};
    width: 90px;
    height: 33px;
    font-family: "Helvetica Neue";
    font-size: 11px;
    font-weight: 100;
    color: {COLOR_01};
"""

Credit_section_button = f"""
    border: None;
    width: 90px;
    height: 33px;
    font-family: "Helvetica Neue";
    font-size: 11px;
    font-weight: 100;
    color: {COLOR_07};
"""