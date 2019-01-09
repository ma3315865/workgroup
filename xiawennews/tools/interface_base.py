# coding = utf-8
import json
import requests


class BaseInterface(object):
    def __init__(self):
        self._base_dict = {}

    def post(self, base_dict, params_dict, style, num):
        """
        :param style: 接口类型
        :param num: 接口号
        :param base_dict: base后跟的一个字典项
        :param params_dict: params后跟的一个字典项
        :return: 接口返回的数据
        """
        _url = self._post_url(style, num)
        _body = self._base_body(base_dict, params_dict)
        res = requests.post(url=_url, headers=self._post_header, json=_body).text
        return eval(str(json.loads(res)))

    @staticmethod
    def zip_dict(list_0, list_1):
        return dict(zip(list_0, list_1))

    @staticmethod
    def new_dict(**kwargs):
        return kwargs

    @staticmethod
    def _post_url(style, interface_num):
        from tools import reader
        _info = reader.Reader()
        return _info.url + style + "/" + interface_num + _info.url_ver

    @property
    def _post_header(self):
        return {'Content-Type': 'application/json'}

    def _base_body(self, base_dict, params_dict):
        self._base_dict.update({"base": base_dict})
        self._base_dict.update({"params": params_dict})
        return self._base_dict


if __name__ == '__main__':
    b = BaseInterface()
    list0 = ["platform", "deviceId"]
    list1 = ["Android", ""]
    l0 = ["type", "loginName", "phone", "avatar", "msgCode", "password", "nickName", "sex", "jpushId", "jpushTag"]
    l1 = ["1", "", "", "", "", "", "", "", ""]
    dict0 = dict(zip(list0, list1))
    dict1 = dict(zip(l0, l1))
    r = b.post(dict0, dict1, "user", "10001")
    print(r["params"]["user"])


