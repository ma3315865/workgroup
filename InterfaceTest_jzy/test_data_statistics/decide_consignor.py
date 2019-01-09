# coding = utf-8
import configparser
from InterfaceTest_jzy.test_data_statistics import consignor_decide_data


class DecideConsignor(object):
    def __init__(self):
        self.cdc = consignor_decide_data.DecideConsigorDatas()
        self.config_file_path = 'D:\python\InterfaceTest_jzy\Config\config.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path)

    @staticmethod
    def subtraction(data1, data2):
        return data1-data2

    def decide_exception_num(self):
        data_l = self.config.get('decide_consignor_datas', 'exceptionOrderNum')
        data1 = float(data_l)
        data2 = self.cdc.get_exception_order_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    def decide_pay_freight(self):
        data_l = self.config.get('decide_consignor_datas', 'payFreightNum')
        data1 = float(data_l)
        data2 = self.cdc.get_pay_freight_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    def decide_car_count(self):
        data_l = self.config.get('decide_consignor_datas', 'carCountNum')
        data1 = float(data_l)
        data2 = self.cdc.get_car_count_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    def decide_load_weight(self):
        data_l = self.config.get('decide_consignor_datas', 'loadWeightNum')
        data1 = float(data_l)
        data2 = self.cdc.get_load_weight_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    def decide_order_num(self):
        data_l = self.config.get('decide_consignor_datas', 'orderNum')
        data1 = float(data_l)
        data2 = self.cdc.get_order_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    def decide_load_volume(self):
        data_l = self.config.get('decide_consignor_datas', 'loadVolumeNum')
        data1 = float(data_l)
        data2 = self.cdc.get_load_volume_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    def decide_cancel_num(self):
        data_l = self.config.get('decide_consignor_datas', 'cancelOrderNum')
        data1 = float(data_l)
        data2 = self.cdc.get_cancel_order_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    def print_result(self):
        print('累计异常' + str(self.decide_exception_num()))
        print('应付费用' + str(self.decide_pay_freight()))
        print('累计车次' + str(self.decide_car_count()))
        print('累计货量' + str(self.decide_load_weight()))
        print('累计发单' + str(self.decide_order_num()))
        print('累计方量' + str(self.decide_load_volume()))
        print('累计取消' + str(self.decide_cancel_num()))


if __name__ == '__main__':
    main = DecideConsignor()
    print(type(main.decide_load_volume()))
    main.print_result()