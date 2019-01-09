# coding : utf-8
import json
import requests
import configparser
from InterfaceTest_jzy.Config import read_config as con
from InterfaceTest_jzy.BaseInf import baseJudge


class InterfacesConsigor20053(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('D:\python\InterfaceTest_jzy\Config\config.ini')
        self.configer = con.TestFile(self.config)
        self.uid = self.configer.consignor_uid()
        self.token = self.configer.consignor_token()
        self.consignor_url = self.configer.consignor_url()
        self.rsaKeyID = self.configer.common_rsaKeyID()
        # url
        self._post_url = self.consignor_url + '20053'
        # header
        self._post_header = {'Content-Type': 'application/json', 'XMLHttpRequest': 'X-Requested-With'}
        # data
        self._datas = {
            "base": {
                "uid": self.uid,
                "token": self.token
            },
            "params": {
            }
        }

    def json_datas(self):
        return json.dumps(self._datas)

    def get_results(self):
        results = requests.post(url=self._post_url, headers=self._post_header, data=self.json_datas())
        return results

    def results_txt(self):
        return self.get_results().text

    def decide_result(self):
        print(self.results_txt())
        baseju = baseJudge.BaseJudge('success', self.get_results().text)
        baseju.judge()


if __name__ == '__main__':
    interface = InterfacesConsigor20053()
    interface.decide_result()