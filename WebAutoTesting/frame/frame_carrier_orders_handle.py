# coding = utf-8
from selenium.common.exceptions import NoSuchElementException
from frame.base_frame import BaseFrame
from tools import read_ini


class CarrierHandleOrders(BaseFrame):
    def __init__(self, driver):
        self.driver = driver
        self.path = r"D:\python\WebAutoTesting\config\CarrierOrdersHandleFrame.ini"
        super().__init__(self.driver, self.path)
        self._op_dict = self._option_dialog_dict()

    @staticmethod
    def _option_dialog_dict():
        msg_list = ["查看运单",
                    "查看异常原因",
                    "评价货主",
                    "查看评价",
                    "确认同意吗?",
                    "确认不同意吗?",
                    "确认删除运单吗?",
                    "发布子运单",
                    "确认同意取消运单吗?",
                    "确认不同意取消运单吗?",
                    "调整金额",
                    "确认同意调整运费吗?",
                    "确认不同意调整运费吗?",
                    "确认取消报价吗?",
                    "报价",
                    "确认要取消选中的运单吗?",
                    "选择投标",
                    "确认委托",
                    "运单",
                    "加入异常",
                    "异常",
                    "确认收货吗?",
                    "评价司机",
                    "查看评价",
                    "调整运费",
                    "确认费用"]
        options = ["viewOrder",
                   "showExceptionReason",
                   "appriseConsignor",
                   "showAppriseConsignor",
                   "agree",
                   "disagree",
                   "delete",
                   "release",
                   "agreeCancel",
                   "disagreeCancel",
                   "showAdjustMoney",
                   "agreeAdjustMoney",
                   "disagreeAdjustMoney",
                   "cancelBid",
                   "updateBid",
                   "cancel",
                   "chooseBid",
                   "payDeposit",
                   "edit",
                   "checkReport",
                   "addException",
                   "confirmReceipt",
                   "appriseDriver",
                   "showAppriseCarrier",
                   "adjustMoney",
                   "payBalance"]
        return dict(zip(msg_list, options))

    def msg_ele_dict(self, msg_list):
        ele_list = []
        for msg in msg_list:
            option = self._op_dict[msg]
            self.ele_first_pager.click()
            for page in range(self.pager_num):
                try:
                    ele = self.element.get_ele("op", option)
                    ele_list.append(ele)
                    break
                except NoSuchElementException:
                    self.ele_next_pager.click()
        return dict(zip(msg_list, ele_list))

    def ele_page_tab(self, num):
        ele_list = []
        option_list = read_ini.ReadIni(self.path).get_data_list("other", "pagetabs")
        for option in option_list[1:]:
            ele = self.element.select_element(option_list[0], option)
            ele_list.append(ele)
        return ele_list[num]

    def ele_signed_receipt(self):
        return self.element.get_ele("op", "checkSignedReceipt")

    def ele_view_order(self):
        return self.element.get_ele("op", "viewOrder")

    @property
    def ele_send_date(self):
        js = 'document.getElementsByName("search_indate_totalOrder.sendDate")[0].removeAttribute("readonly")'
        self.driver.execute_script(js)
        return self.element.get_ele("send", "sendDate")

    @property
    def ele_receiver_time(self):
        js = 'document.getElementsByName("search_indate_totalOrder.receiverTime")[0].removeAttribute("readonly")'
        self.driver.execute_script(js)
        return self.element.get_ele("send", "receiverTime")
