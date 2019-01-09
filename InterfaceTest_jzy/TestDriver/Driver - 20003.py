# coding : utf-8
import json
import requests
import configparser
from InterfaceTest_jzy.Config import read_config as con
from InterfaceTest_jzy.BaseInf import baseJudge

config = configparser.ConfigParser()
config.read('D:\python\InterfaceTest_jzy\Config\config.ini')
configer = con.TestFile(config)

uid = configer.driver_uid()
token = configer.driver_token()
driver_url = configer.driver_url()
rsaKeyID = configer.common_rsaKeyID()


# url
url = driver_url
uri = '20003'
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
        "phone": "15600000010",                         # 手机号码
        "loginName": "test_data_statistics",                     # 登录名
        "msgCode": "8888",                       # 短信验证码
        "password": "123456",                       # 密码
        "rsaKeyID": rsaKeyID
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

