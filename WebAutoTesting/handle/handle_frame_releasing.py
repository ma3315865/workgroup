# coding = utf-8
import time
from pykeyboard import PyKeyboard
from tools import get_time_string


class HandleReleaseFrame(object):
    def __init__(self, frame):
        self._num = "12"
        self._phone = "15600000000"
        self._project = "测试项目品名"
        self._test = "test"
        self._bid_time = "2020-12-25 12:00:00"
        self._send_time = "2019-12-25"
        self._receiver_time = "2023-12-25"
        self._attachment_path = "temp/20181212/da19dffa-37c0-4f88-94b4-5c17988dd569.jpg"
        self._image_path = "D:\python\WebAutoTesting\pic\image.jpg"
        self._frame = frame

    def input(self):
        self._input_num()
        self._input_phone()
        self._input_project()
        self._input_test()
        self._input_bidvalid_time()
        self._input_senddate_time()
        self._input_receiver_time()

    def click(self):
        self._click_downbox()
        self._click_sendlocation()
        self._click_receivelocation()
        self._click_invoice()
        self._click_insurance()

    def send(self):
        self._send_attachment()
        self._send_image()

    def save_order(self):
        self._frame.ele_save.click()

    def release_order(self):
        self._frame.ele_release.click()

    def back_order(self):
        self._frame.ele_back.click()

    def _input_num(self):
        for ele in self._frame.eles_input("num"):
            ele.send_keys(self._num)

    def _input_phone(self):
        for ele in self._frame.eles_input("phone"):
            ele.send_keys(self._phone)

    def _input_project(self):
        time_data = get_time_string.TimeName().time_to_string()
        project = self._project + time_data
        for ele in self._frame.eles_input("project"):
            ele.send_keys(project)

    def _input_test(self):
        for ele in self._frame.eles_input("test"):
            ele.send_keys(self._test)

    def _input_bidvalid_time(self):
        self._frame.ele_bidvalid_time.send_keys(self._bid_time)

    def _input_senddate_time(self):
        self._frame.ele_senddate_time.send_keys(self._send_time)

    def _input_receiver_time(self):
        self._frame.ele_receivertime_time.send_keys(self._receiver_time)

    def _click_downbox(self):
        self._frame.downbox_consignor()

    def _click_sendlocation(self):
        self._frame.sendlocation_click()

    def _click_receivelocation(self):
        self._frame.receivelocation_click()

    def _click_invoice(self):
        self._frame.ele_invoice[1].click()

    def _click_insurance(self):
        self._frame.ele_insurance[1].click()

    def _send_attachment(self):
        self._frame.ele_attachment_path.send_keys(self._attachment_path)

    def _send_image(self):
        i = 0
        while i < 5:
            self._frame.ele_image.click()
            time.sleep(0.5)
            keyboard = PyKeyboard()
            keyboard.type_string(self._image_path)
            keyboard.press_key(keyboard.enter_key)
            i = i + 1

    @property
    def dialog_boolean(self):
        if self._frame.ele_dialog.text == "保存成功":
            return True
        else:
            return False

    def click_dialog(self):
        return self._frame.ele_dialog_yes.click()


class HandleReleaseOrdersFrame(HandleReleaseFrame):
    def __init__(self, frame):
        super().__init__(frame)
        self._frame = frame

    def send(self):
        self._send_image()

    def _input_test(self):
        for ele in self._frame.eles_input("test"):
            ele.send_keys(self._test)
        self._frame.ele_remark_1.send_keys("test")

    def _click_downbox(self):
        self._frame.downbox_carrier()