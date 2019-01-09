# coding : utf-8
from InterfaceTest_jzy.BaseInf import post_interfaces


class Common20000(object):
    def __init__(self):
        """
        Common - 20000 获取系统密码加密公钥

        """
        self.intface = post_interfaces.PostInterface('Common', '20000')

    @staticmethod
    def inter_datas():
        return {"base": {}, "params": {}}

    def interface_20000(self):
        return self.intface.get_result(self.inter_datas())


if __name__ == '__main__':
    main = Common20000()
    print(main.interface_20000().text)



