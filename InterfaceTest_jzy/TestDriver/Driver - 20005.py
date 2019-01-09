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


# url
url = driver_url
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
        "avatar": "test_data_statistics",                        # 用户头像
        "identityCardNo": "340000000000000000",                # 身份证号
        "driverLicensePic": "http://118.190.115.95/fs/carrierPic/20180905/ecb572b5-579e-4542-afa9-482e36ce51b7.jpg",              # 驾驶证照片
        "vehicleLicensePic": "http://118.190.115.95/fs/carrierPic/20180905/ecb572b5-579e-4542-afa9-482e36ce51b7.jpg",             # 行驶证照片
        "companyName": "test_data_statistics",                   # 车主 一个公司名称
        "carNo": "test_data_statistics",                         # 车牌号
        "carLength": "11",                     # 车长
        "carType": "test_data_statistics",                       # 车型
        "carPic": "http://118.190.115.95/fs/carrierPic/20180905/ecb572b5-579e-4542-afa9-482e36ce51b7.jpg",                        # 车的侧体图片
        "carLoadWeight": "",                 # 载重
        "productionDate": "",                # 出厂日期
        "familiarPathFrom": "上海市黄浦区",              # 常跑路线
        "familiarPathTo": "河北省石家庄市长安区",                # 常跑路线
        "locationCId": "",                   # 所在地市id
        "locationAId": "",                   # 所在地区县id (可为空)
        "locationName": "",                   # 省 + 市 + 县
        "locationAddress": "",
        "identityCardPhoto": "",             # 手持身份证照片
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

