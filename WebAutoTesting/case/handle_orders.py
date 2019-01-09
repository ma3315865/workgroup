# coding = utf-8
from business import busi_login, busi_consignor_wrapper


def handle_orders():
    login = busi_login.Login()
    wrapper = busi_consignor_wrapper.WrapperConsignor(login.driver)
    login.main_consignor()
    wrapper.handle_orders()
    login.driver.quit()


if __name__ == '__main__':
    handle_orders()