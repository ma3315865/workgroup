# coding = utf-8
import configparser
from tools import reader
from tools.interface_base import BaseInterface


class User(object):
    def __init__(self):
        self.configer = configparser.ConfigParser()
        self._path = "D:\python\\xiawennews\config\InterfaceConfig.ini"
        self.configer.read(self._path)
        self.type = "user"
        self.num = "10008"

    @property
    def result(self):
        base = BaseInterface()
        read = reader.Reader()
        b_dict = base.new_dict(uid=read.uid,
                               token=read.token)
        p_dict = {}
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = User()
    r = user.result
    print(r)