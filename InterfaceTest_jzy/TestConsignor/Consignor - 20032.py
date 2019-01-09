# coding : utf-8
import time
import configparser
from InterfaceTest_jzy.BaseInf import post_interfaces
from InterfaceTest_jzy.Config import read_config as con


class Consignor20032(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('D:\python\InterfaceTest_jzy\Config\config.ini')
        configer = con.TestFile(config)
        self.intface = post_interfaces.PostInterface('Consignor', '20032')
        self.uid = self.intface.post_uid()
        self.token = self.intface.post_token()
        self.pic = configer.common_pic()
        self.customize_order_no = self.input_date()[0]
        self.project_name = self.input_date()[1]
        self.load_name = self.input_date()[2]

    @staticmethod
    def input_date():
        local_time = time.localtime()
        date_year = time.strftime('%y', local_time) + '年'
        date_month = time.strftime('%m', local_time) + '月'
        date_day = time.strftime('%d', local_time) + '日'
        date_hour = time.strftime('%H', local_time) + '时'
        date_min = time.strftime('%M', local_time) + '分'
        date_sec = time.strftime('%S', local_time) + '秒'
        date_name = date_year + date_month + date_day + date_hour + date_min + date_sec
        customize_order_no = '测试货主订单号' + date_name
        project_name = '测试项目名称' + date_name
        load_name = '测试品名' + date_name
        return customize_order_no, project_name, load_name

    def inter_datas(self):
        return {
            "base": {
                "uid": self.uid,
                "token": self.token
            },
            "params": {
                "orderId": "31d41d69-e0c3-11e8-bb03-00163e04a258",  # 订单ID 重新编辑传值(可空)
                "exceptionCode": "其他",  # 异常代码 字典项
                "exceptionReason": "测试货主加入异常，其他异常原因",  # 异常原因
                "exceptionFilePath": self.pic  # 附件
            }
        }

    def interface_20032(self):
        return self.intface.get_result(self.inter_datas())


if __name__ == '__main__':
    main = Consignor20032()
    print(main.interface_20032().text)

