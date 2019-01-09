# coding : utf-8
class TestFile:
    def __init__(self, config):
        self.config = config

    def common_rsakeyid(self):
        common_rsakeyid = self.config.get("common", "common_rsakeyid")
        return common_rsakeyid

    def common_url(self):
        common_url = self.config.get("common", "common_url")
        return common_url

    def common_pic(self):
        common_pic = self.config.get("common", "common_pic")
        return common_pic

    def driver_url(self):
        driver_url = self.config.get("driver", "driver_url")
        return driver_url

    def driver_uid(self):
        driver_uid = self.config.get("driver", "driver_uid")
        return driver_uid

    def driver_token(self):
        driver_token = self.config.get("driver", "driver_token")
        return driver_token

    def driver_biddingId(self):
        driver_biddingId = self.config.get("driver", "driver_biddingId")
        return driver_biddingId

    def carrier_url(self):
        carrier_url = self.config.get("carrier", "carrier_url")
        return carrier_url

    def carrier_uid(self):
        carrier_uid = self.config.get("carrier", "carrier_uid")
        return carrier_uid

    def carrier_token(self):
        carrier_token = self.config.get("carrier", "carrier_token")
        return carrier_token

    def consignor_url(self):
        consignor_url = self.config.get("consignor", "consignor_url")
        return consignor_url

    def consignor_uid(self):
        consignor_uid = self.config.get("consignor", "consignor_uid")
        return consignor_uid

    def consignor_token(self):
        consignor_token = self.config.get("consignor", "consignor_token")
        return consignor_token

    def consignor_goods_uri(self):
        consignor_goods_uri = self.config.get("consignor", "consignor_goods_rui")
        return consignor_goods_uri
