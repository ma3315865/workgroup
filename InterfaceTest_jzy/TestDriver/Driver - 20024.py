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
uri = '20024'
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
        "driverId": "9e273d0b-b1b4-11e8-bb03-00163e04a258",                      # 司机id
        "location1": "117.189118",                    # 坐标1LON 经度
        "location2": "31.831996",                     # 坐标2LAT 纬度
        "location3": "安徽省合肥市蜀山区望江西路3566号靠近云掌大厦"                       # 坐标3地址
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

