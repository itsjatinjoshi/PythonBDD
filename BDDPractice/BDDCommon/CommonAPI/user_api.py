from BDDCommon.CommonHelpers.WooRequestHelpers import WooRequestHelper


def create_user(data):
    return WooRequestHelper().post(wc_end_point="customers", params=data)
