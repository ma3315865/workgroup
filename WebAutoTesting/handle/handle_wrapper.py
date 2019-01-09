# coding = utf-8
class HandleWrapper(object):
    def __init__(self, page):
        self.page = page

    def label_click(self, num):
        """
        :param num: 点击左侧大menu的index 从0开始计算列表
        """
        self.page.eles_side_menus[num].click()

    def click_dropdown_menu(self):
        self.page.ele_dropdown.click()

    def click_personal_info(self):
        self.page.ele_personal_info.click()

    def click_biding_central(self):
        self.page.ele_biding_central.click()

    def click_logout(self):
        self.page.ele_logout.click()

    def iframe_click(self, side_menu_num, sub_menu_num):
        """
        :param side_menu_num: 左侧可折叠大menu的index 0, 1, 2, 3
        :param sub_menu_num: menu下的label的index
        """
        self.label_click(side_menu_num)
        self.page.iframe_list(side_menu_num)[sub_menu_num].click()

    def switch_to_iframe(self):
        self.switch_to_default_frame()
        self.page.switch_to_frame("iframe")

    def switch_to(self, frame_name):
        self.page.switch_to_frame(frame_name)

    def switch_to_layui_frame(self):
        self.page.switch_to_frame(self.page.ele_layui_iframe)

    def switch_to_parent_frame(self):
        self.page.switch_to_parent_frame()

    def switch_to_default_frame(self):
        self.page.switch_to_default_frame()