# coding = utf-8
from tools.reader import Reader
from tools.interface_base import BaseInterface


class News(object):
    def __init__(self):
        self.type = "news"
        self.num = "10013"

    def result(self):
        base = BaseInterface()
        read = Reader()
        b_dict = base.new_dict(uid=read.uid,
                               token=read.token)
        p_dict = base.new_dict(endDate="")                      # 上次请求最后一条时间,请求这个时间点之后数据,第一次不带
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = News()
    r = user.result()
    print(r)