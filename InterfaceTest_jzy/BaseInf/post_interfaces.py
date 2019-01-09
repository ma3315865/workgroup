# coding = utf-8
import configparser
import json
import requests
from InterfaceTest_jzy.Config import read_config as con


class PostInterface(object):
    def __init__(self, release_kind, interface_num):
        self.interface_num = interface_num
        self.release_kind = release_kind
        self.config = configparser.ConfigParser()
        self.config.read('D:\python\InterfaceTest_jzy\Config\config.ini')
        self.configer = con.TestFile(self.config)

    def post_url(self):
        if self.release_kind is 'Consignor':
            post_url = self.configer.consignor_url() + self.interface_num
        elif self.release_kind is 'Carrier':
            post_url = self.configer.carrier_url() + self.interface_num
        elif self.release_kind is 'Driver':
            post_url = self.configer.driver_url() + self.interface_num
        elif self.release_kind is 'Common':
            post_url = self.configer.common_url() + self.interface_num
        else:
            print('输入的release类型不正确')
            post_url = ''
        return post_url

    def post_uid(self):
        if self.release_kind is 'Consignor':
            post_uid = self.configer.consignor_uid()
        elif self.release_kind is 'Carrier':
            post_uid = self.configer.carrier_uid()
        elif self.release_kind is 'Driver':
            post_uid = self.configer.driver_uid()
        else:
            print('输入的release类型不正确')
            post_uid = ''
        return post_uid

    def post_token(self):
        if self.release_kind is 'Consignor':
            post_token = self.configer.consignor_token()
        elif self.release_kind is 'Carrier':
            post_token = self.configer.carrier_token()
        elif self.release_kind is 'Driver':
            post_token = self.configer.driver_token()
        else:
            print('输入的release类型不正确')
            post_token = ''
        return post_token

    def get_result(self, data):
        js_url = self.post_url()
        post_head = {'Content-Type': 'application/json', 'XMLHttpRequest': 'X-Requested-With'}
        js_data = json.dumps(data)
        return requests.post(url=js_url, headers=post_head, data=js_data)


if __name__ == '__main__':
    main = PostInterface('consignor', '20053')
    uid = main.post_uid()
    token = main.post_token()
    datas = {
        "base": {
            "uid": uid,
            "token": token
        },
        "params": {
        }
    }
    result = main.get_result(datas)
    print(uid)
    print(token)
    print(result.text)