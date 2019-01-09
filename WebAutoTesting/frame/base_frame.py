# coding = utf-8
from tools import find_element


class BaseFrame(object):
    def __init__(self, driver, path):
        self.driver = driver
        self.path = path
        self.element = find_element.Element(self.driver, self.path)

    @property
    def ele_project(self):
        return self.element.get_ele("send", "projectName")

    @property
    def ele_send_location(self):
        return self.element.get_ele("send", "sendLocationName")

    @property
    def ele_receive_location(self):
        return self.element.get_ele("send", "receiveLocationName")

    @property
    def ele_send_date(self):
        js = 'document.getElementsByName("search_indate_sendDate")[0].removeAttribute("readonly")'
        self.driver.execute_script(js)
        return self.element.get_ele("send", "sendDate")

    @property
    def ele_receiver_time(self):
        js = 'document.getElementsByName("search_indate_receiverTime")[0].removeAttribute("readonly")'
        self.driver.execute_script(js)
        return self.element.get_ele("send", "receiverTime")

    @property
    def ele_btn_search(self):
        return self.element.get_ele("click", "search")

    @property
    def ele_btn_reset(self):
        return self.element.get_ele("click", "reset")

    @property
    def dialog_text(self):
        return self.element.get_eles("other", "dialog_text")[0].text

    @property
    def ele_dialog_yes(self):
        return self.element.get_eles("other", "dialog_yes")[0]

    @property
    def ele_dialog_no(self):
        return self.element.get_eles("other", "dialog_no")[0]

    @property
    def ele_dialog_close(self):
        return self.element.get_eles("other", "dialog_close")[0]

    @property
    def ele_nowrap(self):
        return self.element.get_ele("other", "nowrap")

    @property
    def ele_toggle_order(self):
        return self.element.get_ele("other", "dialog_toggle_oder")

    @property
    def order_info_text(self):
        return self.element.get_ele("other", "order_info").text

    @property
    def ele_prev_pager(self):
        return self.element.get_ele("click", "prev_jqGridPager")

    @property
    def ele_next_pager(self):
        return self.element.get_ele("click", "next_jqGridPager")

    @property
    def pager_num(self):
        return int(self.element.get_ele("other", "pagerNum").text)

    @property
    def ele_first_pager(self):
        return self.element.get_ele("other", "firstPager")

    def decide_order_info(self, msg):
        return self.order_info_text.find(msg) >= 0

    def decide_dialog_boolean(self, msg):
        return self.dialog_text.find(msg) >= 0