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
uri = '20007'
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
        "title": "",                         # 公司名称/手机号码模糊查询(可为空)
        "locationPId": "",                   # 所在地省id(可为空)
        "locationCId": "",                   # 所在地市id(可为空)
        "locationAId": "",                   # 所在地区县id(可为空)
        "primaryPathFrom": "",               # 主营路线1（始发地）(可为空)
        "primaryPathTo": "",                 # 主营路线2（目的地）(可为空)
        "endDate": ""                       # (用于请求下一页数据)上次请求最后一条时间,请求这个时间点之后数据,第一次不带
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

