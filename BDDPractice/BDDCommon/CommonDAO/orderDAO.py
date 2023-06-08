import random

from BDDCommon.CommonHelpers.DBHelper import DBHelper


class OrderDAO(object):

    def __init__(self):
        self.db_helper = DBHelper()

    def get_user_by_id_from_database(self, order_id):
        sql_query = f"SELECT * FROM local.wp_posts where ID={order_id};"
        query_response = self.db_helper.execute_select(sql_query)
        return query_response
