# coding = utf-8
from business import busi_login, busi_consignor_wrapper


def bill_lists():
    login = busi_login.Login()
    wrapper = busi_consignor_wrapper.WrapperConsignor(login.driver)
    login.main_consignor()
    wrapper.bill_lists()
    login.driver.quit()


if __name__ == '__main__':
    bill_lists()