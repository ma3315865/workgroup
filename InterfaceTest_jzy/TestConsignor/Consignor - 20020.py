# coding : utf-8
import configparser
from InterfaceTest_jzy.BaseInf import post_interfaces, Get_Tokens, time_pro
from InterfaceTest_jzy.Config import read_config as con


class Consignor20020(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('D:\python\InterfaceTest_jzy\Config\config.ini')
        configer = con.TestFile(config)
        self.intface = post_interfaces.PostInterface('Consignor', '20020')
        self.uid = self.intface.post_uid()
        self.token = self.intface.post_token()
        self.pic = configer.common_pic()
        self.goods_uri = configer.consignor_goods_uri()
        time_data = time_pro.TimeProjectName()
        self.customize_order_no = time_data.customize_order_no
        self.project_name = time_data.project_name
        self.load_name = time_data.load_name

    def inter_datas(self):
        return {
            "base": {
                "uid": self.uid,
                "token": self.token
            },
            "params": {
                "id": "",  # 订单ID 重新编辑传值(可空)
                "customizeOrderNo": self.customize_order_no,  # 货主订单号
                "carrierCompanyId": "4fe3cc7c-d59d-11e8-bb03-00163e04a258",  # 承运商公司ID (可空)
                "projectName": self.project_name,  # 项目名称
                "loadName": self.load_name,  # 品名
                "loadWeight": "10",  # 货物总重量(吨)
                "loadVolume": "11",  # 货物总体积（立方米）
                "loadCount": "12",  # 货物件数 (可空)
                "singleSize": "12",  # 单个长宽高 (可空)
                "packageType": "木箱",  # 包装形式
                "transportMode": "整车",  # 运输模式
                "sendOrg": "发货单位test",  # 发货单位
                "sendLocationPId": "7",  # 发货地省id
                "sendLocationCId": "156",  # 发货地市id
                "sendLocationAId": "906",  # 发货地县区id (可空)
                "sendLocationName": "察哈尔",  # 发货地 省+市+县
                "sendDetailAddress": "发货详细地址test发货详细地址test",  # 发货详细地址
                "sendDate": "2019-09-26",  # 发货时间 yyyy-MM-dd
                "sendTime": "22:00:00",  # 发货时间段
                "sendTimeHour": "22:00-23:59",  # 发货整点 发货时间段字典项的value(sendTime)
                "senderName": "发货人姓名test",  # 发货人姓名
                "senderPhone": "13400000000",  # 发货人手机号码
                "receiveOrg": "收货单位test",  # 收货单位
                "receiveLocationPId": "31",  # 收货地省id
                "receiveLocationCId": "473",  # 收货地市id
                "receiveLocationAId": "3230",  # 收货地县区id
                "receiveLocationName": "阿克陶",  # 收货地 省+市+县
                "receiveDetailAddress": "发货详细地址test收货详细地址test",  # 收货详细地址
                "receiverTime": "2032-09-26",  # 收货时间 yyyy-MM-dd
                "receiverName": "收货人姓名test",  # 收货人姓名
                "receiverPhone": "13400000000",  # 收货人手机号码

                "issueType": "1",  # 发布类型(0是招标,1是指)

                "bidValidTime": "2019-09-30 16:50:42",  # yyyy-MM-dd hh:mm:ss
                "expectedLoadMoney": "10",  # 预期运费金额 保留两位小数点
                "signatureRequirements": "不需要",  # 签收单的要求
                "signatureRequirementsCode": "0",  # 签收单的要求code signatureRequirements字典项的value
                "ifInsurance": "1",  # 是否投保
                "insuranceMoney": "12",  # 投保金额
                "loadPic1": self.pic,  # 获取图片1 (可空)
                "loadPic2": self.pic,  # 获取图片2 (可空)
                "loadPic3": self.pic,  # 获取图片3 (可空)
                "loadPic4": self.pic,  # 获取图片4 (可空)
                "loadPic5": self.pic,  # 获取图片5 (可空)
                "attachmentFilePath": self.goods_uri,
                "carType": "平板",  # 车型 (可空)
                "carLength": "6米",  # 车厂 (可空)
                "remarks": "备注 (可空)测试数据",  # 备注 (可空)
                "ifInvoice": "1",  # 是否需要发票(0否，1是) 需要发票时以下字段必填
                "invoiceType": "0",  # 发票类型（0是普通发票，1是专用发票)
                "invoiceCompanyTitle": "发票抬头公司名称test",  # 发票抬头公司名称
                "invoiceCompanyTaxNo": "纳税人识别号test",  # 纳税人识别号
                "invoiceAddress": "单位地址test",  # 单位地址
                "invoicePhone": "电话号码test",  # 电话号码
                "invoiceBank": "开户银行test",  # 开户银行
                "invoiceBankNo": "银行账号test"  # 银行账号
            }
        }

    def interface_20020(self):
        return self.intface.get_result(self.inter_datas())


if __name__ == '__main__':
    token = Get_Tokens.GetToken()
    token.write_token()
    main = Consignor20020()
    print(main.interface_20020().text)