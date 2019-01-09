# coding = utf-8
from business import busi_login, busi_consignor_wrapper


def bills_payable():
    login = busi_login.Login()
    wrapper = busi_consignor_wrapper.WrapperConsignor(login.driver)
    login.main_consignor()
    wrapper.bills_payable()
    login.driver.quit()


if __name__ == '__main__':
    bills_payable()