# coding = utf-8
from tools import find_element


class BillsPayable(object):
    def __init__(self, driver):
        self.driver = driver
        self.path = r"D:\python\WebAutoTesting\config\BillsPayableFrameIni.ini"
        self.element = find_element.Element(self.driver, self.path)

    @property
    def ele_order_num(self):
        return self.element.get_ele("send", "orderNo")

    @property
    def ele_customize_num(self):
        return self.element.get_ele("send", "customizeOrderNo")

    @property
    def ele_carrier_name(self):
        return self.element.get_ele("send", "carrierName")

    @property
    def ele_gtedate(self):
        return self.element.get_ele("send", "gtedate")

    @property
    def ele_ltdate(self):
        return self.element.get_ele("send", "ltdate")

    @property
    def ele_search(self):
        return self.element.get_ele("click", "search")

    @property
    def ele_reset(self):
        return self.element.get_ele("click", "reset")

    @property
    def ele_prev_pager(self):
        return self.element.get_ele("click", "prev_jqGridPager")

    @property
    def ele_next_pager(self):
        return self.element.get_ele("click", "next_jqGridPager")

    @property
    def ele_order(self):
        return self.element.get_ele("click", "orderNum")

    @property
    def ele_dialog_close(self):
        return self.element.get_eles("other", "dialog_close")[0]

    @property
    def dialog_text(self):
        return self.element.get_ele("other", "dialog_text").text

    @property
    def ele_nowrap(self):
        return self.element.get_ele("other", "nowrap")
