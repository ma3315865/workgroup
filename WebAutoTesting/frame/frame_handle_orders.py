# coding = utf-8
from tools import find_element, read_ini


class FrameTabParent(object):
    def __init__(self, driver):
        self.driver = driver
        self.path = r"D:\python\WebAutoTesting\config\HandleOrdersFrameIni.ini"
        self.element = find_element.Element(self.driver, self.path)

    @property
    def ele_project(self):
        return self.element.get_ele("send", "projectName")

    @property
    def ele_send_location(self):
        return self.element.get_ele("send", "sendLocationName")

    @property
    def ele_receive_location(self):
        return self.element.get_ele("send", "receiveLocationName")

    @property
    def ele_send_date(self):
        js = 'document.getElementsByName("search_indate_sendDate")[0].removeAttribute("readonly")'
        self.driver.execute_script(js)
        return self.element.get_ele("send", "sendDate")

    @property
    def ele_receiver_time(self):
        js = 'document.getElementsByName("search_indate_receiverTime")[0].removeAttribute("readonly")'
        self.driver.execute_script(js)
        return self.element.get_ele("send", "receiverTime")

    @property
    def ele_btn_search(self):
        return self.element.get_ele("click", "search")

    @property
    def ele_btn_reset(self):
        return self.element.get_ele("click", "reset")

    @property
    def dialog_text(self):
        return self.element.get_eles("other", "dialog_text")[0].text

    @property
    def ele_dialog_yes(self):
        return self.element.get_eles("other", "dialog_yes")[0]

    @property
    def ele_dialog_no(self):
        return self.element.get_eles("other", "dialog_no")[0]

    @property
    def ele_dialog_close(self):
        return self.element.get_eles("other", "dialog_close")[0]

    @property
    def ele_nowrap(self):
        return self.element.get_ele("other", "nowrap")

    @property
    def ele_toggle_order(self):
        return self.element.get_ele("other", "dialog_toggle_oder")

    @property
    def order_info_text(self):
        return self.element.get_ele("other", "order_info").text

    @property
    def ele_prev_pager(self):
        return self.element.get_ele("click", "prev_jqGridPager")

    @property
    def ele_next_pager(self):
        return self.element.get_ele("click", "next_jqGridPager")


class FrameTab0(FrameTabParent):
    """
    0:待发布 1:待提货 2:在途中 3:已完成 4:已取消 5:异常运单
    """

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def ele_pagtab(self):
        """
        :return: 返回了一个element
                 0:待发布 1:待提货 2:在途中 3:已完成 4:已取消 5:异常运单
        """
        return self.element.get_eles("other", "pagetabs")[0]

    @property
    def ele_op0_release(self):
        return self.element.get_eles("click", "op0_release")[1]

    @property
    def ele_op0_edit(self):
        return self.element.get_eles("click", "op0_edit")[0]

    @property
    def ele_op0_delete(self):
        return self.element.get_eles("click", "op0_delete")[0]

    @property
    def ele_op0_copy(self):
        return self.element.get_eles("click", "op0_copy")[0]

    @property
    def ele_op0_view(self):
        return self.element.get_eles("click", "op0_view")[0]


class FrameTab1(FrameTabParent):
    """
    0:待发布 1:待提货 2:在途中 3:已完成 4:已取消 5:异常运单
    """

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def ele_pagtab(self):
        """
        :return: 返回了一个element
                 0:待发布 1:待提货 2:在途中 3:已完成 4:已取消 5:异常运单
        """
        return self.element.get_eles("other", "pagetabs")[1]

    def select_downbox(self):
        reader = read_ini.ReadIni(self.path)
        temp_tuple = reader.get_data_list("select", "hd1_search_eq_bizStatus")
        self.element.select_box(temp_tuple[0], temp_tuple[1], temp_tuple[2], temp_tuple[3])

    @property
    def ele_op1_cancel(self):
        return self.element.get_eles("click", "op1_cancel")[1]

    @property
    def ele_op1_choosebid(self):
        return self.element.get_eles("click", "op1_chooseBid")[0]

    @property
    def ele_op1_add_exception(self):
        return self.element.get_eles("click", "op1_addException")[0]

    @property
    def ele_op1_pay_advance(self):
        return self.element.get_eles("click", "op1_payAdvance")[0]

    @property
    def ele_op1_order_num(self):
        return self.element.get_eles("click", "op1_orderNum")[0]


class FrameTab2(FrameTabParent):
    """
    0:待发布 1:待提货 2:在途中 3:已完成 4:已取消 5:异常运单
    """

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def ele_pagtab(self):
        """
        :return: 返回了一个element
                 0:待发布 1:待提货 2:在途中 3:已完成 4:已取消 5:异常运单
        """
        return self.element.get_eles("other", "pagetabs")[2]

    def select_downbox(self):
        reader = read_ini.ReadIni(self.path)
        temp_tuple = reader.get_data_list("select", "hd2_search_eq_bizStatus")
        self.element.select_box(temp_tuple[0], temp_tuple[1], temp_tuple[2], temp_tuple[3])

    @property
    def ele_op2_add_exception(self):
        return self.element.get_eles("click", "op2_addException")[0]

    @property
    def ele_op2_order_num(self):
        return self.element.get_eles("click", "op2_orderNum")[0]


class FrameTab3(FrameTabParent):
    """
    0:待发布 1:待提货 2:在途中 3:已完成 4:已取消 5:异常运单
    """

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def ele_pagtab(self):
        """
        :return: 返回了一个element
                 0:待发布 1:待提货 2:在途中 3:已完成 4:已取消 5:异常运单
        """
        return self.element.get_eles("other", "pagetabs")[3]

    @property
    def ele_op3_check_signed_receipt(self):
        return self.element.get_eles("click", "op3_checkSignedReceipt")[0]

    @property
    def ele_op3_apprise_carrier(self):
        return self.element.get_eles("click", "op3_appriseCarrier")[0]

    @property
    def ele_op3_show_apprise_consignor(self):
        return self.element.get_eles("click", "op3_showAppriseConsignor")[0]

    @property
    def ele_op3_order_num(self):
        return self.element.get_eles("click", "op3_orderNum")[0]

    @property
    def ele_op3_dialog_text(self):
        return self.element.get_ele("other", "dialog_text").text


class FrameTab4(FrameTabParent):
    """
    0:待发布 1:待提货 2:在途中 3:已完成 4:已取消 5:异常运单
    """

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def ele_pagtab(self):
        """
        :return: 返回了一个element
                 0:待发布 1:待提货 2:在途中 3:已完成 4:已取消 5:异常运单
        """
        return self.element.get_eles("other", "pagetabs")[4]

    @property
    def ele_op4_copy(self):
        return self.element.get_eles("click", "op4_copy")[0]

    @property
    def ele_op4_order_num(self):
        return self.element.get_eles("click", "op4_orderNum")[0]


class FrameTab5(FrameTabParent):
    """
    0:待发布 1:待提货 2:在途中 3:已完成 4:已取消 5:异常运单
    """

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def ele_pagtab(self):
        """
        :return: 返回了一个element
                 0:待发布 1:待提货 2:在途中 3:已完成 4:已取消 5:异常运单
        """
        return self.element.get_eles("other", "pagetabs")[5]

    def select_downbox(self):
        reader = read_ini.ReadIni(self.path)
        temp_tuple = reader.get_data_list("select", "hd5_search_eq_bizStatus")
        self.element.select_box(temp_tuple[0], temp_tuple[1], temp_tuple[2], temp_tuple[3])

    @property
    def ele_op5_show_exception_reason(self):
        return self.element.get_eles("click", "op5_showExceptionReason")[0]

    @property
    def ele_op5_check_signed_receipt(self):
        return self.element.get_eles("click", "op5_checkSignedReceipt")[0]

    @property
    def ele_op5_apprise_carrier(self):
        return self.element.get_eles("click", "op5_appriseCarrier")[0]

    @property
    def ele_op5_order_num(self):
        return self.element.get_eles("click", "op5_orderNum")[0]

    @property
    def ele_op5_dialog_text(self):
        return self.element.get_ele("other", "dialog_text").text


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    test = FrameTabParent(driver)
    test1 = FrameTab1(test)
    print(isinstance(test1, FrameTab1))
    driver.quit()