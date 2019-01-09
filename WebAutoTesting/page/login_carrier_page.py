# coding = utf-8
from tools import find_element
from selenium.common.exceptions import NoSuchElementException as ECelement
from selenium.webdriver.support.select import Select


class LoginPage(object):
    def __init__(self, driver, ini_path):
        self.driver = driver
        self.find_element = find_element.Element(self.driver, ini_path)

    def select_type(self, login_type):
        Select(self.ele_type_top).select_by_visible_text(login_type)

    @property
    def ele_type_top(self):
        return self.find_element.get_ele("login_carrier", "userTypetop")

    @property
    def ele_type_bottom(self):
        return self.find_element.get_ele("login_carrier", "userTypebottom")

    @property
    def ele_username(self):
        return self.find_element.get_ele("login_carrier", "username")

    @property
    def ele_password(self):
        return self.find_element.get_ele("login_carrier", "password")

    @property
    def ele_cod(self):
        return self.find_element.get_ele("login_carrier", "verificationCode")

    @property
    def ele_login_button(self):
        return self.find_element.get_ele("login_carrier", "btn")

    @property
    def cod_error(self):
        try:
            self.find_element.get_ele("login_carrier", "loginError")
            return True
        except ECelement:
            return False

    @property
    def wrapper_title(self):
        try:
            self.find_element.get_ele("login_carrier", "loginTitle")
            return True
        except ECelement:
            return False


if __name__ == '__main__':
    from tools import methods_driver
    test_url = "http://118.190.115.95:8086/jzt2_web/login.jsp"
    # path = r"D:\python\WebAutoTesting\config\LoginPageIni.ini"
    home_path = r"D:\MyPycharm\JztWebAutoTesting\config\LoginPageIni.ini"
    driver = methods_driver.BaseDriver().select_driver("chrome")
    test = LoginPage(driver, home_path)
    driver.get(test_url)
    print(test.ele_login_button)
    driver.quit()
