# coding = utf-8
from business import busi_login


def login_consignor():
    login = busi_login.Login()
    login.main_consignor()
    login.driver.quit()


def login_carrier():
    login = busi_login.Login()
    login.main_carrier()
    login.driver.quit()


if __name__ == '__main__':
    login_consignor()
    login_carrier()