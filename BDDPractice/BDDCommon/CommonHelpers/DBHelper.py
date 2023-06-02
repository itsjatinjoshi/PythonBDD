import pymysql
from BDDCommon.CommonHelpers.CredentailsHelper import CredentialsHelper


class DBHelper(object):

    def __init__(self):
        credentailsHelper = CredentialsHelper()
        cred = credentailsHelper.get_db_credentials()
        self.host = 'localhost'
        self.db_user = cred['db_user']
        self.db_password = cred['db_password']

    def create_connection(self):
        self.connection = pymysql.connect(host=self.host, user=self.db_user, password=self.db_password, port=3306)

    def execute_select(self, sql):
        try:
            self.create_connection()
            cur = self.connection.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            dict_response = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running {sql} query. Error: {str(e)}")

        finally:
            self.connection.close()

        return dict_response

    def execute_sql(self):
        pass
