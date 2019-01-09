# coding : utf-8
import json
import requests
import configparser
import time
from InterfaceTest_jzy.Config import read_config as con
from InterfaceTest_jzy.BaseInf import baseJudge

config = configparser.ConfigParser()
config.read('D:\python\InterfaceTest_jzy\Config\config.ini')
configer = con.TestFile(config)

uid = configer.consignor_uid()
token = configer.consignor_token()
consignor_url = configer.consignor_url()
rsaKeyID = configer.common_rsaKeyID()
pic = configer.common_pic()

local_time = time.localtime()
Year = time.strftime('%y', local_time) + '年'
Month = time.strftime('%m', local_time) + '月'
Day = time.strftime('%d', local_time) + '日'
Hour = time.strftime('%H', local_time) + '时'
Min = time.strftime('%M', local_time) + '分'
Sec = time.strftime('%S', local_time) + '秒'
date_Name = Year+Month+Day+Hour+Min+Sec
customizeOrderNo = '货主订单号' + date_Name
Project_Name = '项目名称' + date_Name
LoadName = '品名' + date_Name

# url
url = consignor_url
uri = '20024'
URL = url + uri

# header
header = {'Content-Type': 'application/json',
          'XMLHttpRequest': 'X-Requested-With'}

# data
datas = {
    "base": {
        "uid": uid,
        "token": token
    },
    "params": {
        "id": "",                            # 订单ID 重新编辑传值(可空)
        "customizeOrderNo": customizeOrderNo,              # 货主订单号
        "carrierCompanyId": "1f2e17d9-cc7d-11e8-bb03-00163e04a258", # 承运商公司ID (可空)指定承运商是必填
        "projectName": Project_Name,                   # 项目名称
        "loadName": LoadName,                      # 品名
        "loadWeight": "10",                    # 货物总重量(吨)
        "loadVolume": "11",                    # 货物总体积（立方米）
        "loadCount": "",                     # 货物件数 (可空)
        "singleSize": "",                    # 单个长宽高 (可空)
        "packageType": "木箱",                   # 包装形式
        "transportMode": "整车",                 # 运输模式
        "sendOrg": "test_data_statistics",                       # 发货单位
        "sendLocationPId": "10",               # 发货地省id
        "sendLocationCId": "183",               # 发货地市id
        "sendLocationAId": "1107",               # 发货地县区id (可空)
        "sendLocationName": "黑龙江省 齐齐哈尔市 富拉尔基区",              # 发货地 省+市+县
        "sendDetailAddress": "test_data_statistics",             # 发货详细地址
        "sendDate": "2019-09-26",                      # 发货时间 yyyy-MM-dd
        "sendTime": "22:00:00",                      # 发货时间段
        "sendTimeHour": "22:00-23:59",                  # 发货整点 发货时间段字典项的value(sendTime)
        "senderName": "test_data_statistics",                    # 发货人姓名
        "senderPhone": "15600000000",                   # 发货人手机号码
        "receiveOrg": "test_data_statistics",                    # 收货单位
        "receiveLocationPId": "4",            # 收货地省id
        "receiveLocationCId": "87",            # 收货地市id
        "receiveLocationAId": "",            # 收货地县区id
        "receiveLocationName": "重庆市 万州区",           # 收货地 省+市+县
        "receiveDetailAddress": "test_data_statistics",          # 收货详细地址
        "receiverTime": "2032-09-26",                  # 收货时间 yyyy-MM-dd
        "receiverName": "test_data_statistics",                  # 收货人姓名
        "receiverPhone": "15600000000",                 # 收货人手机号码

        "issueType": "1",                     # 发布类型(0是招标,1是指)

        "bidValidTime": "2019-09-30 16:50:42",                  # yyyy-MM-dd hh:mm:ss
        "expectedLoadMoney": "11",             # 预期运费金额 保留两位小数点
        "signatureRequirements": "需要",         # 签收单的要求
        "signatureRequirementsCode": "0",     # 签收单的要求code signatureRequirements字典项的value
        "ifInsurance": "1",                   # 是否投保
        "insuranceMoney": "11",                # 投保金额
        "loadPic1": pic,                      # 获取图片1 (可空)
        "loadPic2": "",                      # 获取图片2 (可空)
        "loadPic3": "",                      # 获取图片3 (可空)
        "loadPic4": "",                      # 获取图片4 (可空)
        "loadPic5": "",                      # 获取图片5 (可空)
        "carType": "平板",                       # 车型 (可空)
        "carLength": "6米",                     # 车厂 (可空)
        "remarks": "备注",                       # 备注 (可空)
        "ifInvoice": "1",                     # 是否需要发票(0否，1是) 需要发票时以下字段必填
        "invoiceType": "0",                   # 发票类型（0是普通发票，1是专用发票)
        "invoiceCompanyTitle": "发票抬头公司名称",           # 发票抬头公司名称
        "invoiceCompanyTaxNo": "纳税人识别号",           # 纳税人识别号
        "invoiceAddress": "单位地址",                # 单位地址
        "invoicePhone": "电话号码",                  # 电话号码
        "invoiceBank": "开户银行",                   # 开户银行
        "invoiceBankNo": "银行账号"                 # 银行账号
    }
}
json_datas = json.dumps(datas)

# 输出结果
result = requests.post(url=URL, headers=header, data=json_datas)

# 对比结果
r = result.text
print(r)
print(result.status_code)
baseju = baseJudge.BaseJudge('success', r)
baseju.judge()

