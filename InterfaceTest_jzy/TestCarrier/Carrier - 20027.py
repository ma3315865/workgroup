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
uri = '20027'
URL = url + uri
# header
header = {'Content-Type': 'application/json', 'XMLHttpRequest': 'X-Requested-With'}

# data
quo = '[{"carLength": "5米",' \
      '"carType": "高栏",' \
      '"carCount": "1", ' \
      '"carMoney": "12"}]'


datas = {
    "base" : {
        "uid": uid,
        "token": token
    },
    "params": {
        "biddingId": "7f85d387-c3c5-11e8-bb03-00163e04a258",                     # 招标记录ID
        "taxRate": "0",                       # 税率
        "bidMoney": "12",                      # 总金额
        "quoteList": quo
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

