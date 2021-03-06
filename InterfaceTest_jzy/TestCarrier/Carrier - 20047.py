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
uri = '20047'
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
         "subOrderId": "fd454a09-d12c-11e8-bb03-00163e04a258",                 # 小订单ID
         "payMoney": "6",                     # 付款金额
         "payMode": "0",                      # 0余额 1支付宝 2微信 只能传0
         "password": "",                     # 密码 ras加密后的密码 (暂时不要)
         "rsaKeyID": rsaKeyID                     # rsaKeyID 告诉服务器用什么key解密 (暂时不要)
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

