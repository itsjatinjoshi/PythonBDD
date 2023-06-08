import time

from behave import step, then

from BDDCommon.CommonFunctions.webcommon import assert_element_visible, read_text
from BDDCommon.Configs.element_configs import ORDER_DETAILS
from BDDCommon.Configs.order_page_config import ORDER_PAGE_ELEMENT, ORDER_DETAILED_ELEMENT


@step('verify "{correct_details}" page loaded with correct data')
def verify_order_received_message_display(context, correct_details):
    time.sleep(40)
    order_received_msg_type = ORDER_DETAILS['ORDER_RECEIVED_MSG']['type']
    order_received_msg_locator = ORDER_DETAILS['ORDER_RECEIVED_MSG']['locator']
    assert_element_visible(context, order_received_msg_type, order_received_msg_locator)
    expected_text = read_text(context, order_received_msg_type, order_received_msg_locator)
    assert expected_text == correct_details, "Order not found"

    context.execute_steps(
        """
        then verify "Thank you" message displayed
        then verify order number, date, email, total and payment method displayed
        """
    )


@then('verify "{expected_message}" message displayed')
def verify_thank_you_message_displayed(context, expected_message):
    msg_type = ORDER_PAGE_ELEMENT['THANK_YOU_TEXT']['type']
    msg_locator = ORDER_PAGE_ELEMENT['THANK_YOU_TEXT']['locator']
    actual_message = read_text(context, msg_type, msg_locator)
    assert expected_message in actual_message, f"Displayed message is {actual_message}, " \
                                               f"but expected message is {expected_message}."


@then('verify order number, date, email, total and payment method displayed')
def verify_all_billing_info_display(context):
    order_id_type = ORDER_DETAILED_ELEMENT["ID"]['type']
    order_id_locator = ORDER_DETAILED_ELEMENT["ID"]['locator']

    order_date_type = ORDER_DETAILED_ELEMENT["DATE"]['type']
    order_date_locator = ORDER_DETAILED_ELEMENT["DATE"]['locator']

    order_total_type = ORDER_DETAILED_ELEMENT["TOTAL"]['type']
    order_total_locator = ORDER_DETAILED_ELEMENT["TOTAL"]['locator']

    order_payment_method_type = ORDER_DETAILED_ELEMENT["PAYMENT_METHOD"]['type']
    order_payment_method_locator = ORDER_DETAILED_ELEMENT["PAYMENT_METHOD"]['locator']

    order_id = int(read_text(context, order_id_type, order_id_locator))
    assert order_id is not None and order_id >= 0, f"Displayed order ID is :{order_id}"

    order_date = read_text(context, order_date_type, order_date_locator)
    assert order_date is not None, f"Displayed order DATE is :{order_date}"

    order_total = read_text(context, order_total_type, order_total_locator)
    assert order_total is not None, f"Displayed order TOTAL is :{order_total}"

    order_payment_method = read_text(context, order_payment_method_type,
                                     order_payment_method_locator)
    assert order_payment_method is not None, f"Displayed order PAYMENT is :{order_payment_method}"

    context.order_id = order_id
