import time

from BDDCommon.CommonSteps import webstepscommon
from BDDCommon.CommonFunctions import webcommon
from behave import step
from BDDCommon.Configs.nav_bars_configs import MY_ACCOUNT_LOCATORS


@step('I type "{email}" to the username of login form')
def send_login_email(context, email):
    """

    :param context:
    :param email:
    :return:
    """

    email_locator_type = MY_ACCOUNT_LOCATORS['LOGIN_FIELD']['type']
    email_locator_text = MY_ACCOUNT_LOCATORS['LOGIN_FIELD']['locator']
    webcommon.type_into_element(context, email, email_locator_type, email_locator_text)



@step('I type "{password}" to the login form')
def send_login_password(context, password):
    """
    :param context:
    :param password:
    :return:
    """
    pswd_locator_type = MY_ACCOUNT_LOCATORS['PSWD_FIELD']['type']
    pswd_locator_text = MY_ACCOUNT_LOCATORS['PSWD_FIELD']['locator']
    webcommon.type_into_element(context, password, pswd_locator_type, pswd_locator_text)


@step('I click on "{button_name}" button')
def click_login_button(context, button_name):
    login_btn_locator_type = MY_ACCOUNT_LOCATORS['LOGIN_BTN']['type']
    login_btn_locator_text = MY_ACCOUNT_LOCATORS['LOGIN_BTN']['locator']
    webcommon.type_into_element(context, button_name, login_btn_locator_type, login_btn_locator_text)
    webcommon.click(context, login_btn_locator_type, login_btn_locator_text)
    # print("STATUS CODE : ", context.driver.status_code)
    # assert context.driver.status_code == 200


@step('user should be logged in')
def verify_user_login(context):
    left_nav_bar_type = MY_ACCOUNT_LOCATORS['LEFT_NAV']['type']
    left_nav_bar_locator = MY_ACCOUNT_LOCATORS['LEFT_NAV']['locator']

    logout_link_type = MY_ACCOUNT_LOCATORS['LOGOUT_LINK']['type']
    logout_link_type_locator = MY_ACCOUNT_LOCATORS['LOGOUT_LINK']['locator']

    webcommon.assert_element_visible(context, left_nav_bar_type, left_nav_bar_locator)
    webcommon.assert_element_visible(context, logout_link_type, logout_link_type_locator)


@step('user should get an error message for related to entered email "{email}"')
def enter_wrong_login_password(context, email):
    expected_msg = f"Error: The password you entered for the email " \
                   f"address {email} is incorrect. Lost your password?"

    wrong_password_msg_output_type = MY_ACCOUNT_LOCATORS['WRONG_PSWD']['type']
    wrong_password_msg_output_locator = MY_ACCOUNT_LOCATORS['WRONG_PSWD']['locator']

    actual_msg = webcommon.read_text(context, wrong_password_msg_output_type, wrong_password_msg_output_locator)
    assert actual_msg == expected_msg, "wrong error msg"


@step('user should get an error message unknown email address')
def enter_wrong_email_address(context):
    expected_msg = f"Unknown email address. Check again or try your username."

    wrong_email_msg_output_type = MY_ACCOUNT_LOCATORS['WRONG_EMAIL']['type']
    wrong_email_msg_output_locator = MY_ACCOUNT_LOCATORS['WRONG_EMAIL']['locator']

    actual_msg = webcommon.read_text(context, wrong_email_msg_output_type, wrong_email_msg_output_locator)
    print("ACTUAL MSG : ", actual_msg)
    assert actual_msg == expected_msg, "wrong email msg output"
