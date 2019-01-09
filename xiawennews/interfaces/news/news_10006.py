# coding = utf-8
from tools.reader import Reader
from tools.interface_base import BaseInterface


class News(object):
    def __init__(self):
        self.type = "news"
        self.num = "10006"

    def result(self):
        base = BaseInterface()
        read = Reader()
        b_dict = base.new_dict(uid=read.uid,
                               token=read.token)
        p_dict = base.new_dict(hisId="34588e58-0fc4-11e9-bb03-00163e04a258")
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = News()
    r = user.result()
    print(r)