# coding = utf-8
import traceback


# noinspection PyBroadException
class HandleFrameBillLists(object):
    def __init__(self, frame):
        self._frame = frame
        self.order_num = "9F55100000001390"
        self.customize_num = "测试货主订单号"

    def try_do(self, func):
        try:
            func()
        except Exception:
            self._frame.driver.save_screenshot('D:\python\WebAutoTesting\pic\\hd_try_bill_lists.png')
            traceback.print_exc()

    def send(self):
        self.check_send(self.send_order_num)
        self.check_send(self.send_customize_num)

    def check_send(self, func):
        self.try_do(func)
        self.click_search()
        if not self.find_nowrap_boolean():
            self._frame.driver.save_screenshot('D:\python\WebAutoTesting\pic\\hd_check_bill_list.png')
        self.click_reset()
        self.click_search()

    def send_order_num(self):
        self._frame.ele_order_num.send_keys(self.order_num)

    def send_customize_num(self):
        self._frame.ele_customize_num.send_keys(self.customize_num)

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

    def click_order_num(self):
        self._frame.ele_order.click()

    def click_dialog_close(self):
        self._frame.ele_dialog_close.click()

    def click_toggle_order(self):
        self._frame.ele_toggle_order.click()

    def decide_order_info(self, msg):
        return self._frame.order_info_text.find(msg) >= 0