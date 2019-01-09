# coding = utf-8
from business import busi_login, busi_carrier_wrapper


def check_carrier():
    login = busi_login.Login()
    wrapper = busi_carrier_wrapper.WrapperCarrier(login.driver)
    login.main_carrier()
    wrapper.handle_orders()
    login.driver.quit()


if __name__ == '__main__':
    check_carrier()