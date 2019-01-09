# coding = utf-8
import traceback
from handle import handle_login
from page import login_consignor_page, login_carrier_page
from tools import get_time_string as time
from tools import methods_driver


# noinspection PyBroadException
class Login(object):
    def __init__(self):
        test_url = "http://118.190.115.95:8086/jzt2_web/login.jsp"
        _path = r"D:\python\WebAutoTesting\config\LoginPageIni.ini"
        self.driver = methods_driver.BaseDriver().select_driver("chrome")
        _consignor_page = login_consignor_page.LoginPage(self.driver, _path)
        self._consignor_handle = handle_login.HandleLoginPage(_consignor_page)
        _carrier_page = login_carrier_page.LoginPage(self.driver, _path)
        self._carrier_handle = handle_login.HandleLoginPage(_carrier_page)
        self.driver.get(test_url)

    def try_do(self, fuc):
        time_str = time.TimeName().time_to_string()
        _except_pic = "D:\screenshot\\" + time_str + ".png"
        try:
            fuc()
        except Exception:
            self.driver.save_screenshot(_except_pic)
            self.driver.quit()
            traceback.print_exc()

    def loop_consignor(self):
        self.try_do(self._consignor_handle.input_cod)
        self.try_do(self._consignor_handle.select_consignor)
        self.try_do(self._consignor_handle.input_username)
        self.try_do(self._consignor_handle.input_password)
        self.try_do(self._consignor_handle.click_login)

    def main_consignor(self):
        while True:
            if self._consignor_handle.wrapper_display:
                break
            elif self._consignor_handle.login_error:
                self.loop_consignor()
            else:
                self.loop_consignor()

    def loop_carrier(self):
        self.try_do(self._carrier_handle.input_cod)
        self.try_do(self._carrier_handle.select_carrier)
        self.try_do(self._carrier_handle.input_username)
        self.try_do(self._carrier_handle.input_password)
        self.try_do(self._carrier_handle.click_login)

    def main_carrier(self):
        while True:
            if self._carrier_handle.wrapper_display:
                break
            elif self._carrier_handle.login_error:
                self.loop_carrier()
            else:
                self.loop_carrier()


if __name__ == '__main__':
    test = Login()
    test.main_consignor()
    test.driver.quit()