# coding = utf-8
import configparser
from InterfaceTest_jzy.test_data_statistics import carrier_decide_data


class DecideCarrier(object):
    """
    输出结果为与上次写入结果比较，用于判断承运商统计

    releaseOrderNum 累计车次
    inComeNum 总收入金额
    exceptionOrderNum 累计异常
    outOrderNum 外部接单（承运商自己发单）
    carCountNum 累计件数
    loadWeightNum 累计货量
    outComeNum 总支出金额
    orderNum 累计接单
    loadVolumeNum 累计方量
    cancelOrderNum 累计取消
    profitNum 毛利润
    """
    def __init__(self):
        self.cdc = carrier_decide_data.DecideCarrierDatas()
        self.config_file_path = 'D:\python\InterfaceTest_jzy\Config\config.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path)

    @staticmethod
    def subtraction(data1, data2):
        return data1-data2

    def decide_releaseorder_num(self):
        data_l = self.config.get('decide_carrier_datas', 'releaseOrderNum')
        data1 = float(data_l)
        data2 = self.cdc.get_release_order_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    # inComeNum 总收入金额
    def decide_income_freight(self):
        data_l = self.config.get('decide_carrier_datas', 'inComeNum')
        data1 = float(data_l)
        data2 = self.cdc.get_income_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    # exceptionOrderNum 累计异常
    def decide_exceptionorder_count(self):
        data_l = self.config.get('decide_carrier_datas', 'exceptionOrderNum')
        data1 = float(data_l)
        data2 = self.cdc.get_exception_order_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    # outOrderNum 外部接单（承运商自己发单）
    def decide_outorder_weight(self):
        data_l = self.config.get('decide_carrier_datas', 'outOrderNum')
        data1 = float(data_l)
        data2 = self.cdc.get_outorder_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    # carCountNum 累计件数
    def decide_carcount_num(self):
        data_l = self.config.get('decide_carrier_datas', 'carCountNum')
        data1 = float(data_l)
        data2 = self.cdc.get_carcount_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    # loadWeightNum 累计货量
    def decide_loadweight_volume(self):
        data_l = self.config.get('decide_carrier_datas', 'loadWeightNum')
        data1 = float(data_l)
        data2 = self.cdc.get_loadweight_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    # outComeNum 总支出金额
    def decide_outcome_num(self):
        data_l = self.config.get('decide_carrier_datas', 'outComeNum')
        data1 = float(data_l)
        data2 = self.cdc.get_outcome_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    # orderNum 累计接单
    def decide_order_num(self):
        data_l = self.config.get('decide_carrier_datas', 'orderNum')
        data1 = float(data_l)
        data2 = self.cdc.get_order_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    # loadVolumeNum 累计方量
    def decide_loadvolume_num(self):
        data_l = self.config.get('decide_carrier_datas', 'loadVolumeNum')
        data1 = float(data_l)
        data2 = self.cdc.get_loadvolume_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    # cancelOrderNum 累计取消
    def decide_cancelorder_num(self):
        data_l = self.config.get('decide_carrier_datas', 'cancelOrderNum')
        data1 = float(data_l)
        data2 = self.cdc.get_cancelorder_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    # profitNum 毛利润
    def decide_profit_num(self):
        data_l = self.config.get('decide_carrier_datas', 'profitNum')
        data1 = float(data_l)
        data2 = self.cdc.get_profit_num()
        if data1 != data2:
            return self.subtraction(data2, data1)

    def print_result(self):
        print('累计车次' + str(self.decide_releaseorder_num()))
        print('总收入金额' + str(self.decide_income_freight()))
        print('累计异常' + str(self.decide_exceptionorder_count()))
        print('外部接单（承运商自己发单）' + str(self.decide_outorder_weight()))
        print('累计件数' + str(self.decide_carcount_num()))
        print('累计货量' + str(self.decide_loadweight_volume()))
        print('总支出金额' + str(self.decide_outcome_num()))
        print('累计接单' + str(self.decide_order_num()))
        print('累计方量' + str(self.decide_loadvolume_num()))
        print('累计取消' + str(self.decide_cancelorder_num()))
        print('毛利润' + str(self.decide_profit_num()))


if __name__ == '__main__':
    main = DecideCarrier()
    main.print_result()