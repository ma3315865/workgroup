# coding = utf-8
import hashlib
import configparser
from tools.interface_base import BaseInterface


class User(object):
    def __init__(self):
        self.configer = configparser.ConfigParser()
        self._path = "D:\python\\xiawennews\config\InterfaceConfig.ini"
        self.configer.read(self._path)
        self.type = "user"
        self.num = "10007"

    @property
    def result(self):
        password = hashlib.md5(b'123456').hexdigest()
        base = BaseInterface()
        b_dict = base.new_dict(platform="Android",
                               deviceId="")
        p_dict = base.new_dict(type="3",            # 1 loginName密码登录 2 手机号密码登录 3 手机号验证码登录
                               loginName="",
                               phone="13400000001",
                               msgCode="888888",
                               password=password,
                               jpushId="",
                               jpushTag="")
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = User()
    r = user.result
    print(r)