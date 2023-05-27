from selenium import webdriver


def go_to(url, browser_type=None):
    """
    :param url:
    :param browser_type: can set any browser, either chrome or EI, default is Firefox
    :return url:
    """
    if not browser_type:
        driver = webdriver.Chrome()

    elif browser_type.lower() == "firefox":
        driver = webdriver.Firefox()

    else:
        raise Exception(f"The Browser type {browser_type} is not supported")

    url = url.strip()
    driver.get(url)

    return driver


def assert_page_title(context, expected_page_title):
    """
    Function to check if title is same as expected
    :param context:
    :param expected_page_title:
    :return:
    """

    actual_title = context.driver.title

    print("Actual title is : ", actual_title)
    print("Expected title is : ", expected_page_title)

    assert expected_page_title == actual_title, "Title is not the same as expected."


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

    print("Actual title is : ", actual_current_url)
    print("Expected title is : ", expected_current_url)

    assert expected_current_url == actual_current_url, "URL is not the same as expected."
