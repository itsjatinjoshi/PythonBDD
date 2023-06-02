import time

from selenium.webdriver.common.by import By

from BDDCommon.CommonSteps.webstepscommon import *
from BDDCommon.CommonFunctions.webcommon import *
from BDDCommon.Configs import nav_bars_configs

from behave import *


@then('the "{nav_bars}" should be visible')
def verify_the_nav_bars(context, nav_bars):
    expected_bars = ['Home', 'Saved', 'Fashion', 'Sneakers', 'Motors', 'Electronics',
                     'Sporting Goods', 'Toys & Hobbies ', 'Homes & Garden',
                     'Collectibles & Art', 'eBay Refurbished', 'Business & Industrial']

    # nav_container_name = context.driver.find_element_by_class_name("hl-cat-nav__container")
    # print(nav_container_name)
    # print("DRIVER: ", context.driver.find_element('xpath', '//*[@id="mainContent"]/div[1]/ul/li[1]'))

    if nav_bars not in expected_bars:
        print("Actual Nav Bar is :", nav_bars)
        print("Expected Nav Bar is :", expected_bars)
        raise Exception("Element not available in the List.")
    else:
        locator_attribute = nav_bars_configs.NAV_BAR_CONFIG.get(nav_bars)
        locator_type = locator_attribute['type']
        locator_value = locator_attribute['locator']

        nav_locator = webcommon.find_element(context, locator_type, locator_value)
        webcommon.assert_element_visible(nav_locator)
