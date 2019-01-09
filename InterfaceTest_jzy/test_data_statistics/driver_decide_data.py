# coding = utf-8
from InterfaceTest_jzy.BaseInf import post_interfaces


class DecideDriverDatas(object):
    def __init__(self):
        self.post_interface = post_interfaces.PostInterface('driver', '20044')

    def get_drvier_results(self):
        uid = self.post_interface.post_uid()
        token = self.post_interface.post_token()
        data = {
            "base": {
                "uid": uid,
                "token": token
            },
            "params": {
            }
        }
        results = self.post_interface.get_result(data)
        return results.text


if __name__ == '__main__':
    main = DecideDriverDatas()
    re = main.get_drvier_results()
    print(re)