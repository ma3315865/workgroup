# coding = utf-8
import time
import traceback
from business import busi_login, busi_consignor_wrapper


# noinspection PyBroadException
def releasing_order():
    login = busi_login.Login()
    wrapper = busi_consignor_wrapper.WrapperConsignor(login.driver)
    try:
        login.main_consignor()
        time.sleep(2)
        wrapper.releasing_order()
        time.sleep(2)
    except Exception:
        login.driver.save_screenshot("D:\python\WebAutoTesting\pic\case_exception.png")
        traceback.print_exc()


if __name__ == '__main__':
    releasing_order()