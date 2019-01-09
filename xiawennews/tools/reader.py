# coding = utf -8
from tools import login
from configparser import ConfigParser


class Reader(object):
    def __init__(self):
        path = "D:\python\\xiawennews\config\InterfaceConfig.ini"
        self.login = login.User()
        self.configer = ConfigParser()
        self.configer.read(path)

    def get(self, section, option):
        return self.configer.get(section, option)

    @property
    def url(self):
        return self.configer.get("base", "url")

    @property
    def url_ver(self):
        return self.configer.get("base", "url_ver")

    @property
    def uid(self):
        return self.login.uid

    @property
    def token(self):
        return self.login.token
