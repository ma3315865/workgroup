# coding : utf-8
import configparser
from InterfaceTest_jzy.BaseInf import post_interfaces, Get_Tokens, time_pro
from InterfaceTest_jzy.Config import read_config as con


class Carrier20037(object):
    def __init__(self):
        """
        Carrier - 20037发布小订单

        """
        config = configparser.ConfigParser()
        config.read('D:\python\InterfaceTest_jzy\Config\config.ini')
        configer = con.TestFile(config)
        self.intface = post_interfaces.PostInterface('Carrier', '20037')
        self.uid = self.intface.post_uid()
        self.token = self.intface.post_token()
        self.pic = configer.common_pic()
        time_data = time_pro.TimeProjectName()
        self.customize_order_no = time_data.customize_order_no
        self.project_name = time_data.project_name
        self.load_name = time_data.load_name
        self.order_id = "211625fd-f6c4-11e8-bb03-00163e04a258"

    def inter_datas(self):
        """
        id 指定不同意, 重新编辑会有值， sub_order_id
        """
        list1 = '{' \
                '"id": "",' \
                '"customizeOrderNo": "",' \
                '"loadWeight": "1",' \
                '"loadVolume": "1",' \
                '"loadCount": "1",' \
                '"carType": "高栏",' \
                '"carLength": "5米",' \
                '"carCount": "13",' \
                '"expectedLoadMoney": "10",' \
                '"chooseDriverId": "",' \
                '"chooseDriverName":"",' \
                '"bidValidTime": "2019-10-25 12:12:12",' \
                '"payMode": "2",' \
                '"moneyRatio": "70",' \
                '"oilCardRatio": "30"}'

        list2 = '{' \
                '"id": "",' \
                '"customizeOrderNo": "",' \
                '"loadWeight": "9",' \
                '"loadVolume": "9",' \
                '"loadCount": "9",' \
                '"carType": "高栏",' \
                '"carLength": "5米",' \
                '"carCount": "13",' \
                '"expectedLoadMoney": "10",' \
                '"chooseDriverId": "3e6e3b5d-cc7d-11e8-bb03-00163e04a258",' \
                '"chooseDriverName":"TESTma",' \
                '"bidValidTime": "2019-10-25 12:12:12",' \
                '"payMode": "2",' \
                '"moneyRatio": "70",' \
                '"oilCardRatio": "30"}'
        # sub = '[{}]'.format(list1)
        # sub = '[{}]'.format(list2)
        sub = '[{0},{1}]'.format(list1, list2)
        return {
            "base": {
                "uid": self.uid,
                "token": self.token
            },
            "params": {
                "orderId": self.order_id,                       # 大订单ID
                "subList": sub
            }
        }

    def interface_20037(self):
        return self.intface.get_result(self.inter_datas())


if __name__ == '__main__':
    token = Get_Tokens.GetToken()
    token.write_token()
    main = Carrier20037()
    print(main.interface_20037().text)
