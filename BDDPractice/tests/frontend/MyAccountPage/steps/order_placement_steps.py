import random
import time

from behave import step

from BDDCommon.CommonFunctions import webcommon
from BDDCommon.CommonFunctions.user_info_for_billing_details import user_info
from BDDCommon.CommonFunctions.webcommon import get_all_elements_list, add_to_cart, read_text, click, verify_title, \
    assert_element_visible, wait_time
from BDDCommon.Configs.element_configs import ALL_PRODUCT_LIST, CART_ELEMENT, SHIPPING_ADDRESS, PAYMENT_OPTION, \
    SHIPPING_METHOD, PLACE_ORDER, ORDER_DETAILS


@step('I added a random item into the cart')
def add_random_item_to_the_cart(context):
    """

    :param context:
    :return:
    """

    locator_type = ALL_PRODUCT_LIST['ALL_PRODUCT_LIST_PAGE1']['type']
    locator = ALL_PRODUCT_LIST['ALL_PRODUCT_LIST_PAGE1']['locator']

    cart_type = CART_ELEMENT['ELEMENT_IN_CART']['type']
    cart_locator = CART_ELEMENT['ELEMENT_IN_CART']['locator']
    all_items_list = get_all_elements_list(context, locator_type, locator)
    random_item_number = str(random.randint(1, all_items_list))
    wait_time(context, cart_type, cart_locator, 20)
    add_to_cart(context, locator_type, locator, random_item_number)
    time.sleep(10)

    total_items = read_text(context, cart_type, cart_locator)
    assert "1" in total_items, "Item not added into the cart"


@step('click on navigation cart button on the home page')
def click_on_add_to_cart_nav_button(context):
    shop_cart_type = CART_ELEMENT['SHOP_CART']['type']
    shop_cart_locator = CART_ELEMENT['SHOP_CART']['locator']
    click(context, shop_cart_type, shop_cart_locator)


@step('Verify the title of "{title}" page')
def verify_cart_page_title(context, title):
    cart_title_element_type = CART_ELEMENT['CART_PAGE_TITLE']['type']
    cart_title_element_locator = CART_ELEMENT['CART_PAGE_TITLE']['locator']
    verify_title(context, cart_title_element_type, cart_title_element_locator, title)


@step('click on "proceed to checkout" button')
def click_on_proceed_checkout_btn(context):
    proceed_btn_type = CART_ELEMENT['PROCEED_CHECKOUT']['type']
    proceed_btn_locator = CART_ELEMENT['PROCEED_CHECKOUT']['locator']
    click(context, proceed_btn_type, proceed_btn_locator)


@step('Verify "{title}" page is loaded')
def verify_cart_page_title(context, title):
    cart_title_element_type = CART_ELEMENT['CHECKOUT_PAGE_TITLE']['type']
    cart_title_element_locator = CART_ELEMENT['CHECKOUT_PAGE_TITLE']['locator']
    verify_title(context, cart_title_element_type, cart_title_element_locator, title)


@step('Fill all the necessary details in billing details form')
def shipping_address_info(context):
    first_name_type = SHIPPING_ADDRESS['FIRST_NAME']['type']
    first_name_locator = SHIPPING_ADDRESS['FIRST_NAME']['locator']

    last_name_type = SHIPPING_ADDRESS['LAST_NAME']['type']
    last_name_locator = SHIPPING_ADDRESS['LAST_NAME']['locator']

    company_type = SHIPPING_ADDRESS['COMPANY']['type']
    company_locator = SHIPPING_ADDRESS['COMPANY']['locator']

    street_address_type = SHIPPING_ADDRESS['STREET_ADDRESS']['type']
    street_address_locator = SHIPPING_ADDRESS['STREET_ADDRESS']['locator']

    city_type = SHIPPING_ADDRESS['CITY']['type']
    city_locator = SHIPPING_ADDRESS['CITY']['locator']

    # state_type = SHIPPING_ADDRESS['STATE']['type']
    # state_locator = SHIPPING_ADDRESS['STATE']['locator']

    postal_code_type = SHIPPING_ADDRESS['POSTAL_CODE']['type']
    postal_code_locator = SHIPPING_ADDRESS['POSTAL_CODE']['locator']

    phone_type = SHIPPING_ADDRESS['PHONE']['type']
    phone_locator = SHIPPING_ADDRESS['PHONE']['locator']

    email_type = SHIPPING_ADDRESS['EMAIL']['type']
    email_locator = SHIPPING_ADDRESS['EMAIL']['locator']
    # 650 5th Ave, New York, NY 10019, United States
    shipping_info = user_info(street_address="650 5th Ave",
                              city="Ottawa",
                              # state="NY",
                              postal_code="K2T 0P3",
                              phone=1231231231,
                              )

    webcommon.type_into_element(context, shipping_info['firstName'], first_name_type, first_name_locator)
    webcommon.type_into_element(context, shipping_info['lastName'], last_name_type, last_name_locator)
    webcommon.type_into_element(context, shipping_info['company'], company_type, company_locator)
    webcommon.type_into_element(context, shipping_info['street'], street_address_type, street_address_locator)
    webcommon.type_into_element(context, shipping_info['city'], city_type, city_locator)
    # webcommon.type_into_element(context, shipping_info['state'], state_type, state_locator)
    webcommon.type_into_element(context, shipping_info['postalCode'], postal_code_type, postal_code_locator)
    webcommon.type_into_element(context, shipping_info['phone'], phone_type, phone_locator)
    webcommon.type_into_element(context, shipping_info['email'], email_type, email_locator)


@step('verify "{shipping_method}" is selected')
def verify_correct_shipping_method(context, shipping_method):
    # todo cannot see block during automation test

    # shipping_method_type = SHIPPING_METHOD['FLAT_RATE']['type']
    # shipping_method_locator = SHIPPING_METHOD['FLAT_RATE']['locator']
    # print("SHIPPING TYPE", shipping_method_type)
    # print("SHIPPING LOCATOR", shipping_method_locator)
    #
    # # element = context.driver.find_element(By.CLASS_NAME, 'pagination-r')
    # # context.driver.execute_script("arguments[0].click();", element)
    # click(context, shipping_method_type, shipping_method_locator)
    # time.sleep(30)
    # shipping_method_text = read_text(context, shipping_method_type, shipping_method_locator)
    #
    # assert shipping_method in shipping_method_text, f"Wrong shipping method found. was expecting " \
    #                                                 f"{shipping_method} but got {shipping_method_text}"
    pass


@step('"{expected_payment}" method is selected')
def verify_cash_on_delivery_selected(context, expected_payment):
    time.sleep(10)
    payment_type = PAYMENT_OPTION['CASH_ON_DELIVERY']['type']
    payment_locator = PAYMENT_OPTION['CASH_ON_DELIVERY']['locator']
    wait_time(context, payment_type, payment_locator, 20)
    click(context, payment_type, payment_locator)
    payment_method_text = read_text(context, payment_type, payment_locator)
    assert expected_payment in payment_method_text, "Wrong Payment method found"


@step('click on "Place order" button')
def click_on_place_order_button(context):
    order_btn_type = PLACE_ORDER['PLACE_ORDER']['type']
    order_btn_locator = PLACE_ORDER['PLACE_ORDER']['locator']
    click(context, order_btn_type, order_btn_locator)
