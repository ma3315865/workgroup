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
uri = '20004'
URL = url + uri

# header
header = {'Content-Type': 'application/json', 'XMLHttpRequest': 'X-Requested-With'}

# data
datas = {
    "base" : {
        "platform": "Android",                      # 平台 Android,IOS
        "deviceId": ""                       # 设备ID
    },
    "params": {
        "type": "3",                          # 1 loginName密码登录 2 手机号密码登录 3 手机号验证码登录
        "loginName": "",                     # 登录名
        "phone": "13400000000",                         # 手机号码
        "msgCode": "888888",                       # 短信验证码
        "password": "",                      # 密码 ras加密后的密码
        "rsaKeyID": rsaKeyID,                      # rsaKeyID 告诉服务器用什么key解密
        "jpushId": "jpushId",                       # jpush Id 登录更新jpush信息
        "jpushTag": "jpushTag"                       # jpush Tag
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

