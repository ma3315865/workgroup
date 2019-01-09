# coding = utf-8
from tools.reader import Reader
from tools.interface_base import BaseInterface


class User(object):
    def __init__(self):
        self.type = "user"
        self.num = "10024"

    def result(self):
        base = BaseInterface()
        b_dict = {}
        p_dict = base.new_dict(phone="15600000000",
                               type="2")                        # 登录时绑定手机号传1 完善信息绑定手机号传2
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = User()
    r = user.result()
    print(r)