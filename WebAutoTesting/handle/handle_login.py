# coding = utf-8
class HandleLoginPage(object):
    def __init__(self, page):
        self.page = page
        self.type_consignor = "货主"
        self.type_carrier = "承运商"
        self.username = "13400000000"
        self.password = "123456"

    def select_consignor(self):
        self.page.select_type(self.type_consignor)

    def select_carrier(self):
        self.page.select_type(self.type_carrier)

    def input_username(self):
        self.page.ele_username.send_keys(self.username)

    def input_password(self):
        self.page.ele_password.send_keys(self.password)

    def input_cod(self):
        input_str = input("输入验证码\n")
        self.page.ele_cod.send_keys(input_str)

    def click_login(self):
        self.page.ele_login_button.click()

    @property
    def login_error(self):
        return self.page.cod_error

    @property
    def wrapper_display(self):
        return self.page.wrapper_title


if __name__ == '__main__':
    from tools import methods_driver
    from page import login_consignor_page
    test_url = "http://118.190.115.95:8086/jzt2_web/login.jsp"
    path = r"D:\MyPycharm\JztWebAutoTesting\config\LoginPageIni.ini"
    driver = methods_driver.BaseDriver().select_driver("chrome")
    driver.get(test_url)
    page = login_consignor_page.LoginPage(driver, path)
    test = HandleLoginPage(page)
    test.click_login()
    driver.quit()