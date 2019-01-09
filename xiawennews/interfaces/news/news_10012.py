# coding = utf-8
from tools.reader import Reader
from tools.interface_base import BaseInterface


class News(object):
    def __init__(self):
        self.type = "news"
        self.num = "10012"

    def result(self):
        base = BaseInterface()
        read = Reader()
        b_dict = base.new_dict(uid=read.uid,
                               token=read.token)
        p_dict = base.new_dict(target="47f91035-05cd-11e8-b048-00163e04a258",                           # 收藏对象ID
                               type="3",                            # 1 新闻 2 最热新闻 3 最新新闻
                               trackingSeq="")                      # 收藏新闻,需要携带,用于生成静态页面
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = News()
    r = user.result()
    print(r)