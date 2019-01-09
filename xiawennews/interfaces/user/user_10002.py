# coding = utf-8
from tools import reader
from tools.interface_base import BaseInterface


class User(object):
    def __init__(self):
        self.type = "user"
        self.num = "10002"

    def result(self):
        base = BaseInterface()
        uid = reader.Reader().get("info", "uid")
        token = reader.Reader().get("info", "token")
        b_dict = base.new_dict(uid=uid,
                               token=token)
        p_dict = base.new_dict(roomId="8325115",
                               target="10025",
                               optvalue="true")
        return base.post(b_dict, p_dict, self.type, self.num)


if __name__ == '__main__':
    user = User()
    r = user.result()
    print(r)