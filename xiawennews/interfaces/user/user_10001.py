# coding = utf-8
import hashlib
from tools.interface_base import BaseInterface


class User(object):
    def __init__(self):
        self.type = "user"
        self.num = "10001"

    def result(self):
        base = BaseInterface()
        password = hashlib.md5(b'123456').hexdigest()
        b_dict = base.new_dict(platform="Android",
                               deviceId="")
        p_dict = base.new_dict(type="1",                # 1 临时用户 2 注册用户（2必须携带下面的参数）
                               loginName="",
                               phone="13400000009",
                               avatar="",
                               msgCode="888888",
                               password=password,
                               nickName="",
                               sex="",
                               jpushId="",
                               jpushTag="")
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = User()
    r = user.result()
    print(r)