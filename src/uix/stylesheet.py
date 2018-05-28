# UI Palette
COLOR_01 = "#6C7E8E"
COLOR_02 = "#91A4AD"
COLOR_03 = "#F4F8F9"
COLOR_04 = "#657FEB"
COLOR_05 = "#7DCC54"
COLOR_06 = "#FFFFFF"

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
        background: white;
    }
    
    #Login_title {
        font-family: "Open Sans";
        font-size: 14px;
        font-weight: 500;
        color: #7bcafa;
    }
    
    #Login_prologue {
        font-family: "Open Sans";
        font-size: 9px;
        font-weight: 300;
        color: #7f7f7f;
    }
    
    #Login_input_title {
        font-family: "Open Sans";
        font-size: 10px;
        font-weight: 500;
        color: #616161;
    }
    
    #Login_input_input {
        border: none;
        border-bottom: 1px solid #616161;
        font-family: "Open Sans";
        font-weight: 200;
        font-size: 10px;
    }
    
    #Login_big_button {
        border: none;
        border-radius: 3px;
        background-color: #7BCAFA;
        height: 30px;
        font-family: "Open Sans";
        font-size: 11px;
        font-weight: 500;
        color: white;
    }
    
    #Login_hint {
        font-family: "Open Sans";
        font-size: 9px;
        font-weight: 400;
        color: #ff2020;
    }
    
    #Login_check_box_check::indicator {
        width: 10px;
        height: 10px;
    }
    
    #Login_check_box_check::indicator:checked {
        border-image: url(./src/img/checked.png);
    }
    
    #Login_check_box_check::indicator:unchecked {   
        border-image: url(./src/img/unchecked.png);     
    }         
                                        
    #Login_check_box_title_label {
        font-family: "Open Sans";
        font-size: 10px;
        font-weight: 400;
        color: #616161;
    }
    
    #Login_check_box_title_button {
        border: none;
        font-family: "Open Sans";
        font-size: 10px;
        font-weight: 400;
        color: #0030ff;
    }
    
    #Login_forget_pwd {
        border: none;
        text-align: right;
        font-family: "Open Sans";
        font-size: 10px;
        font-weight: 400;
        color: #4c6eff;
    }
    
    #Login_switch_section {
        border: none;
    }
    
    #Login_switch_description {
        font-family: "Open Sans";
        font-weight:300;
        font-size: 10px;
        color: #7f7f7f;
    }
    
    #Login_switch_button {
        border: None;
        text-align: left;
        font-family: "Open Sans";
        font-size: 10px;
        font-weight: 400;
        color: #0030ff;
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

    #Page_input_title {
        font-family: "Helvetica Neue";
        font-size: 13px;
        font-weight: 300;
        color: #6C7E8E;
    }
    
    #Page_input_input {
        border: None;
        background-color: #F7F7F7;
        padding: 0 1px;
        font-family: "Helvetica Neue";
        font-size: 12px;
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
    
    #Page_table_button {
        border: None;
        font-family: "Helvetica Neue";
        font-size:12px;
        font-weight: 100;
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

question_style = """



"""