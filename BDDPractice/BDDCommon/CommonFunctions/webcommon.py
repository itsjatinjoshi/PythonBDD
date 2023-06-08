import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from BDDCommon.Configs import configs


def go_to(context, location, **kwargs):
    """
    :param context:
    :param location:
    :return:
    """

    if not location.startswith('http'):
        if location == "home".lower():
            _url = ""
        else:
            _url = configs.URL_CONFIG.get(location)
        base_url = configs.URL_CONFIG.get('base_url')
        url = base_url + _url

    browser = context.config.userdata.get('browser')

    if not browser:
        browser = 'chrome'

    if browser.lower() == 'chrome':
        context.driver = webdriver.Chrome(ChromeDriverManager().install())

    elif browser.lower() == 'headlesschrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        context.driver = webdriver.Chrome(options=options)

    elif browser.lower() in ("ff", "firefox"):
        context.driver = webdriver.Firefox()

    else:
        raise Exception(f"The Browser type {browser} is not supported")

    wait = int(kwargs['implicitly_wait']) if 'implicitly_wait' in kwargs.keys() else 15
    context.driver.implicitly_wait(wait)

    context.driver.maximize_window()
    url = url.strip()
    context.driver.get(url)

    return context.driver


# ====================================================================
def assert_page_title(context, expected_page_title):
    """
    Function to check if title is same as expected
    :param context:
    :param expected_page_title:
    :return:
    """
    # import pdb;
    # pdb.set_trace()
    actual_title = context.driver.title
    assert actual_title == expected_page_title, "Title is not the same as expected."


# ====================================================================
def assert_current_url(context, expected_current_url):
    """
    Function to check if title is same as expected
    :param context:
    :param expected_current_url:
    :return:
    """

    actual_current_url = context.driver.current_url

    if not expected_current_url.startswith("http") or not expected_current_url.startswith("https"):
        expected_current_url = "https://" + expected_current_url + "/"
    assert expected_current_url == actual_current_url, "URL is not the same as expected."


# ====================================================================
def element_isVisible(element):
    if element.is_displayed():
        return True
    else:
        return False


# ===========================================================================

def find_element(context, locator_attribute, locator_value):
    possible_attributes = ["id", "xpath", "link text", "partial link text",
                           "name", "tag name", "class name", "css selector"]
    if locator_attribute not in possible_attributes:
        raise Exception("No Attribute Found.")

    else:
        try:
            element = context.driver.find_element(locator_attribute, locator_value)
            return element
        except:
            raise Exception


def assert_element_visible(context_or_element, locator_type, locator_text):
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_type, locator_text)
    if not element.is_displayed():
        raise AssertionError("Element not Displayed")


# ===========================================================================

def type_into_element(context_or_element, input_value, locator_type, locator_text):
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        input_value = context_or_element
    else:
        input_field = context_or_element.driver.find_element(locator_type, locator_text)
    input_field.send_keys(input_value)


def click(context_or_element, locator_type, locator_text):
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_type, locator_text)
    element.click()


def read_text(context_or_element, locator_type, locator_text):
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_type, locator_text)
    return element.text


def get_all_elements_list(context_or_element, locator_type, locator_text):
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        elements = context_or_element
    else:
        elements = context_or_element.driver.find_elements(locator_type, locator_text)
    return len(elements)


def add_to_cart(context_or_element, locator_type, locator_text, element_num):
    element = context_or_element.driver.find_element(locator_type, locator_text + "[" + element_num + "]" + '/a[2]')
    text = read_text(context_or_element, locator_type, locator_text + "[" + element_num + "]" + '/a[2]')
    if text == "Add to cart":
        element.click()
    else:
        element = context_or_element.driver.find_element(locator_type, locator_text + "[1]/a[2]")
        element.click()


def verify_title(context_or_element, locator_type, locator_text, expected_page_title):
    """
    Function to check if title is same as expected
    :param context:
    :param expected_page_title:
    :return:
    """
    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        actual_title = context_or_element
    else:
        actual_title = read_text(context_or_element, locator_type, locator_text)
    assert actual_title == expected_page_title, "Title is not the same as expected."


def wait_time(context, locator_type, locator_text, min_time=10):
    element = WebDriverWait(context.driver, min_time). \
        until(EC.presence_of_element_located((locator_type, locator_text)))

    if element:
        print("Element Found")
    else:
        print("Element not found. ")
