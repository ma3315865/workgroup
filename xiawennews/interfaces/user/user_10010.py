# coding = utf-8
from tools.interface_base import BaseInterface


class User(object):
    def __init__(self):
        self.type = "user"
        self.num = "10010"

    def result(self):
        base = BaseInterface()
        b_dict = {}
        p_dict = base.new_dict(phone="13400000010")
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = User()
    r = user.result()
    print(r)