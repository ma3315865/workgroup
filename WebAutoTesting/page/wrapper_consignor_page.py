# coding = utf-8
from tools import find_element


class WrapperPage(object):
    def __init__(self, driver):
        ini_path = r"D:\python\WebAutoTesting\config\WrapperPageIni.ini"
        self.driver = driver
        self.element = find_element.Element(self.driver, ini_path)

    @property
    def eles_side_menus(self):
        """
        :return: 运单处理，开票管理，承运商管理，信息维护的element
        """
        return self.element.get_eles("wrapper_consignor", "side_menus")

    def iframe_list(self, side_menu_num):
        """
        :param side_menu_num: 左侧可折叠大menu的index 0, 1, 2, 3
        :return: 返回一个大menu下的列表
        """
        ele_list = []
        if side_menu_num < 1:
            for iframe_num in ("iframe0", "iframe1", "iframe2"):
                ele = self.element.get_ele("consignor_menu0", iframe_num)
                ele_list.append(ele)
        elif side_menu_num < 2:
            for iframe_num in ("iframe0", "iframe1"):
                ele = self.element.get_ele("consignor_menu1", iframe_num)
                ele_list.append(ele)
        elif side_menu_num < 3:
            for iframe_num in ("iframe0", "iframe1"):
                ele = self.element.get_ele("consignor_menu2", iframe_num)
                ele_list.append(ele)
        else:
            for iframe_num in ("iframe0", "iframe1", "iframe2"):
                ele = self.element.get_ele("consignor_menu3", iframe_num)
                ele_list.append(ele)
        return ele_list

    @property
    def ele_dropdown(self):
        return self.element.get_ele("wrapper_consignor", "dropdown")

    @property
    def _ele_dropdown_menu(self):
        return self.element.get_ele("wrapper_consignor", "dropdown_menu")

    @property
    def ele_personal_info(self):
        return self.element.get_eles_by_ele(self._ele_dropdown_menu, "wrapper_consignor", "personal_info")[0]

    @property
    def ele_logout(self):
        return self.element.get_eles_by_ele(self._ele_dropdown_menu, "wrapper_consignor", "logout")[0]

    @property
    def ele_layui_iframe(self):
        return self.element.get_ele("wrapper_consignor", "layui_layer_iframe")

    def switch_to_frame(self, frame):
        self.driver.switch_to.frame(frame)

    def switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()

    def switch_to_default_frame(self):
        self.driver.switch_to.default_content()


if __name__ == '__main__':
    from business import busi_login
    path = r"D:\python\WebAutoTesting\config\WrapperPageIni.ini"
    # home_path = r"D:\MyPycharm\JztWebAutoTesting\config\WrapperPageIni.ini"
    login = busi_login.Login()
    test = WrapperPage(login.driver)
    login.main_consignor()
    print(test.iframe_list(0))
    login.driver.quit()

