# coding = utf-8
from tools.interface_base import BaseInterface


class User(object):
    def __init__(self):
        self.type = "user"
        self.num = "10027"

    def result(self):
        base = BaseInterface()
        b_dict = base.new_dict(uid="812a0c13-0f2c-11e9-bb03-00163e04a258",
                               token="771c9e3b12ab9fea627ddcd19b0d1746")
        p_dict = {}
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = User()
    r = user.result()
    print(r)