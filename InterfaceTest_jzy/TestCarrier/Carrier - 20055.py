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
uri = '20055'
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
        "msgCode": "888888",                       # 验证码
        "oldPassword": "",                   # 旧密码 
        "newPassword": "",                   # 新密码 
        "rsaKeyID": rsaKeyID                      # rsaKeyID 告诉服务器用什么key解密
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

