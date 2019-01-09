# coding = utf-8
from tools.reader import Reader
from tools.interface_base import BaseInterface


class News(object):
    def __init__(self):
        self.type = "news"
        self.num = "10023"

    def result(self):
        base = BaseInterface()
        read = Reader()
        b_dict = base.new_dict(uid=read.uid,
                               token=read.token)
        p_dict = base.new_dict(newsId="3c6cf4e2-0fed-11e9-bb03-00163e04a258",
                               trackingSeq="63405")
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = News()
    r = user.result()
    print(r)