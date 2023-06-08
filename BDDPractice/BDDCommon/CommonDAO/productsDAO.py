import random

from BDDCommon.CommonHelpers.DBHelper import DBHelper


class ProductsDAO(object):

    def __init__(self):
        self.db_helper = DBHelper()

    def get_app_products_from_database(self):
        sql_query = "select * from local.wp_posts where post_type='product';"
        query_response = self.db_helper.execute_select(sql_query)
        return query_response

    def get_product_detail_from_database(self, value):
        """
        A method that will return a
        :return:
        """
        sql_query = "select * from local.wp_posts where post_type='product' order by id desc Limit 5000;"
        query_response = self.db_helper.execute_select(sql_query)
        return random.sample(query_response, int(value))
