# coding = utf-8
import traceback


# noinspection PyBroadException
class HandleMyCarrier(object):
    def __init__(self, frame):
        self._frame = frame
        self.company_name = "TestCarrierCompany"
        self.location_name = "安徽省"
        self.primary_from = "安徽省"
        self.primary_to = "安徽省"

    def try_do(self, func):
        try:
            func()
        except Exception:
            self._frame.driver.save_screenshot('D:\python\WebAutoTesting\pic\\hd_try_do.png')
            traceback.print_exc()

    def send(self):
        self.check_send(self.send_company_name)
        self.check_send(self.send_location_name)
        self.check_send(self.send_primary_from)
        self.check_send(self.send_primary_to)

    def check_send(self, func):
        self.try_do(func)
        self.click_search()
        if not self.find_nowrap_boolean():
            self._frame.driver.save_screenshot('D:\python\WebAutoTesting\pic\\hd_my_carrier_check_send.png')
        self.click_reset()
        self.click_search()

    def send_company_name(self):
        self._frame.ele_company_name.send_keys(self.company_name)

    def send_location_name(self):
        self._frame.ele_location_name.send_keys(self.location_name)

    def send_primary_from(self):
        self._frame.ele_primary_from.send_keys(self.primary_from)

    def send_primary_to(self):
        self._frame.ele_primary_to.send_keys(self.primary_to)

    def find_nowrap_boolean(self):
        return self._frame.ele_nowrap.is_enabled()

    def click_remove(self):
        return self._frame.ele_op_remove.click()

    def click_op_view(self):
        return self._frame.ele_op_view.click()

    def click_search(self):
        self._frame.ele_search.click()

    def click_reset(self):
        self._frame.ele_reset.click()

    def click_prev_pager(self):
        self._frame.ele_prev_pager.click()

    def click_next_pager(self):
        self._frame.ele_next_pager.click()

    def click_dialog_close(self):
        self._frame.ele_dialog_close.click()

    def decide_dialog_boolean(self, msg):
        return self._frame.dialog_text.find(msg) >= 0