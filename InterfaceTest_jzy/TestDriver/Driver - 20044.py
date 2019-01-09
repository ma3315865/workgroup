# coding : utf-8
import configparser
from InterfaceTest_jzy.BaseInf import post_interfaces


class Driver20044(object):
    def __init__(self):
        """
        添加接口注释

        """
        config = configparser.ConfigParser()
        config.read('D:\python\InterfaceTest_jzy\Config\config.ini')
        self.intface = post_interfaces.PostInterface('Driver', '20044')
        self.uid = self.intface.post_uid()
        self.token = self.intface.post_token()

    def inter_datas(self):
        return {
            "base": {
                "uid": self.uid,
                "token": self.token
            },
            "params": {
            }
        }

    def interface_20044(self):
        return self.intface.get_result(self.inter_datas())


if __name__ == '__main__':
    main = Driver20044()
    print(main.interface_20044().text)

