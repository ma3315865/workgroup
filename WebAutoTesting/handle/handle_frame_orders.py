# coding = utf-8
import traceback


# noinspection PyBroadException
class HandleFrameOrders(object):
    def __init__(self, frame):
        self._frame = frame
        self.project = "测试项目品名20181213134228"
        self.sendlocation = "安徽省"
        self.receivelocation = "河南"
        self.senddate = "2019-12-25"
        self.receivertime = "2023-12-25"

    def try_do(self, func):
        try:
            func()
        except Exception:
            self._frame.driver.save_screenshot('D:\python\WebAutoTesting\pic\\try_do_exception.png')
            traceback.print_exc()

    def select_pagtab(self):
        self._frame.ele_pagtab.click()

    def select_downbox(self):
        self.try_do(self._frame.select_downbox)

    def send(self):
        self.check_send(self.send_project)
        self.check_send(self.send_sendlocation)
        self.check_send(self.send_receivelocation)
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

    def send_senddate(self):
        self._frame.ele_send_date.send_keys(self.senddate)

    def send_receivertime(self):
        self._frame.ele_receiver_time.send_keys(self.receivertime)

    def find_nowrap_boolean(self):
        return self._frame.ele_nowrap.is_enabled()

    def click_search(self):
        self._frame.ele_btn_search.click()

    def click_reset(self):
        self._frame.ele_btn_reset.click()

    def click_prev_pager(self):
        self._frame.ele_prev_pager.click()

    def click_next_pager(self):
        self._frame.ele_next_pager.click()

    def click_dialog_yes(self):
        self._frame.ele_dialog_yes.click()

    def click_dialog_no(self):
        self._frame.ele_dialog_no.click()

    def click_dialog_close(self):
        self._frame.ele_dialog_close.click()

    def click_toggle_order(self):
        self._frame.ele_toggle_order.click()

    def decide_order_info(self, msg):
        return self._frame.order_info_text.find(msg) >= 0

    def decide_dialog_boolean(self, msg):
        return self._frame.dialog_text.find(msg) >= 0

    def click_op0_release(self):
        self.try_do(self._frame.ele_op0_release.click)

    def click_op0_edit(self):
        self.try_do(self._frame.ele_op0_edit.click)

    def click_op0_delete(self):
        self.try_do(self._frame.ele_op0_delete.click)

    def click_op0_copy(self):
        self.try_do(self._frame.ele_op0_copy.click)

    def click_op0_view(self):
        self.try_do(self._frame.ele_op0_view.click)

    def click_op1_cancel(self):
        self.try_do(self._frame.ele_op1_cancel.click)

    def click_op1_choosebid(self):
        self.try_do(self._frame.ele_op1_choosebid.click)

    def click_op1_add_exception(self):
        self.try_do(self._frame.ele_op1_add_exception.click)

    def click_op1_pay_advance(self):
        self.try_do(self._frame.ele_op1_pay_advance.click)

    def click_op1_order_num(self):
        self.try_do(self._frame.ele_op1_order_num.click)

    def click_op2_add_exception(self):
        self.try_do(self._frame.ele_op2_add_exception.click)

    def click_op2_order_num(self):
        self.try_do(self._frame.ele_op2_order_num.click)

    def click_op3_check_receipt(self):
        self.try_do(self._frame.ele_op3_check_signed_receipt.click)

    def click_op3_apprise_carrier(self):
        self.try_do(self._frame.ele_op3_apprise_carrier.click)

    def click_op3_show_apprise(self):
        self.try_do(self._frame.ele_op3_show_apprise_consignor.click)

    def click_op3_order_num(self):
        self.try_do(self._frame.ele_op3_order_num.click)

    def op3_decide_dialog_boolean(self, msg):
        return self._frame.ele_op3_dialog_text.find(msg) >= 0

    def click_op4_copy(self):
        self.try_do(self._frame.ele_op4_copy.click)

    def click_op4_order_num(self):
        self.try_do(self._frame.ele_op4_order_num.click)

    def click_op5_exception_reason(self):
        self.try_do(self._frame.ele_op5_show_exception_reason.click)

    def click_op5_signed_receipt(self):
        self.try_do(self._frame.ele_op5_check_signed_receipt.click)

    def click_op5_apprise_carrier(self):
        self.try_do(self._frame.ele_op5_apprise_carrier.click)

    def click_op5_order_num(self):
        self.try_do(self._frame.ele_op5_order_num.click)

    def op5_decide_dialog_boolean(self, msg):
        return self._frame.ele_op5_dialog_text.find(msg) >= 0
