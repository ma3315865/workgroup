# coding = utf-8
import ast
from BaseInf import post_interfaces


class DecideCarrierDatas(object):
    def __init__(self):
        self.post_interface = post_interfaces.PostInterface('Carrier', '20077')

    def get_carrier_results(self):
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
        return ast.literal_eval(self.get_carrier_results())

    def get_dict_root(self):
        return self.dict_results().get('data').get('result')

    def get_release_order_num(self):
        return self.get_dict_root().get('releaseOrderNum')

    def get_income_num(self):
        return self.get_dict_root().get('inComeNum')

    def get_exception_order_num(self):
        return self.get_dict_root().get('exceptionOrderNum')

    def get_outorder_num(self):
        return self.get_dict_root().get('outOrderNum')

    def get_carcount_num(self):
        return self.get_dict_root().get('carCountNum')

    def get_loadweight_num(self):
        return self.get_dict_root().get('loadWeightNum')

    def get_outcome_num(self):
        return self.get_dict_root().get('outComeNum')

    def get_order_num(self):
        return self.get_dict_root().get('orderNum')

    def get_loadvolume_num(self):
        return self.get_dict_root().get('loadVolumeNum')

    def get_cancelorder_num(self):
        return self.get_dict_root().get('cancelOrderNum')

    def get_profit_num(self):
        return self.get_dict_root().get('profitNum')


if __name__ == '__main__':
    main = DecideCarrierDatas()
    re = main.get_income_num()
    print(re)
    print(type(re))