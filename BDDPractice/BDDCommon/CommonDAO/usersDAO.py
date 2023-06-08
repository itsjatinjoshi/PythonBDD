import random

from BDDCommon.CommonHelpers.DBHelper import DBHelper


class UserDAO(object):

    def __init__(self):
        self.db_helper = DBHelper()

    def get_user_by_email_from_database(self, email):
        sql_query = f"select * from local.wp_users where user_email='{email}';"
        query_response = self.db_helper.execute_select(sql_query)
        return query_response
