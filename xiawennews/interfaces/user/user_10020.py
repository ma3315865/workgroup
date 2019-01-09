# coding = utf-8
from tools.reader import Reader
from tools.interface_base import BaseInterface


class User(object):
    def __init__(self):
        self.type = "user"
        self.num = "10020"

    def result(self):
        base = BaseInterface()
        read = Reader()
        b_dict = base.new_dict(uid=read.uid,
                               token=read.token)
        """
        type:1 跳过按钮
        type:2 验证码登录按钮
        type:3 日历入口
        type:4 组织入口
        type:5 闪聊入口
        type:6 收藏按钮
        type:7 分享按钮 
        type:8 日历分享
        type:9 AI点击数
        type:10 热点资讯
        """
        p_dict = base.new_dict(type="3")
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = User()
    r = user.result()
    print(r)