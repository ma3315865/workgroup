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
uri = '20014'
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
        "type": "2",                          # 1 招标中 2 已过期
        "title":"",                          # 货主公司名
        "sendLocationPId":"",                # 发货地省id(可为空)
        "sendLocationCId":"",                # 发货地市id(可为空)
        "sendLocationAId":"",	             # 发货地区县id(可为空)
        "receiveLocationPId":"",             # 收货地省id(可为空)
        "receiveLocationCId":"",             # 收货地市id(可为空)
        "receiveLocationAId":"",             # 收货地区县id(可为空)
        "sendDate": "",            # 发货日期 yyyy-MM-dd(可为空)
        "endDate": "",                       # (用于请求下一页数据)上次请求最后一条时间,请求这个时间点之后数据,第一次不带
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

