# coding = utf-8
import configparser
from InterfaceTest_jzy.test_data_statistics.consignor_decide_data import DecideConsigorDatas
from InterfaceTest_jzy.test_data_statistics.carrier_decide_data import DecideCarrierDatas


class WriteDecideIni(object):
    def __init__(self):
        self.config_file_path = 'D:\python\InterfaceTest_jzy\Config\config.ini'
        self.consignor_datas = DecideConsigorDatas()
        self.carrier_datas = DecideCarrierDatas()
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path)

    def write_consignor_ini(self):
        _exception_order = str(self.consignor_datas.get_exception_order_num())
        _pay_freight = str(self.consignor_datas.get_pay_freight_num())
        _car_count = str(self.consignor_datas.get_car_count_num())
        _load_weight = str(self.consignor_datas.get_load_weight_num())
        _order_num = str(self.consignor_datas.get_order_num())
        _load_volume = str(self.consignor_datas.get_load_volume_num())
        _cancel_order = str(self.consignor_datas.get_cancel_order_num())
        self.config.set('decide_consignor_datas', 'exceptionOrderNum', value=_exception_order)
        self.config.set('decide_consignor_datas', 'payFreightNum', value=_pay_freight)
        self.config.set('decide_consignor_datas', 'carCountNum', value=_car_count)
        self.config.set('decide_consignor_datas', 'loadWeightNum', value=_load_weight)
        self.config.set('decide_consignor_datas', 'orderNum', value=_order_num)
        self.config.set('decide_consignor_datas', 'loadVolumeNum', value=_load_volume)
        self.config.set('decide_consignor_datas', 'cancelOrderNum', value=_cancel_order)
        self.config.write(open(self.config_file_path, "r+"))

    def write_carrier_ini(self):
        _release_order = str(self.carrier_datas.get_release_order_num())
        _income = str(self.carrier_datas.get_income_num())
        _exception = str(self.carrier_datas.get_exception_order_num())
        _outorder = str(self.carrier_datas.get_outorder_num())
        _carcount = str(self.carrier_datas.get_carcount_num())
        _loadweight = str(self.carrier_datas.get_loadweight_num())
        _outcome = str(self.carrier_datas.get_outcome_num())
        _order = str(self.carrier_datas.get_order_num())
        _loadvolume = str(self.carrier_datas.get_loadvolume_num())
        _cancelorder = str(self.carrier_datas.get_cancelorder_num())
        _profit = str(self.carrier_datas.get_profit_num())
        self.config.set('decide_carrier_datas', 'releaseOrderNum', value=_release_order)
        self.config.set('decide_carrier_datas', 'inComeNum', value=_income)
        self.config.set('decide_carrier_datas', 'exceptionOrderNum', value=_exception)
        self.config.set('decide_carrier_datas', 'outOrderNum', value=_outorder)
        self.config.set('decide_carrier_datas', 'carCountNum', value=_carcount)
        self.config.set('decide_carrier_datas', 'loadWeightNum', value=_loadweight)
        self.config.set('decide_carrier_datas', 'outComeNum', value=_outcome)
        self.config.set('decide_carrier_datas', 'orderNum', value=_order)
        self.config.set('decide_carrier_datas', 'loadVolumeNum', value=_loadvolume)
        self.config.set('decide_carrier_datas', 'cancelOrderNum', value=_cancelorder)
        self.config.set('decide_carrier_datas', 'profitNum', value=_profit)
        self.config.write(open(self.config_file_path, "w+"))


if __name__ == '__main__':
    wd = WriteDecideIni()
    wd.write_consignor_ini()
    wd.write_carrier_ini()