ALL_PRODUCT_LIST = {
    "ALL_PRODUCT_LIST_PAGE1": {"type": "xpath", 'locator': '//*[@id="main"]/ul/li'},
    "ALL_PRODUCT_LIST_PAGE2": {"type": "xpath", 'locator': '//*[@id="main"]/ul/li'}
}

ELEMENT_TEXT = {
    "ELEMENT_TEXT": {'type': 'xpath', 'locator': '//*[@id="main"]/ul/li/a[2]'}
}

CART_ELEMENT = {
    "ELEMENT_IN_CART": {"type": "xpath", "locator": '//*[@id="site-header-cart"]/li[1]/a/span[2]'},
    "SHOP_CART": {"type": "xpath", "locator": '//*[@id="site-header-cart"]/li[1]/a'},
    "CART_PAGE_TITLE": {"type": "xpath", "locator": '//*[@id="post-7"]/header/h1'},
    "CHECKOUT_PAGE_TITLE": {"type": "xpath", "locator": '//*[@id="post-8"]/header/h1'},
    "PROCEED_CHECKOUT": {"type": "xpath", "locator": '//*[@id="post-7"]/div[1]/div/div[2]/div/div/a'}
}

SHIPPING_ADDRESS = {
    "FIRST_NAME": {"type": "xpath", "locator": '//*[@id="billing_first_name_field"]/span/input'},
    "LAST_NAME": {"type": "xpath", "locator": '//*[@id="billing_last_name_field"]/span/input'},
    "COMPANY": {"type": "xpath", "locator": '//*[@id="billing_company"]'},
    "COUNTRY": {"type": "xpath", "locator": '//*[@id="select2-billing_country-container"]'},
    "STREET_ADDRESS": {"type": "xpath", "locator": '//*[@id="billing_address_1"]'},
    "CITY": {"type": "xpath", "locator": '//*[@id="billing_city"]'},
    "STATE": {"type": "xpath", "locator": '//*[@id="select2-billing_state-container"]'},
    "POSTAL_CODE": {"type": "xpath", "locator": '//*[@id="billing_postcode"]'},
    "PHONE": {"type": "xpath", "locator": '//*[@id="billing_phone"]'},
    "EMAIL": {"type": "xpath", "locator": '//*[@id="billing_email"]'},
}

SHIPPING_METHOD = {
    "FLAT_RATE": {"type": "css selector", "locator": '#shipping_method > li:nth-child(1)'},
    "FREE_SHIPPING": {"type": "css selector", "locator": '#shipping_method > li:nth-child(2)'},
    "LOCAL_PICKUP": {"type": "css selector", "locator": '#shipping_method > li:nth-child(3)'},
}

PAYMENT_OPTION = {
    "CASH_PAYMENT": {"type": "xpath", "locator": '//*[@id="payment"]/ul/li[1]'},
    "CASH_ON_DELIVERY": {"type": "xpath", "locator": '//*[@id="payment"]/ul/li[2]'},
}

PLACE_ORDER = {
    "PLACE_ORDER": {"type": "xpath", "locator": '//*[@id="place_order"]'}
}

ORDER_DETAILS = {
    "ORDER_RECEIVED_MSG": {"type": "xpath", "locator": '//*[@id="post-8"]/header/h1'}
}