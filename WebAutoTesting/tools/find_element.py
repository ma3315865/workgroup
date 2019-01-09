# coding = utf-8
from tools import methods_driver, read_ini
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class Element(object):
    def __init__(self, driver, ini_path):
        """
        :type driver select 传入driver即可
        :type ini_path 传入配置文件地址
        """
        self._reader = read_ini.ReadIni(ini_path)
        self.driver = driver

    def select_element(self, by_style, ele_value):
        by = str.lower(by_style)
        if by == "id":
            return self.driver.find_element_by_id(ele_value)
        elif by == "classname":
            return self.driver.find_element_by_class_name(ele_value)
        elif by == "name":
            return self.driver.find_element_by_name(ele_value)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(ele_value)
        elif by == "css":
            return self.driver.find_element_by_css_selector(ele_value)
        elif by == "tagname":
            return self.driver.find_element_by_tag_name(ele_value)
        elif by == "text":
            return self.driver.find_element_by_link_text(ele_value)
        elif by == "partial":
            return self.driver.find_element_by_partial_link_text(ele_value)
        else:
            print("输入的by为 %s ,输入的Element类型为 %s" % (by, ele_value))

    def select_elements(self, nod_by_style, nod_ele_value):
        nod_by = str.lower(nod_by_style)
        if nod_by == "id":
            return self.driver.find_elements_by_id(nod_ele_value)
        elif nod_by == "classname":
            return self.driver.find_elements_by_class_name(nod_ele_value)
        elif nod_by == "name":
            return self.driver.find_elements_by_name(nod_ele_value)
        elif nod_by == "xpath":
            return self.driver.find_elements_by_xpath(nod_ele_value)
        elif nod_by == "css":
            return self.driver.find_elements_by_css_selector(nod_ele_value)
        elif nod_by == "tagname":
            return self.driver.find_elements_by_tag_name(nod_ele_value)
        elif nod_by == "text":
            return self.driver.find_elements_by_link_text(nod_ele_value)
        elif nod_by == "partial":
            return self.driver.find_elements_by_partial_link_text(nod_ele_value)
        else:
            print("输入的by为 %s ,输入的Element类型为 %s" % (nod_by, nod_ele_value))

    @staticmethod
    def select_eles_by_ele(element, by_style, ele_value):
        by = str.lower(by_style)
        if by == "id":
            return element.find_elements_by_id(ele_value)
        elif by == "classname":
            return element.find_elements_by_class_name(ele_value)
        elif by == "name":
            return element.find_elements_by_name(ele_value)
        elif by == "xpath":
            return element.find_elements_by_xpath(ele_value)
        elif by == "css":
            return element.find_elements_by_css_selector(ele_value)
        elif by == "tagname":
            return element.find_elements_by_tag_name(ele_value)
        elif by == "text":
            return element.find_elements_by_link_text(ele_value)
        elif by == "partial":
            return element.find_elements_by_partial_link_text(ele_value)
        else:
            print("输入的by为 %s ,输入的Element类型为 %s" % (by, ele_value))

    def get_ele(self, section, option):
        """
        :param section: 配置文件节点
        :param option: 配置文件key
        :return: 返回一个element
        """
        i, j = self._reader.get_data(section, option)
        return self.select_element(i, j)

    def get_eles(self, section, option):
        """
        :param section: 配置文件节点
        :param option: 配置文件key
        :return: 返回一个elements，多个element
        """
        i, j = self._reader.get_data(section, option)
        return self.select_elements(i, j)

    def get_eles_by_ele(self, element, section, option):
        i, j = self._reader.get_data(section, option)
        return self.select_eles_by_ele(element, i, j)

    def get_ele_by_list(self, section, list):
        ele_list = []
        for option in list:
            i, j = self._reader.get_data(section, option)
            element = self.select_element(i, j)
            ele_list.append(element)
        return ele_list

    def select_box(self, by_style, ele_value, style, string):
        """
        :param style: 选择类型为三种 index， value， text
        :param string: 选择类型后，传入的值
        :return: 返回一个下拉框中隐藏的element并选择
        """
        webelement = self.select_element(by_style, ele_value)
        if str.lower(style) == "index":
            Select(webelement).select_by_index(string)
        elif str.lower(style) == "value":
            Select(webelement).select_by_value(string)
        elif str.lower(style) == "text":
            Select(webelement).select_by_visible_text(string)
        else:
            print("输入的by_style为 %s 输入的ele_value为 %s 输入的类型为 %s 输入的值为 %s" % (by_style, ele_value, style, string))

    def action_click(self, bottom_element):
        actions = ActionChains(self.driver)
        actions.click(bottom_element)
        actions.perform()

    @staticmethod
    def exist_boolean(get_ele_function):
        try:
            get_ele_function()
            return True
        except NoSuchElementException:
            return False


if __name__ == '__main__':
    url = "http://www.baidu.com"
    # path = r"D:\python\WebAutoTesting\config\LoginPageIni.ini"
    home_path = r"D:\MyPycharm\JztWebAutoTesting\config\LoginPageIni.ini"
    driver = methods_driver.BaseDriver().select_driver("chrome")
    test = Element(driver, home_path)
    driver.get(url)
    # test.driver.find_elements_by_class_name("mnav")[0].click()
    print(type(test.get_ele("test", "new")))
    Select(test.get_ele("test", "new")).deselect_by_value()
    test.driver.quit()