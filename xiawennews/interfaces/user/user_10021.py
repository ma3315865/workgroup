# coding = utf-8
from tools.reader import Reader
from tools.interface_base import BaseInterface


class User(object):
    def __init__(self):
        self.type = "user"
        self.num = "10021"

    def result(self):
        base = BaseInterface()
        read = Reader()
        b_dict = base.new_dict(uid=read.uid,
                               token=read.token,
                               platform="Android",
                               deviceId="")
        p_dict = base.new_dict(uniqueId="123456",             # 第三方 id
                               origin="wechat",            # wechat weibo qq
                               jpushId="",
                               jpushTag="")
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = User()
    r = user.result()
    print(r)