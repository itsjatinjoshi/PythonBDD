from behave import step

from BDDCommon.CommonAPI.products_api_steps import get_all_products_api, get_product_by_id
from BDDCommon.CommonDAO.productsDAO import ProductsDAO


@step('I get number of available product from db')
def get_all_products_from_database(context):
    """
    Get all the products from the database.
    :param context:
    :return:
    """
    all_rows = ProductsDAO().get_app_products_from_database()
    # print("NO OF ROWS : ", len(all_rows))
    context.qty_products_database = len(all_rows)


@step('I get number of available product from api')
def get_all_products_from_api(context):
    number_of_products = get_all_products_api()
    context.qty_products_api = len(number_of_products)


@step('total number of products in api and db should be same')
def total_num_of_products_in_api_and_db_should_same(context):
    assert context.qty_products_database == context.qty_products_api, \
        "LENGTH OF PRODUCTS ARE NOT EQUAL"


@step('Get "{qty}" random product from Database')
def get_random_product_from_db(context, qty):
    random_product = ProductsDAO().get_product_detail_from_database(qty)
    context.random_product = random_product


@step('Verify the product api return the correct product id.')
def verify_product_api_return_correct_product_by_id(context):

    product_id = context.random_product[0]['ID']
    context.product_id = product_id
    response = get_product_by_id(product_id)

    context.response = response


@step('verify API name and DB post title are same')
def verify_apiName_and_postTitle_are_same(context):
    context.response['id'] = context.product_id, "Wrong ID"
    context.response['name'] = context.random_product[0]['post_title'], "Wrong Name"
