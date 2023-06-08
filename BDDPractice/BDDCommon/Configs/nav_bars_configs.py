NAV_BAR_CONFIG = {
    "Home": {'type': 'xpath', 'locator': '//*[@id="mainContent"]/div[1]/ul/li[1]'},
    "Saved": {'type': 'xpath', 'locator': '//*[@id="mainContent"]/div[1]/ul/li[2]'},
    "Fashion": {'type': 'xpath', 'locator': '//*[@id="mainContent"]/div[1]/ul/li[3]'},
    "Sneakers": {'type': 'xpath', 'locator': '//*[@id="mainContent"]/div[1]/ul/li[4]'},
    "Motors": {'type': 'xpath', 'locator': '//*[@id="mainContent"]/div[1]/ul/li[5]'},
    "Electronics": {'type': 'xpath', 'locator': '//*[@id="mainContent"]/div[1]/ul/li[6]'},

}

MY_ACCOUNT_LOCATORS = {
    "LOGIN_FIELD": {'type': 'id', 'locator': 'username'},
    "PSWD_FIELD": {'type': 'id', 'locator': 'password'},
    "LOGIN_BTN": {'type': 'css selector', 'locator': 'button[name="login"]'},
    "LEFT_NAV": {'type': 'xpath', 'locator': "//*[@id='post-9']/div/div/nav/ul"},
    "LOGOUT_LINK": {'type': 'xpath', 'locator': "//*[@id='post-9']/div/div/nav/ul/li[6]/a"},
    "WRONG_PSWD": {'type': 'xpath', 'locator': '//*[@id="content"]/div/div[1]/ul/li'},
    "WRONG_EMAIL": {'type': 'xpath', 'locator': '//*[@id="content"]/div/div[1]/ul/li'},
}



