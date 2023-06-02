import os


class CredentialsHelper(object):

    def __init__(self):
        pass

    def get_wc_api_keys(self):
        wc_key = os.environ.get("WC_CUSTOMER_KEY")
        wc_secret = os.environ.get("WC_CUSTOMER_SECRET")

        if not wc_key or not wc_secret:
            raise Exception("Wrong API key or Secret key or might be not saved in SYSTEM ENV.")
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}

    def get_db_credentials(self):
        # todo create credentials for db and use it
        db_user = os.environ.get("DB_USER")
        db_password = os.environ.get("DB_PASSWORD")

        if not db_user or not db_password:
            raise Exception("The DB USERNAME and DB PASSWORD or might be not saved in SYSTEM ENV. ")
        else:
            return {'db_user': db_user, 'db_password': db_password}
