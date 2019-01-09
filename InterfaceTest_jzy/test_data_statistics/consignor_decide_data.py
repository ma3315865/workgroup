# coding = utf-8
import ast
from InterfaceTest_jzy.BaseInf import post_interfaces


class DecideConsigorDatas(object):
    def __init__(self):
        self.post_interface = post_interfaces.PostInterface('Consignor', '20053')

    def get_consignor_results(self):
        uid = self.post_interface.post_uid()
        token = self.post_interface.post_token()
        data = {
            "base": {
                "uid": uid,
                "token": token
            },
            "params": {
            }
        }
        results = self.post_interface.get_result(data)
        return results.text

    def dict_results(self):
        return ast.literal_eval(self.get_consignor_results())

    def get_dict_root(self):
        return self.dict_results().get('data').get('result')

    def get_exception_order_num(self):
        return self.get_dict_root().get('exceptionOrderNum')

    def get_pay_freight_num(self):
        return self.get_dict_root().get('payFreightNum')

    def get_car_count_num(self):
        return self.get_dict_root().get('carCountNum')

    def get_load_weight_num(self):
        return self.get_dict_root().get('loadWeightNum')

    def get_order_num(self):
        return self.get_dict_root().get('orderNum')

    def get_load_volume_num(self):
        return self.get_dict_root().get('loadVolumeNum')

    def get_cancel_order_num(self):
        return self.get_dict_root().get('cancelOrderNum')


if __name__ == '__main__':
    main = DecideConsigorDatas()
    # dicts = main.get_dict_root()
    # re = dicts.get('payFreightNum')
    re = main.get_pay_freight_num()
    print(re)
    print(type(re))