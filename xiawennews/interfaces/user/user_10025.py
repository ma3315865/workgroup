# coding = utf-8
from tools.reader import Reader
from tools.interface_base import BaseInterface


class User(object):
    def __init__(self):
        self.type = "user"
        self.num = "10025"

    def result(self):
        base = BaseInterface()
        read = Reader()
        b_dict = base.new_dict(uid=read.get("info", "temp_uid"),
                               token=read.get("info", "temp_token"))
        p_dict = base.new_dict(uniqueId="11110000",             # 第三方 id
                               origin="wechat")
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = User()
    r = user.result()
    print(r)