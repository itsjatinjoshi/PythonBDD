from behave import step
from BDDCommon.CommonDAO.orderDAO import OrderDAO


@step('verify order is created in database')
def verify_order_created_in_database(context):
    order_database = OrderDAO().get_user_by_id_from_database(context.order_id)
    assert order_database, f" {context.order_id} is not found in database."
    assert order_database[0]['post_type'] == 'shop_order', f"Post type not found in Database."
