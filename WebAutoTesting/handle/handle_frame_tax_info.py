# coding = utf-8
import traceback


# noinspection PyBroadException
class HandleTaxInfo(object):
    def __init__(self, frame):
        self._frame = frame
        self.company_title = "danweitest"
        self.tax_num = "shibiehaotest"

    def try_do(self, func):
        try:
            func()
        except Exception:
            self._frame.driver.save_screenshot('D:\python\WebAutoTesting\pic\\hd_tax_info_try_do.png')
            traceback.print_exc()

    def send(self):
        self.check_send(self.send_company_title)
        self.check_send(self.send_tax_num)

    def check_send(self, func):
        self.try_do(func)
        self.click_search()
        if not self.find_nowrap_boolean():
            self._frame.driver.save_screenshot('D:\python\WebAutoTesting\pic\\hd_tax_info_check_send.png')
        self.click_reset()
        self.click_search()

    def send_company_title(self):
        self._frame.ele_company_title.send_keys(self.company_title)

    def send_tax_num(self):
        self._frame.ele_tax_num.send_keys(self.tax_num)

    def find_nowrap_boolean(self):
        return self._frame.ele_nowrap.is_enabled()

    def _click_jqgrid(self):
        if not self._frame.ele_cb_jqgrid.is_selected():
            self._frame.ele_cb_jqgrid.click()

    def click_op_edit(self):
        return self._frame.ele_op_edit.click()

    def click_op_delete(self):
        return self._frame.ele_op_delete.click()

    def click_icon_add(self):
        self._click_jqgrid()
        self._frame.ele_icon_add.click()

    def click_icon_del(self):
        self._click_jqgrid()
        self._frame.ele_icon_del.click()

    def click_icon_edit(self):
        self._click_jqgrid()
        self._frame.ele_icon_edit.click()

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