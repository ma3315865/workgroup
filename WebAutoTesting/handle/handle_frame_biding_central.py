# coding = utf-8
import traceback


# noinspection PyBroadException
class HandleFrameBidingCentral(object):
    def __init__(self, frame):
        self._frame = frame
        self.project = "测试项目品名2018"
        self.sendlocation = "安徽省"
        self.receivelocation = "河南"
        self.sendaddress = "test"
        self.senddate = "2019-12-25"
        self.receivertime = "2023-12-25"

    def try_do(self, func):
        try:
            func()
        except Exception:
            self._frame.driver.save_screenshot('D:\python\WebAutoTesting\pic\\try_do_exception.png')
            traceback.print_exc()

    def send(self):
        self.check_send(self.send_project)
        self.check_send(self.send_sendlocation)
        self.check_send(self.send_receivelocation)
        self.check_send(self.send_sendaddress)
        self.check_send(self.send_senddate)
        self.check_send(self.send_receivertime)

    def check_send(self, func):
        self.try_do(func)
        self.click_search()
        if not self.find_nowrap_boolean():
            self._frame.driver.save_screenshot('D:\python\WebAutoTesting\pic\\check_send_exception.png')
        self.click_reset()
        self.click_search()

    def send_project(self):
        self._frame.ele_project.send_keys(self.project)

    def send_sendlocation(self):
        self._frame.ele_send_location.send_keys(self.sendlocation)

    def send_receivelocation(self):
        self._frame.ele_receive_location.send_keys(self.receivelocation)

    def send_sendaddress(self):
        self._frame.ele_send_address.send_keys(self.sendaddress)

    def send_senddate(self):
        self._frame.ele_send_date.send_keys(self.senddate)

    def send_receivertime(self):
        self._frame.ele_receiver_time.send_keys(self.receivertime)

    def find_nowrap_boolean(self):
        return self._frame.ele_nowrap.is_enabled()

    def click_op_bid(self):
        self._frame.ele_op_bid.click()

    def click_op_view(self):
        self._frame.ele_op_view.click()

    def click_search(self):
        self._frame.ele_btn_search.click()

    def click_reset(self):
        self._frame.ele_btn_reset.click()

    def click_prev_pager(self):
        self._frame.ele_prev_pager.click()

    def click_next_pager(self):
        self._frame.ele_next_pager.click()

    def click_dialog_close(self):
        self._frame.ele_dialog_close.click()

    def decide_order_info(self, msg):
        return self._frame.order_info_text.find(msg) >= 0

    def decide_dialog_boolean(self, msg):
        return self._frame.dialog_text.find(msg) >= 0