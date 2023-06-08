ORDER_PAGE_ELEMENT = {
    "THANK_YOU_TEXT": {'type': 'xpath', 'locator': '//*[@id="post-8"]/div[1]/div/div/p[1]'}
}

ORDER_DETAILED_ELEMENT = {
    "ID": {'type': 'xpath', 'locator': '//*[@id="post-8"]/div[1]/div/div/ul/li[1]/strong'},
    "DATE": {'type': 'xpath', 'locator': '//*[@id="post-8"]/div[1]/div/div/ul/li[2]/strong'},
    # "EMAIL": {'type': 'xpath', 'locator': '//*[@id="post-8"]/div[1]/div/div/ul/li[3]/strong'},
    "TOTAL": {'type': 'xpath', 'locator': '//*[@id="post-8"]/div[1]/div/div/ul/li[3]/strong'},
    "PAYMENT_METHOD": {'type': 'xpath', 'locator': '//*[@id="post-8"]/div[1]/div/div/ul/li[4]/strong'},
}
