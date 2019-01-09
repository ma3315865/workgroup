# coding : utf-8
import time
import configparser
from InterfaceTest_jzy.BaseInf import post_interfaces
from InterfaceTest_jzy.Config import read_config as con


class Driver20042(object):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('D:\python\InterfaceTest_jzy\Config\config.ini')
        configer = con.TestFile(config)
        self.intface = post_interfaces.PostInterface('Driver', '20042')
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
                "subOrderId": "8b75c1c3-e979-11e8-bb03-00163e04a258",  # 小订单ID
                "content": "测试上报内容！",  # 上报内容
                "pic1": self.pic,  # 图片1
                "pic2": self.pic,  # 图片2
                "pic3": self.pic,  # 图片3
                "pic4": self.pic,  # 图片3
                "pic5": self.pic  # 图片3
            }
        }

    def interface_20042(self):
        return self.intface.get_result(self.inter_datas())


if __name__ == '__main__':
    main = Driver20042()
    print(main.interface_20042().text)
