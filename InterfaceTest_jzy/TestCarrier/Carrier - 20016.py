# coding : utf-8
import json
import requests
import configparser
from InterfaceTest_jzy.Config import read_config as con
from InterfaceTest_jzy.BaseInf import baseJudge

config = configparser.ConfigParser()
config.read('D:\python\InterfaceTest_jzy\Config\config.ini')
configer = con.TestFile(config)

uid = configer.carrier_uid()
token = configer.carrier_token()
carrier_url = configer.carrier_url()
rsaKeyID = configer.common_rsaKeyID()


# url
url = carrier_url
uri = '20016'
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
        "type": "1",                         # 发票类型(0是普通发票，1是专用发票)
        "companyTitle": "test_data_statistics",                  # 发票抬头公司名称
        "companyTaxNo": "test_data_statistics",                  # 纳税人识别号
        "address": "test_data_statistics",                       # 地址
        "phone": "test_data_statistics",                         # 电话
        "bank": "test_data_statistics",                          # 开户行
        "bankNo": "test_data_statistics"                        # 账号
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

