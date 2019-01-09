# coding : utf-8
import time
import configparser
from InterfaceTest_jzy.BaseInf import post_interfaces
from InterfaceTest_jzy.Config import read_config as con


class Driver20045(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('D:\python\InterfaceTest_jzy\Config\config.ini')
        configer = con.TestFile(config)
        self.intface = post_interfaces.PostInterface('Driver', '20045')
        self.uid = self.intface.post_uid()
        self.token = self.intface.post_token()
        self.pic = configer.common_pic()

    def inter_datas(self):
        return {
            "base": {
                "uid": self.uid,
                "token": self.token
            },
            "params": {
                "feedback": "测试反馈意见"  # 反馈意见
            }
        }

    def interface_20045(self):
        return self.intface.get_result(self.inter_datas())


if __name__ == '__main__':
    main = Driver20045()
    print(main.interface_20045().text)

