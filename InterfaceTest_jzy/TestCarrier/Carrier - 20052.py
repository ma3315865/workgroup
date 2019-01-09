# coding : utf-8
import configparser
from InterfaceTest_jzy.BaseInf import post_interfaces, Get_Tokens, time_pro
from InterfaceTest_jzy.Config import read_config as con


class Carrier20052(object):
    def __init__(self):
        """
        Carrier - 20052发布大订单

        """
        config = configparser.ConfigParser()
        config.read('D:\python\InterfaceTest_jzy\Config\config.ini')
        configer = con.TestFile(config)
        self.intface = post_interfaces.PostInterface('Carrier', '20052')
        self.uid = self.intface.post_uid()
        self.token = self.intface.post_token()
        self.pic = configer.common_pic()
        time_data = time_pro.TimeProjectName()
        self.customize_order_no = time_data.customize_order_no
        self.project_name = time_data.project_name
        self.load_name = time_data.load_name

    def inter_datas(self):
        list1 = '{"customizeOrderNo": "",' \
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

        list2 = '{"customizeOrderNo": "",' \
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

        # sub = '[{0}]'.format(list1)
        # sub = '[{0}]'.format(list2)
        sub = '[{0},{1}]'.format(list1, list2)
        return {
            "base": {
                "uid": self.uid,
                "token": self.token
            },
            "params": {
                "customizeOrderNo": self.customize_order_no,              # 货主订单号
                "projectName": self.project_name,                   # 项目名称
                "loadName": self.load_name,                      # 品名
                "loadWeight": "10",                    # 货物总重量(吨)
                "loadVolume": "10",                    # 货物总体积（立方米）
                "loadCount": "1",                     # 货物件数 (可空)
                "singleSize": "单个长宽高 (可空)test_data_statistics",                    # 单个长宽高 (可空)
                "packageType": "木箱",                   # 包装形式
                "transportMode": "整车",                 # 运输模式
                "sendOrg": "发货单位test发货单位test",                       # 发货单位
                "sendLocationPId": "10",               # 发货地省id
                "sendLocationCId": "189",               # 发货地市id
                "sendLocationAId": "1170",               # 发货地县区id (可空)
                "sendLocationName": "向阳",              # 发货地 省+市+县
                "sendDetailAddress": "发货详细地址test发货详细地址test",             # 发货详细地址
                "sendDate": "2019-10-23",                      # 发货时间 yyyy-MM-dd
                "sendTime": "上午6点-8点",                      # 发货时间段
                "sendTimeHour": "6",                  # 发货整点 发货时间段字典项的value(sendTime)
                "senderName": "发货人姓名test",                    # 发货人姓名
                "senderPhone": "15600000000",                   # 发货人手机号码
                "receiveOrg": "收货单位test收货单位test收货单位test",                    # 收货单位
                "receiveLocationPId": "31",            # 收货地省id
                "receiveLocationCId": "473",            # 收货地市id
                "receiveLocationAId": "3230",            # 收货地县区id
                "receiveLocationName": "阿克陶",           # 收货地 省+市+县
                "receiveDetailAddress": "收货详细地址test收货详细地址test收货详细地址test",          # 收货详细地址
                "receiverTime": "2032-09-26",                  # 收货时间 yyyy-MM-dd
                "receiverName": "收货人姓名test",                  # 收货人姓名
                "receiverPhone": "15600000000",                 # 收货人手机号码
                "signatureRequirements": "不需要",         # 签收单的要求
                "signatureRequirementsCode": "0",     # 签收单的要求code signatureRequirements字典项的value
                "loadPic1": self.pic,                      # 获取图片1 (可空)
                "loadPic2": self.pic,                      # 获取图片2 (可空)
                "loadPic3": self.pic,                      # 获取图片3 (可空)
                "loadPic4": self.pic,                      # 获取图片4 (可空)
                "loadPic5": self.pic,                      # 获取图片5 (可空)
                "remarks": "备注 (可空)test_data_statistics",                       # 备注 (可空)
                "subList": sub
            }
        }

    def interface_20052(self):
        return self.intface.get_result(self.inter_datas())


if __name__ == '__main__':
    token = Get_Tokens.GetToken()
    token.write_token()
    main = Carrier20052()
    print(main.interface_20052().text)
