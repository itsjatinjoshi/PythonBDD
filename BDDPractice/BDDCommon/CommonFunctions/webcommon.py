from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from BDDCommon.Configs import configs


def go_to(context, location):
    """
    :param context:
    :param location:
    :return:
    """

    if not location.startswith('http'):
        _url = configs.URL_CONFIG.get(location)
        base_url = configs.URL_CONFIG.get('base_url')
        url = base_url + _url

    browser = context.config.userdata.get('browser')

    if not browser:
        browser = 'chrome'

    if browser.lower() == 'chrome':
        context.driver = webdriver.Chrome()

    elif browser.lower() in ("ff", "firefox"):
        context.driver = webdriver.Firefox()

    else:
        raise Exception(f"The Browser type {browser} is not supported")

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

    print("Actual title is : ", actual_title)
    print("Expected title is : ", expected_page_title)

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

    print("Actual URL is : ", actual_current_url)
    print("Expected URL is : ", expected_current_url)

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
