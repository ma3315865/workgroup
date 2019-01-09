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
        p_dict = base.new_dict(type="2",            # 1 loginName密码登录 2 手机号密码登录 3 手机号验证码登录
                               loginName="",
                               phone="13400000000",
                               msgCode="",
                               password=password,
                               jpushId="",
                               jpushTag="")
        return base.post(b_dict, p_dict, self.type, self.num)

    @property
    def uid(self):
        uid = self.result["params"]["user"]["uid"]
        self.configer.set("info", "uid", uid)
        with open(self._path, "w+") as ini:
            self.configer.write(ini)
        return uid

    @property
    def token(self):
        token = self.result["params"]["user"]["token"]
        self.configer.set("info", "uid", token)
        with open(self._path, "w+") as ini:
            self.configer.write(ini)
        return token


if __name__ == '__main__':
    user = User()
    r = user.result
    print(r)