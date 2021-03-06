# coding = utf-8
from tools.reader import Reader
from tools.interface_base import BaseInterface


class User(object):
    def __init__(self):
        self.type = "user"
        self.num = "10018"

    def result(self):
        base = BaseInterface()
        read = Reader()
        b_dict = base.new_dict(uid=read.uid,
                               token=read.token)
        p_dict = base.new_dict(groupId="8325115",
                               endTime="2027-04-25 23:00",      # 投票截止时间 yyyy-MM-dd HH:mm 格式
                               title="投票标题",
                               opt1="选项一",
                               opt2="选项二")
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = User()
    r = user.result()
    print(r)