# coding = utf-8
from selenium import webdriver


class BaseDriver(object):
    @staticmethod
    def select_driver(browser_sty):
        """

        :rtype:
        """
        global bro_driver
        if str.lower(browser_sty) == "chrome":
            bro_driver = webdriver.Chrome()
        elif str.lower(browser_sty) == "firefox":
            bro_driver = webdriver.Firefox()
        elif str.lower(browser_sty) == "ie":
            bro_driver = webdriver.Ie()
        else:
            print("请输入正确的driver类型,输入的方式为 %s" % browser_sty)
        bro_driver.implicitly_wait(0.1)
        bro_driver.maximize_window()
        return bro_driver


if __name__ == '__main__':
    test = BaseDriver()
    url = "http://www.baidu.com"
    driver = test.select_driver("chrome")
    driver.get(url)
    driver.find_element().click()
    driver.quit()