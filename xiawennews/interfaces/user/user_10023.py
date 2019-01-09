# coding = utf-8
from tools.interface_base import BaseInterface


class User(object):
    def __init__(self):
        self.type = "user"
        self.num = "10023"

    def result(self):
        base = BaseInterface()
        b_dict = base.new_dict(uid="bee3cb9a-0f27-11e9-bb03-00163e04a258",
                               token="f21680a975c49feedecd20d5cd7d294a")
        p_dict = base.new_dict(phone="15600000000",             # 第三方 id
                               msgCode="888888")
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = User()
    r = user.result()
    print(r)