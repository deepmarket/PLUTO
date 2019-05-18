# UI Palette
COLOR_01 = "#6C7E8E"        # standard label, background
COLOR_02 = "#91A4AD"
COLOR_03 = "#F4F8F9"
COLOR_04 = "#657FEB"
COLOR_05 = "#7DCC54"
COLOR_06 = "#FFFFFF"
COLOR_07 = "#D0DBE0"
COLOR_08 = "#C6CDDB"        # disable background
COLOR_09 = "#F2F2F2"        # disable label

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
    
    QPushButton {
        border-radius: 4px;    
    }
    
    #Login {
        border: None;
        background: #F4F8F9;
    }
    
    #Login_login_title {
        font-family: "Helvetica Neue";
        font-size: 35px;
        font-weight: 100;
        color: #6C7E8E;
    }
    
    #Login_create_title {
        font-family: "Helvetica Neue";
        font-size: 26px;
        font-weight: 100;
        color: #6C7E8E;
    }
    
    #Login_prologue {
        font-family: "Helvetica Neue";
        font-size: 13px;
        font-weight: 200;
        color: #6C7E8E;
    }
    
    #Login_input_box {
        border: none;
        background-color: white;
    }
    
    #Login_input_title {
        font-family: "Helvetica Neue";
        font-size: 14px;
        font-weight: 400;
        color: #6C7E8E;
    }
    
    #Login_input_input {
        border: none;
        font-family: "Helvetica Neue";
        font-weight: 300;
        font-size: 14px;
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
        
        font-weight: 200;
        color: white;
    }
    
    #Login_switch_description {
        background-color: white;
        padding-right: 10px;
        font-family: "Helvetica Neue";
        font-size: 14px;
        font-weight:200;
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
        border-radius: 4px;
    }
    
    #App_navigation_credit {
        font-family: "Helvetica Neue";
        font-size: 12px;
        font-weight: 300;
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
        border-radius: 4px;
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
    padding-left: 16px;
    font-family: "Helvetica Neue";
    font-size: 13px;
    font-weight: 400;
    color: {COLOR_02};
    text-align: left;
"""

app_sidebar_button_active = f"""
    {app_sidebar_button}
    border-left: 2px solid {COLOR_01};
"""

dashboard_style = """

    #Dashboard_overview {
        background-color: white;
    }
    
    #Dashboard_greeting {
        font-family: "Helvetica Neue";
        font-size: 32px;
        font-weight: 50;
        color: #6C7E8E;
    }
    
    #Dashboard_username {
        font-family: "Helvetica Neue";
        font-size: 32px;
        font-weight: 100;
        color: #6C7E8E;
    }
    
    #Dashboard_description {
        font-family: "Helvetica Neue";
        font-size: 14px;
        font-weight: 250;
        color: #6C7E8E;
    }
    
    #Dashboard_highlight_description {
        font-family: "Helvetica Neue";
        font-size: 14px;
        font-weight: 500;
        color: #6C7E8E;
    }
    
    #Dashboard_balance_title {
        font-family: "Helvetica Neue";
        font-size: 30px;
        font-weight: 50;
        color: #6C7E8E;
    }
    
    #Dashboard_balance {
        font-family: "Helvetica Neue";
        font-size: 34px;
        font-weight: 100;
        color: #6C7E8E;
    }
    
    #Dashboard_estimated_title {
        font-family: "Helvetica Neue";
        font-size: 16px;
        font-weight: 200;
        color: #6C7E8E;
    }
    
    #Dashboard_estimated_title_small {
        font-family: "Helvetica Neue";
        font-size: 12px;
        font-weight: 200;
        color: #6C7E8E;
    }
    
    #Dashboard_estimated {
        font-family: "Helvetica Neue";
        font-size: 24px;
        font-weight: 300;
        color: #6C7E8E;
    }
    
    #Dashboard_history {
        background-color: white;
    }
    
    #Dashboard_history_title {
        font-family: "Helvetica Neue";
        font-size: 18px;
        font-weight: 200;
        color: #6C7E8E;
    }
    
    #Dashboard_history_table {
        border: none;
        background-color: #F5F5F5;
        alternate-background-color: white;
    }
    
"""

page_style = """

    #Page_sub_page {
        background-color: white;
    }
    
    #Page_machine_config {
        background-color: #D6EFEF;
    }
    
    #Page_resource_planning {
        background-color: #F4F8F9;
    }
    
    #Page_resource_submission {
        background-color: #F4F8F9;
    }
    
    #Page_scheme {
        background-color: #F4F8F9;
    }
    
    #Page_available_resources {
        background-color: #D6EFEF;
    }
    
    #Page_job_submission {
        background-color: #F4F8F9;
    }
    
    #Page_section_title {
        font-family: "Helvetica Neue";
        font-size: 20px;
        font-weight: 100;
        color: #6C7E8E;
    }
    
    #Page_section_title_small {
        font-family: "Helvetica Neue";
        font-size: 16px;
        font-weight: 300;
        color: #6C7E8E;
    }
    
    #Page_hint {
        font-family: "Helvetica Neue";
        font-size: 12px;
        font-weight: 300;
        color: red;
    }
    
    #Page_hint_small {
        font-family: "Helvetica Neue";
        font-size: 11px;
        font-weight: 300;
        color: red;
    }

    #Page_input_frame {
        background-color: white;
    }

    #Page_input_title {
        font-family: "Helvetica Neue";
        font-size: 13px;
        font-weight: 300;
        color: #6C7E8E;
    }
    
    #Page_button {
        border: None;
        background-color: #6C7E8E;
        height: 30px;
        width: 120px;
        font-family: "Helvetica Neue";
        font-size: 12px;
        font-weight: 300;
        border-radius: 4px;
        color: white;
    }

    #Page_available_title {
        font-family: "Helvetica Neue";
        font-size: 12px;
        font-weight: 500;
        color: #6C7E8E;
    }
    
    #Page_available_label {
        font-family: "Helvetica Neue";
        font-size: 11px;
        font-weight: 500;
        color: #6C7E8E;
    }
    
    #Page_table_workspace {
        background-color: white;
    }

    #Page_table_test {
        background-color: yellow;
    }
    
    #Page_table_workspace_search {
        border: None;
        background-color: #F7F7F7;
        padding: 0 20px;
        font-family: "Helvetica Neue";
        font-size: 13px;
        font-weight: 200;
        color: black;
    }
    
    #Page_table_workspace_button {
        border: None;
        background-color: #6C7E8E;
        height: 35px;
        width: 90px;
        font-family: "Helvetica Neue";
        font-size: 13px;
        font-weight: 200;
        border-radius: 4px;
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
"""

page_menu_button_active = f"""
    border: None;
    border-bottom: 2px solid {COLOR_01};
    width: 95px;
    height: 27px;
    font-family: "Helvetica Neue";
    font-size: 12px;
    font-weight: 200;
    color: {COLOR_01};
"""

page_menu_button = """
    border: None;
    width: 95px;
    height: 27px;
    font-family: "Helvetica Neue";
    font-size: 12px;
    font-weight: 100;
    color: #CBCBCB;
"""

Page_input_ip_input = """
    border: None;
    background-color: #F7F7F7;
    padding: 0 1px;
    font-family: "Helvetica Neue";
    font-size: 12px;
    font-weight: 200;
    color: black;
"""

Page_input_ip_input_disable = f"""
    border: None;
    background-color: {COLOR_08};
    padding: 0 1px;
    font-family: "Helvetica Neue";
    font-size: 12px;
    font-weight: 200;
    color: {COLOR_09};
"""


Page_machine_config_box = """
    background-color: white;
"""

Page_machine_config_box_disable = f"""
    background-color: {COLOR_08};
"""

Page_machine_config_label = f"""
    font-family: "Helvetica Neue";
    font-size: 12px;
    font-weight: 200;
    color: {COLOR_01};
"""

Page_machine_config_label_red = f"""
    font-family: "Helvetica Neue";
    font-size: 12px;
    font-weight: 500;
    color: red;
"""

Page_machine_config_label_green = f"""
    font-family: "Helvetica Neue";
    font-size: 12px;
    font-weight: 400;
    color: #95E637;
"""

Page_machine_config_label_disable = f"""
    font-family: "Helvetica Neue";
    font-size: 12px;
    font-weight: 400;
    color: #F2F2F2;
"""

Page_input_input = f"""
    border: None;
    background-color: white;
    padding: 0 1px;
    font-family: "Helvetica Neue";
    font-size: 12px;
    font-weight: 200;
    color: black;
"""

Page_input_input_disable = f"""
    border: None;
    background-color: {COLOR_08};
    padding: 0 1px;
    font-family: "Helvetica Neue";
    font-size: 12px;
    font-weight: 200;
    color: {COLOR_09};
"""

Page_evaluate_button = f"""
    border: None;
    background-color: {COLOR_01};
    height: 30px;
    width: 120px;
    font-family: "Helvetica Neue";
    font-size: 12px;
    font-weight: 300;
    border-radius: 4px;
    color: white;   
"""

Page_evaluate_button_disable = f"""
    border: None;
    background-color: {COLOR_08};
    height: 30px;
    width: 120px;
    font-family: "Helvetica Neue";
    font-size: 12px;
    font-weight: 300;
    border-radius: 4px;
    color: {COLOR_09};
"""

Page_submission_button = f"""
    border: none;
    background-color: white;
    padding-bottom: 3px;
    height: 20px;
    width: 23px;
    font-size: 20px;
    border-radius: 4px;
    color: {COLOR_01};
"""

Page_submission_button_disable = f"""
    border: none;
    background-color: {COLOR_08};
    padding-bottom: 3px;
    height: 20px;
    width: 23px;
    font-size: 20px;
    border-radius: 4px;
    color: {COLOR_09};
"""

Page_submission_box = f"""
    background-color: white;
"""

Page_submission_box_disable = f"""
    background-color: {COLOR_08};
"""

Page_submission_label = f"""
    font-family: "Helvetica Neue";
    font-size: 13px;
    font-weight: 300;
    color: {COLOR_01};
"""

Page_submission_label_disable = f"""
    font-family: "Helvetica Neue";
    font-size: 13px;
    font-weight: 300;
    color: {COLOR_09};
"""

Page_submission_submit = f"""
    border: None;
    background-color: {COLOR_01};
    height: 30px;
    width: 90px;
    font-family: "Helvetica Neue";
    font-size: 12px;
    font-weight: 300;
    border-radius: 4px;
    color: white;
"""

Page_submission_submit_disable = f"""
    border: None;
    background-color: {COLOR_08};
    height: 30px;
    width: 90px;
    font-family: "Helvetica Neue";
    font-size: 12px;
    font-weight: 300;
    border-radius: 4px;
    color: {COLOR_09};
"""

Page_scheme_box = f"""
    background-color: #82B9B9;
"""

Page_scheme_box_disable = f"""
    border-radius: 4px;
    background-color: {COLOR_03};
"""

Page_scheme_button_frame = f"""
    border-color: {COLOR_01};
    border-width: 1px;        
    border-style: solid;
    border-radius: 4px;
    background-color: white;
"""

Page_scheme_label = f"""
    font-family: "Helvetica Neue";
    font-size: 11px;
    font-weight: 400;
    border-radius: 4px;
    color: white;
"""

Page_scheme_label_disable = f"""
    font-family: "Helvetica Neue";
    font-size: 11px;
    font-weight: 400;
    color: {COLOR_01};
"""

question_style = """

    #Question_window {
        border: none;
        background-color: #F4F8F9;
    }

    #Question_question {
        font-family: "Helvetica Neue";
        font-size: 12px;
        font-weight: 400;
        color: #6C7E8E;
    }
    
    #Question_button_confirm {
        border: none;
        background-color: #0069D9;
        height: 22px;
        width: 65px;
        font-family: "Helvetica Neue";
        font-size: 10px;
        font-weight: 500;
        border-radius: 4px;
        color: white;
    }
    
    #Question_button_cancel {
        border: none;
        background-color: #B9CCDD;
        height: 22px;
        width: 65px;
        font-family: "Helvetica Neue";
        font-size: 10px;
        font-weight: 500;
        border-radius: 4px;
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
    border-radius: 4px;
    color: {COLOR_01};
"""

Credit_section_button = f"""
    border: None;
    width: 90px;
    height: 33px;
    font-family: "Helvetica Neue";
    font-size: 11px;
    font-weight: 100;
    border-radius: 4px;
    color: {COLOR_07};
"""