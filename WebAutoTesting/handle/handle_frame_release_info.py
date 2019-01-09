# coding = utf-8
import traceback


# noinspection PyBroadException
class HandleReleaseInfo(object):
    def __init__(self, frame):
        self._frame = frame
        self.organization = "发货单位"
        self.username = "发货人"
        self.location = "安徽省"

    def try_do(self, func):
        try:
            func()
        except Exception:
            self._frame.driver.save_screenshot('D:\python\WebAutoTesting\pic\\hd_release_info_try_do.png')
            traceback.print_exc()

    def send(self):
        self.check_send(self.send_organization)
        self.check_send(self.send_username)
        self.check_send(self.send_location_name)

    def check_send(self, func):
        self.try_do(func)
        self.click_search()
        if not self.find_nowrap_boolean():
            self._frame.driver.save_screenshot('D:\python\WebAutoTesting\pic\\hd_release_info_check_send.png')
        self.click_reset()
        self.click_search()

    def send_organization(self):
        self._frame.ele_organization.send_keys(self.organization)

    def send_username(self):
        self._frame.ele_username.send_keys(self.username)

    def send_location_name(self):
        self._frame.ele_location_name.send_keys(self.location)

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