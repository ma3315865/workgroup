# coding = utf-8
from tools.reader import Reader
from tools.interface_base import BaseInterface


class News(object):
    def __init__(self):
        self.type = "team"
        self.num = "10003"

    def result(self):
        base = BaseInterface()
        read = Reader()
        b_dict = base.new_dict(uid=read.uid,
                               token=read.token)
        p_dict = base.new_dict(tname="你好")
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = News()
    r = user.result()
    print(r)
