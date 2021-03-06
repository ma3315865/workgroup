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
pic = configer.common_pic()

# url
url = consignor_url
uri = '20005'
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
        "realname": "testMa",                      # 用户真实姓名
        "avatar": pic,                        # 用户真实照片
        "identityCardNo": "340000000000000000",                # 用户身份证号
        "companyName": "test_data_statistics",                   # 公司名称
        "companyPic": pic,                    # 公司营业执照照片地址
        "locationPId": "5",                   # 所在地省id
        "locationCId": "125",                   # 所在地市id
        "locationAId": "533",                   # 所在地区县id (可为空)
        "locationName": "安徽省合肥市高新区",                   # 省 + 市 + 县
        "locationAddress": "大学城",                # 具体地址
        "identityCardPhoto": "",             # 手持身份证照片
        "industry": "",                      # 所属行业
        "telephone": ""
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

