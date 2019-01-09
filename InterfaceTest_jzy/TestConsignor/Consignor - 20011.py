# coding : utf-8
import json
import requests
import configparser
from InterfaceTest_jzy.Config import read_config as con
from InterfaceTest_jzy.BaseInf import baseJudge

config = configparser.ConfigParser()
config.read('D:\python\InterfaceTest_jzy\Config\config.ini')
configer = con.TestFile(config)

uid = configer.consignor_uid()
token = configer.consignor_token()
consignor_url = configer.consignor_url()
rsaKeyID = configer.common_rsaKeyID()


# url
url = consignor_url
uri = '20011'
URL = url + uri

# header
header = {'Content-Type': 'application/json', 'XMLHttpRequest': 'X-Requested-With'}

# data
datas = {
    "base" : {
        "uid": uid,
        "token": token
    },
    "params": {
        "id": "",                            # 对象ID 重新编辑传值(可空)
        "organization": "test_data_statistics",                  # 单位名称
        "userName": "test_data_statistics",                      # 收发货人姓名
        "phone": "15600000000",                         # 联系方式
        "locationPId": "5",                   # 省
        "locationCId": "125",                   # 市
        "locationAId": "533",                   # 县 可为空
        "locationName": "安徽省合肥市高新区",                  # 省 + 市 + 县
        "locationAddress": "大学城",               # 详细地址
        "type": "1"                          # 类型 1 发货地址 2 收货地址
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

