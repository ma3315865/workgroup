# coding : utf-8
from InterfaceTest_jzy.BaseInf import post_interfaces


class Consignor20000(object):
    def __init__(self, phone_num):
        """
        Consignor - 20000用户注册短信

        """
        self.intface = post_interfaces.PostInterface('Consignor', '20000')
        self.phone_num = phone_num

    def inter_datas(self):
        return {
            "base": {},
            "params": {
                "phone": self.phone_num  # 手机号码
            }
        }

    def interface_20000(self):
        return self.intface.get_result(self.inter_datas())


if __name__ == '__main__':
    phone = '11100000000'
    main = Consignor20000(phone)
    print(main.interface_20000().text)

