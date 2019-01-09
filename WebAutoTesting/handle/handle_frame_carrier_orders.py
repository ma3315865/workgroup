# coding = utf-8
from selenium.common.exceptions import NoSuchElementException


# noinspection PyBroadException
class HandleCarrierOrders(object):
    def __init__(self, frame):
        self._frame = frame
        self.project = "测试项目品名2018"
        self.senddate = "2019-12-25"
        self.receivertime = "2023-12-25"
        self.sendlocation = "安徽省"
        self.receivelocation = "河南"

    def click_tab(self, num):
        self._frame.ele_page_tab(num).click()

    def check_send(self, func):
        func()
        self.click_search()
        if not self.find_nowrap_boolean():
            self._frame.driver.save_screenshot('D:\python\WebAutoTesting\pic\\check_send_exception.png')
        self.click_reset()
        self.click_search()

    def input(self):
        func_list = [self.send_project,
                     self.send_date,
                     self.send_receiver_time,
                     self.send_location,
                     self.send_receive_location]
        for func in func_list:
            try:
                self.check_send(func)
            except NoSuchElementException:
                continue

    def click_op(self, num):
        if num < 1:
            self.click_tab0_op()
        elif num < 2:
            self.click_tab1_op()
        elif num < 3:
            self.click_tab2_op()
        elif num < 4:
            self.click_tab3_op()
        elif num < 5:
            self.click_tab4_op()
        else:
            self.click_tab6_op()

    def click_tab0_op(self):
        tab_msg = ['查看运单',
                   '查看异常原因',
                   '评价货主',
                   '查看评价',
                   '确认同意吗?',
                   '确认不同意吗?',
                   '确认删除运单吗?',
                   '发布子运单',
                   '确认同意取消运单吗?',
                   '确认不同意取消运单吗?',
                   '调整金额',
                   '确认同意调整运费吗?',
                   '确认不同意调整运费吗?']
        self._click_dialog_by_msg(tab_msg)

    def click_tab1_op(self):
        tab_msg = ['查看运单', '发布子运单', '确认取消报价吗?', '报价', '确认删除运单吗?', '评价货主', '查看异常原因', '查看评价']
        self._click_dialog_by_msg(tab_msg)

    def click_tab2_op(self):
        tab_msg = ['确认要取消选中的运单吗?', '选择投标', '确认委托', '运单']
        self._click_dialog_by_msg(tab_msg)

    def click_tab3_op(self):
        tab_msg = ['加入异常', '异常', '确认收货吗?', '确认费用']
        self._click_dialog_by_msg(tab_msg)

    def click_tab4_op(self):
        tab_msg = ['评价司机', '查看评价', '异常']
        self._click_dialog_by_msg(tab_msg)

    def click_tab6_op(self):
        tab_msg = ['确认收货吗?', '确认费用', '调整运费', '查看异常原因', '评价司机', '查看评价']
        self._click_dialog_by_msg(tab_msg)

    def _click_dialog_by_msg(self, tab_msg):
        for msg in tab_msg:
            self._frame.msg_ele_dict(tab_msg)[msg].click()
            if self.decide_dialog_boolean(msg):
                self.click_dialog_close()

    def click_signed_receipt(self):
        self._frame.ele_signed_receipt.click()

    def click_view_order(self):
        self._frame.ele_view_order.click()

    def send_project(self):
        self._frame.ele_project.send_keys(self.project)

    def send_date(self):
        self._frame.ele_send_date.send_keys(self.senddate)

    def send_receiver_time(self):
        self._frame.ele_receiver_time.send_keys(self.receivertime)

    def send_location(self):
        self._frame.ele_send_location.send_keys(self.sendlocation)

    def send_receive_location(self):
        self._frame.ele_receive_location.send_keys(self.receivelocation)

    def click_search(self):
        self._frame.ele_btn_search.click()

    def click_reset(self):
        self._frame.ele_btn_reset.click()

    def click_prev_pager(self):
        self._frame.ele_prev_pager.click()

    def click_next_pager(self):
        self._frame.ele_next_pager.click()

    def click_first_page(self):
        self._frame.ele_first_pager.click()

    def click_dialog_close(self):
        self._frame.ele_dialog_close.click()

    def decide_order_info(self, msg):
        return self._frame.order_info_text.find(msg) >= 0

    def decide_dialog_boolean(self, msg):
        return self._frame.dialog_text.find(msg) >= 0

    def find_nowrap_boolean(self):
        return self._frame.ele_nowrap.is_enabled()