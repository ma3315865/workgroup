# coding = utf-8
from tools.reader import Reader
from tools.interface_base import BaseInterface


class News(object):
    def __init__(self):
        self.type = "news"
        self.num = "10002"

    def result(self):
        base = BaseInterface()
        read = Reader()
        b_dict = base.new_dict(uid=read.uid,
                               token=read.token)
        p_dict = base.new_dict(newsChainId="",                              # 欲获取的新闻链ID
                               newsId="",                                   # 欲获取的新闻ID
                               levelId="",                                  # 欲获取的层级ID
                               menu="",                                     # 用户选择的菜单
                               options="[\"菜单一\", \"菜单二\"]",            # 所有菜单选项,符合JSON数组的字符串
                               trackingSeq="")                              # 服务端生成跟踪标识(请求层级不会重新生成)
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = News()
    r = user.result()
    print(r)