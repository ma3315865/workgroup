# coding = utf-8
import traceback


# noinspection PyBroadException
class HandleBillsPayable(object):
    def __init__(self, frame):
        self._frame = frame
        self.order_num = "9F55100000001390"
        self.customize_num = "测试货主订单号"
        self.carrier_name = "TestCarrierCompany"
        self.gtedate = "2018-12-02"
        self.ltdate = "2023-12-25"

    def try_do(self, func):
        try:
            func()
        except Exception:
            self._frame.driver.save_screenshot('D:\python\WebAutoTesting\pic\\try_do_exception.png')
            traceback.print_exc()

    def send(self):
        self.check_send(self.send_order_num)
        self.check_send(self.send_customize_num)
        self.check_send(self.send_carrier_name)
        self.check_send(self.send_gtedate)
        self.check_send(self.send_ltdate)

    def check_send(self, func):
        self.try_do(func)
        self.click_search()
        if not self.find_nowrap_boolean():
            self._frame.driver.save_screenshot('D:\python\WebAutoTesting\pic\\check_send_exception.png')
        self.click_reset()
        self.click_search()

    def send_order_num(self):
        self._frame.ele_order_num.send_keys(self.order_num)

    def send_customize_num(self):
        self._frame.ele_customize_num.send_keys(self.customize_num)

    def send_carrier_name(self):
        self._frame.ele_carrier_name.send_keys(self.carrier_name)

    def send_gtedate(self):
        js = 'document.getElementsByName("search_gtedate_record.createDate")[0].removeAttribute("readonly")'
        self._frame.driver.execute_script(js)
        self._frame.ele_gtedate.clear()
        self._frame.ele_gtedate.send_keys(self.gtedate)

    def send_ltdate(self):
        js = 'document.getElementsByName("search_ltdate_record.createDate")[0].removeAttribute("readonly")'
        self._frame.driver.execute_script(js)
        self._frame.ele_ltdate.send_keys(self.ltdate)

    def find_nowrap_boolean(self):
        return self._frame.ele_nowrap.is_enabled()

    def click_search(self):
        self._frame.ele_search.click()

    def click_reset(self):
        self._frame.ele_reset.click()

    def click_prev_pager(self):
        self._frame.ele_prev_pager.click()

    def click_next_pager(self):
        self._frame.ele_next_pager.click()

    def click_order(self):
        self._frame.ele_order.click()

    def click_dialog_close(self):
        self._frame.ele_dialog_close.click()

    def decide_dialog_boolean(self, msg):
        return self._frame.dialog_text.find(msg) >= 0