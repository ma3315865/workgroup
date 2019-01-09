# coding = utf-8
from tools import find_element


class FrameAllOrders(object):
    def __init__(self, driver):
        self.driver = driver
        self.path = r"D:\python\WebAutoTesting\config\AllOrdersFrameIni.ini"
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
    def ele_order_num(self):
        return self.element.get_eles("click", "orderNum")[0]

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