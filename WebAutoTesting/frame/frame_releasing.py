# coding = utf-8
from tools import find_element, read_ini


class ReleasingFrame(object):
    def __init__(self, driver):
        path = r"D:\python\WebAutoTesting\config\ReleasingFrameIni.ini"
        self.driver = driver
        self.read = read_ini.ReadIni(path)
        self.element = find_element.Element(driver, path)

    def select_downbox(self, section, option):
        data_tuple = self.read.get_data_list(section, option)
        self.element.select_box(data_tuple[0], data_tuple[1], data_tuple[2], data_tuple[3])

    def eles_input(self, string_style):
        """
        :param string_style: 需要输入的类型num phone project test
        :return: element list
        """
        temp_list = []
        if string_style == "num":
            temp_list.extend(["expectedLoadMoney",
                              "singleSize",
                              "loadWeight",
                              "loadVolume",
                              "loadCount"])
        elif string_style == "phone":
            temp_list.extend(["senderPhone", "receiverPhone"])
        elif string_style == "project":
            temp_list.extend(["projectName", "customizeOrderNo", "loadName"])
        elif string_style == "test":
            temp_list.extend(["sendorg",
                              "sendername",
                              "senddetailaddress",
                              "receiveorg",
                              "receivername",
                              "receivedetailaddress",
                              "remarks"])
        else:
            print("输入的类型错误，仅为* num phone project test*")
        return self.element.get_ele_by_list("input", temp_list)

    def downbox_consignor(self):
        temp_list = self.read.get_options("downbox_consignor")
        for option in temp_list:
            self.select_downbox("downbox_consignor", option)

    def downbox_carrier(self):
        temp_list = self.read.get_options("downbox_carrier")
        for option in temp_list:
            self.select_downbox("downbox_carrier", option)

    def sendlocation_click(self):
        self.ele_sendaddress.click()
        bottom_ele_pid = self.element.get_ele("other", "sendLocationPId")
        self.element.action_click(bottom_ele_pid)
        bottom_ele_cid = self.element.get_ele("other", "sendLocationCId")
        self.element.action_click(bottom_ele_cid)
        bottom_ele_aid = self.element.get_ele("other", "sendLocationAId")
        self.element.action_click(bottom_ele_aid)

    def receivelocation_click(self):
        self.ele_receiveaddress.click()
        bottom_ele_pid = self.element.get_ele("other", "receiveLocationPId")
        self.element.action_click(bottom_ele_pid)
        bottom_ele_cid = self.element.get_ele("other", "receiveLocationCId")
        self.element.action_click(bottom_ele_cid)
        bottom_ele_aid = self.element.get_ele("other", "receiveLocationAId")
        self.element.action_click(bottom_ele_aid)

    @property
    def ele_sendaddress(self):
        return self.element.get_eles("click", "sendAddress")[0]

    @property
    def ele_receiveaddress(self):
        return self.element.get_eles("click", "receiveAddress")[1]

    @property
    def ele_bidvalid_time(self):
        js = 'document.getElementsByName("bidValidTime")[0].removeAttribute("readonly")'
        self.driver.execute_script(js)
        return self.element.get_ele("time", "bidValidTime")

    @property
    def ele_senddate_time(self):
        js = 'document.getElementsByName("sendDate")[0].removeAttribute("readonly")'
        self.driver.execute_script(js)
        return self.element.get_ele("time", "sendDate")

    @property
    def ele_receivertime_time(self):
        js = 'document.getElementsByName("receiverTime")[0].removeAttribute("readonly")'
        self.driver.execute_script(js)
        return self.element.get_ele("time", "receiverTime")

    @property
    def ele_invoice(self):
        return self.element.get_eles("click", "ifInvoice")

    @property
    def ele_insurance(self):
        return self.element.get_eles("click", "ifInsurance")

    @property
    def ele_attachment_path(self):
        js = 'document.getElementById("attachmentFilePath").removeAttribute("type")'
        self.driver.execute_script(js)
        return self.element.get_ele("send", "attachmentFilePath")

    @property
    def ele_image(self):
        return self.element.get_ele("send", "selectImage")

    @property
    def ele_save(self):
        return self.element.get_ele("other", "save_order")

    @property
    def ele_release(self):
        return self.element.get_ele("other", "release_order")

    @property
    def ele_back(self):
        return self.element.get_ele("other", "back")

    @property
    def ele_dialog(self):
        return self.element.get_ele("other", "dialog")

    @property
    def ele_dialog_yes(self):
        return self.element.get_ele("other", "dialog_yes")


class ReleaseOrdersFrame(ReleasingFrame):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def ele_remark_1(self):
        return self.element.get_eles("input", "remarks")[1]

    def sendlocation_click(self):
        self.ele_sendaddress.click()
        bottom_ele_pid = self.element.get_ele("other", "carrier_send_PId")
        self.element.action_click(bottom_ele_pid)
        bottom_ele_cid = self.element.get_ele("other", "carrier_send_CId")
        self.element.action_click(bottom_ele_cid)
        bottom_ele_aid = self.element.get_ele("other", "carrier_send_AId")
        self.element.action_click(bottom_ele_aid)

    def receivelocation_click(self):
        self.ele_receiveaddress.click()
        bottom_ele_pid = self.element.get_ele("other", "carrier_receive_PId")
        self.element.action_click(bottom_ele_pid)
        bottom_ele_cid = self.element.get_ele("other", "carrier_receive_CId")
        self.element.action_click(bottom_ele_cid)
        bottom_ele_aid = self.element.get_ele("other", "carrier_receive_AId")
        self.element.action_click(bottom_ele_aid)

    @property
    def ele_release(self):
        return self.element.get_ele("other", "save_order")