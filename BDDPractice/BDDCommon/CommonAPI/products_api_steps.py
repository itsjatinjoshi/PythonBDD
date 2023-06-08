from BDDCommon.CommonHelpers.WooRequestHelpers import WooRequestHelper


def get_all_products_api():
    all_products = []
    max_pages = 1000
    per_page = 1
    while per_page <= max_pages:

        param = {"per_page": 100, "page": per_page}
        response = WooRequestHelper().get(wc_end_point="products", params=param)

        if response:
            per_page += 1
            all_products.extend(response)
        else:
            print("No Product remaining")
            break

    return all_products


def get_product_by_id(product_id):
    response = WooRequestHelper().get(wc_end_point=f"products/{product_id}")
    return response
