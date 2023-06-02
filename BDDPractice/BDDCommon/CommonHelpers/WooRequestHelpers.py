from woocommerce import API
from BDDCommon.CommonHelpers.CredentailsHelper import CredentialsHelper


class WooRequestHelper(object):

    def __init__(self):
        credential_helper = CredentialsHelper()
        wc_credentials = credential_helper.get_wc_api_keys()

        self.wcapi = API(
            url="http://mystore.local",
            consumer_key=wc_credentials['wc_key'],
            consumer_secret=wc_credentials['wc_secret'],
            version="wc/v3",
            timeout=20
        )

    def assert_status_code(self):
        assert self.response.status_code == self.expected_status_code, \
            f"Bad Status Code. EndPoint: {self.wc_end_point}," \
            f"Params: {self.params}, Actual Status Code: {self.response}, " \
            f"Expected Status Code: {self.expected_status_code}"

    def get(self, wc_end_point, params=None, expected_status_code=200):
        self.response = self.wcapi.get(wc_end_point, params=params,)
        self.wc_end_point = wc_end_point
        self.params = params
        self.expected_status_code = expected_status_code
        self.assert_status_code()

        return self.response.json()

    def post(self, wc_end_point, params=None, expected_status_code=201):
        self.response = self.wcapi.post(wc_end_point, data=params)
        self.wc_end_point = wc_end_point
        self.params = params
        self.expected_status_code = expected_status_code
        self.assert_status_code()
        print(self.response)
        return self.response.json()

    def put(self, wc_end_point, param=None, expected_status_code=200):
        # response = self.wcapi.put(wc_end_point, param=param)
        # assert response == expected_status_code, f"Wrong status code {response}"
        pass

    def delete(self, wc_end_point, param=None, expected_status_code=200):
        # response = self.wcapi.delete(wc_end_point, param=param)
        # assert response == expected_status_code, f"Wrong status code {response}"
        pass


if __name__ == '__main__':
    obj = WooRequestHelper()
    # obj.get("products")

    payload = {
        "email": "temp@gmail.com",
        "password": "temp@123"
    }
    obj.post("customers", params=payload)
