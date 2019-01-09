# coding = utf-8
from tools.interface_base import BaseInterface


class User(object):
    def __init__(self):
        self.type = "user"
        self.num = "10022"

    def result(self):
        base = BaseInterface()
        b_dict = base.new_dict(platform="Android",
                               deviceId="")
        p_dict = base.new_dict(uniqueId="11110000",             # 第三方 id
                               origin="wechat",            # wechat weibo qq
                               phone="",
                               msgCode="",
                               jpushId="",
                               jpushTag="",
                               avatar="",
                               nickName="",
                               sex="0",
                               birthday="")
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = User()
    r = user.result()
    print(r)