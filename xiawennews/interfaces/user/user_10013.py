# coding = utf-8
import hashlib
from tools.reader import Reader
from tools.interface_base import BaseInterface
from interfaces.user import user_10012


class User(object):
    def __init__(self):
        self.type = "user"
        self.num = "10013"

    def result(self):
        base = BaseInterface()
        read = Reader()
        user_10012.User().result()
        password = hashlib.md5(b"123456").hexdigest()
        b_dict = base.new_dict(uid=read.uid,
                               token=read.token)
        p_dict = base.new_dict(msgCode="888888",
                               password=password)
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = User()
    r = user.result()
    print(r)