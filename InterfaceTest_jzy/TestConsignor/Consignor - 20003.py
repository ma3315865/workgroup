# coding : utf-8
import configparser
from InterfaceTest_jzy.BaseInf import random_nums, password_methods
from InterfaceTest_jzy.TestConsignor import Consignor_20000
from InterfaceTest_jzy.BaseInf import post_interfaces
from InterfaceTest_jzy.Config import read_config as con


class Consignor20003(object):
    def __init__(self):
        """
        Consignor - 20003用户注册

        """
        config = configparser.ConfigParser()
        config.read('D:\python\InterfaceTest_jzy\Config\config.ini')
        configer = con.TestFile(config)
        self.intface = post_interfaces.PostInterface('Consignor', '20003')
        self.common_rsakeyid = configer.common_rsakeyid()
        self.password = password_methods.PassMethods()
        # 输入要发送短信的手机号
        self.phone = '11100000000'
        self.run_msg = Consignor_20000.Consignor20000(self.phone)

    def inter_datas(self):
        radom = random_nums.RandomNumb()
        random_string = radom.random_string(8)
        return {
            "base": {
                "platform": "Android",                      # 平台 Android,IOS
                "deviceId": "192.168.50.101:5555"                       # 设备ID
            },
            "params": {
                "phone": self.phone,                         # 手机号码
                "loginName": random_string,                     # 登录名
                "msgCode": "888888",                       # 短信验证码
                "password": self.password.pw_encrypt('123456'),                       # 密码
                "rsaKeyID": self.common_rsakeyid                       # rsaKeyID 告诉服务器用什么key解密
            }
        }

    def interface_20003(self):
        self.run_msg.interface_20000()
        return self.intface.get_result(self.inter_datas())


if __name__ == '__main__':
    main = Consignor20003()
    print(main.interface_20003().text)