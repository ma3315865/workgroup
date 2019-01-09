# coding = utf-8
import time
import traceback
from page import wrapper_consignor_page
from frame import frame_releasing
from frame import frame_handle_orders
from frame import frame_all_orders
from frame import frame_bills_payable
from frame import frame_bill_lists
from frame import frame_my_carrier
from frame import frame_carriers_warehouse
from frame import frame_release_info
from frame import frame_receive_info
from frame import frame_tax_info
import handle.handle_wrapper as wrapper
import handle.handle_frame_releasing as release
import handle.handle_frame_orders as handle_orders
import handle.handle_frame_all_orders as search_order
import handle.handle_frame_bills_payable as payable
import handle.handle_frame_bill_lists as bill_list
import handle.handle_frame_my_carrier as my_carrier
import handle.handle_frame_carriers_warehouse as carriers_warehouse
import handle.handle_frame_release_info as release_info
import handle.handle_frame_receive_info as receive_info
import handle.handle_frame_tax_info as tax_info


# noinspection PyBroadException
class WrapperConsignor(object):
    def __init__(self, driver):
        self._driver = driver
        pg_wrapper = wrapper_consignor_page.WrapperPage(self._driver)
        self.hd_wrapper = wrapper.HandleWrapper(pg_wrapper)

        release_frame = frame_releasing.ReleasingFrame(self._driver)
        self.fr_release = release.HandleReleaseFrame(release_frame)
        _frame_tab_parent = frame_handle_orders.FrameTabParent(self._driver)
        self.fr_orders_parent = handle_orders.HandleFrameOrders(_frame_tab_parent)

    # noinspection PyBroadException
    def _check_dialog(self, func, msg):
        while True:
            try:
                self.hd_wrapper.switch_to_iframe()
                func()
                time.sleep(0.5)
                self.fr_orders_parent.decide_dialog_boolean(msg)
                self.hd_wrapper.switch_to_iframe()
            except Exception:
                print(msg)
                self.hd_wrapper.switch_to_iframe()
                self.fr_orders_parent.click_next_pager()
            else:
                self.hd_wrapper.switch_to_iframe()
                self.fr_orders_parent.click_dialog_close()
                time.sleep(0.5)
                break

    def _check_order(self, func, msg):
        func()
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.switch_to_layui_frame()
        self.fr_orders_parent.click_toggle_order()
        if self.fr_orders_parent.decide_order_info(msg):
            self.hd_wrapper.switch_to_parent_frame()
            self.fr_orders_parent.click_dialog_close()
            time.sleep(1)
        else:
            self._driver.save_screenshot("D:\python\WebAutoTesting\pic\\bi_check_order.png")
        self.hd_wrapper.switch_to_default_frame()

    def _tab_page_0(self):
        _frame_tab_0 = frame_handle_orders.FrameTab0(self._driver)
        _fr_orders_0 = handle_orders.HandleFrameOrders(_frame_tab_0)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(0, 1)
        self.hd_wrapper.switch_to_iframe()
        _fr_orders_0.select_pagtab()
        _fr_orders_0.send()
        try:
            self._check_dialog(_fr_orders_0.click_op0_release, "确认要发布选中的记录么?")
            self._check_dialog(_fr_orders_0.click_op0_delete, "确认要删除选中的记录么?")
            _fr_orders_0.click_op0_edit()
            self.fr_release.back_order()
            _fr_orders_0.click_op0_copy()
            self.fr_release.back_order()
            _fr_orders_0.click_op0_view()
            self.fr_orders_parent.click_dialog_close()
        except Exception:
            traceback.print_exc()
            self._driver.save_screenshot("D:\python\WebAutoTesting\pic\\bi_tab_page_0.png")
        finally:
            self._driver.refresh()

    def _tab_page_1(self):
        _frame_tab_1 = frame_handle_orders.FrameTab1(self._driver)
        _fr_orders_1 = handle_orders.HandleFrameOrders(_frame_tab_1)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(0, 1)
        self.hd_wrapper.switch_to_iframe()
        _fr_orders_1.select_pagtab()
        _fr_orders_1.send()
        try:
            self._check_dialog(_fr_orders_1.click_op1_cancel, "确认要取消选中的运单吗?")
            self._check_dialog(_fr_orders_1.click_op1_add_exception, "加入异常")
            self._check_dialog(_fr_orders_1.click_op1_choosebid, "选择投标")
            self._check_dialog(_fr_orders_1.click_op1_pay_advance, "确认委托")
            self._check_order(_fr_orders_1.click_op1_order_num, "主运单号")
        except Exception:
            traceback.print_exc()
            self._driver.save_screenshot("D:\python\WebAutoTesting\pic\\bi_tab_page_1.png")
        finally:
            self._driver.refresh()

    def _tab_page_2(self):
        _frame_tab_2 = frame_handle_orders.FrameTab2(self._driver)
        _fr_orders_2 = handle_orders.HandleFrameOrders(_frame_tab_2)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(0, 1)
        self.hd_wrapper.switch_to_iframe()
        _fr_orders_2.select_pagtab()
        _fr_orders_2.send()
        try:
            self._check_dialog(_fr_orders_2.click_op2_add_exception, "加入异常")
            self._check_order(_fr_orders_2.click_op2_order_num, "主运单号")
        except Exception:
            traceback.print_exc()
            self._driver.save_screenshot("D:\python\WebAutoTesting\pic\\bi_tab_page_2.png")
        finally:
            self._driver.refresh()

    def _tab_page_3(self):
        _frame_tab_3 = frame_handle_orders.FrameTab3(self._driver)
        _fr_orders_3 = handle_orders.HandleFrameOrders(_frame_tab_3)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(0, 1)
        self.hd_wrapper.switch_to_iframe()
        _fr_orders_3.select_pagtab()
        _fr_orders_3.send()
        try:
            self._check_dialog(_fr_orders_3.click_op3_apprise_carrier, "评价承运商")
            # self._check_dialog(_fr_orders_3.click_op3_check_receipt, "查看签收单")
            _fr_orders_3.click_op3_check_receipt()
            self.hd_wrapper.switch_to_parent_frame()
            if _fr_orders_3.op3_decide_dialog_boolean("查看签收单"):
                self.fr_orders_parent.click_dialog_close()
            self._check_dialog(_fr_orders_3.click_op3_show_apprise, "查看评价")
            self._check_order(_fr_orders_3.click_op3_order_num, "主运单号")
        except Exception:
            traceback.print_exc()
            self._driver.save_screenshot("D:\python\WebAutoTesting\pic\\bi_tab_page_3.png")
        finally:
            self._driver.refresh()

    def _tab_page_4(self):
        _frame_tab_4 = frame_handle_orders.FrameTab4(self._driver)
        _fr_orders_4 = handle_orders.HandleFrameOrders(_frame_tab_4)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(0, 1)
        self.hd_wrapper.switch_to_iframe()
        _fr_orders_4.select_pagtab()
        _fr_orders_4.send()
        try:
            _fr_orders_4.click_op4_copy()
            self.fr_release.back_order()
            self._check_order(_fr_orders_4.click_op4_order_num, "主运单号")
        except Exception:
            traceback.print_exc()
            self._driver.save_screenshot("D:\python\WebAutoTesting\pic\\bi_tab_page_4.png")
        finally:
            self._driver.refresh()

    def _tab_page_5(self):
        _frame_tab_5 = frame_handle_orders.FrameTab5(self._driver)
        _fr_orders_5 = handle_orders.HandleFrameOrders(_frame_tab_5)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(0, 1)
        self.hd_wrapper.switch_to_iframe()
        _fr_orders_5.select_pagtab()
        _fr_orders_5.send()
        try:
            self._check_dialog(_fr_orders_5.click_op5_exception_reason, "查看异常原因")
            self._check_dialog(_fr_orders_5.click_op5_apprise_carrier, "评价承运商")
            _fr_orders_5.click_op5_signed_receipt()
            self.hd_wrapper.switch_to_parent_frame()
            if _fr_orders_5.op5_decide_dialog_boolean("查看签收单"):
                self.fr_orders_parent.click_dialog_close()
                time.sleep(0.5)
            self.hd_wrapper.switch_to_iframe()
            self._check_order(_fr_orders_5.click_op5_order_num, "主运单号")
        except Exception:
            traceback.print_exc()
            self._driver.save_screenshot("D:\python\WebAutoTesting\pic\\bi_tab_page_5.png")
        finally:
            self._driver.refresh()

    def logout(self):
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.click_dropdown_menu()
        self.hd_wrapper.click_logout()

    def releasing_order(self):
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(0, 0)
        self.hd_wrapper.switch_to_iframe()
        self.fr_release.input()
        self.fr_release.send()
        self.fr_release.click()
        self.fr_release.release_order()
        if self.fr_release.dialog_boolean:
            self.fr_release.click_dialog()
        else:
            self._driver.save_screenshot("D:\python\WebAutoTesting\pic\\bi_releasing_order.png")
        self._driver.refresh()

    def save_order(self):
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(0, 0)
        self.hd_wrapper.switch_to_iframe()
        self.fr_release.input()
        self.fr_release.send()
        self.fr_release.click()
        self.fr_release.save_order()
        if self.fr_release.dialog_boolean:
            self.fr_release.click_dialog()
        else:
            self._driver.save_screenshot("D:\python\WebAutoTesting\pic\\bi_save_order.png")
            self._driver.refresh()

    def back_order(self):
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(0, 0)
        self.hd_wrapper.switch_to_iframe()
        self.fr_release.back_order()
        self._driver.refresh()

    def handle_orders(self):
        self._tab_page_0()
        self._tab_page_1()
        self._tab_page_2()
        self._tab_page_3()
        self._tab_page_4()
        self._tab_page_5()

    def all_orders(self):
        _frame_search_order = frame_all_orders.FrameAllOrders(self._driver)
        _fr_search_order = search_order.HandleFrameAllOrders(_frame_search_order)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(0, 2)
        self.hd_wrapper.switch_to_iframe()
        _fr_search_order.send()
        try:
            _fr_search_order.click_order_num()
            self.hd_wrapper.switch_to_default_frame()
            self.hd_wrapper.switch_to_layui_frame()
            _fr_search_order.click_toggle_order()
            time.sleep(1)
            if _fr_search_order.decide_order_info("主运单号"):
                self.hd_wrapper.switch_to_parent_frame()
                _fr_search_order.click_dialog_close()
                time.sleep(1)
            else:
                self._driver.save_screenshot("D:\python\WebAutoTesting\pic\\bi_search_order.png")
        except Exception:
            traceback.print_exc()
        finally:
            self._driver.refresh()

    def bills_payable(self):
        _frame_bills_payable = frame_bills_payable.BillsPayable(self._driver)
        _fr_bills_payable = payable.HandleBillsPayable(_frame_bills_payable)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(1, 0)
        self.hd_wrapper.switch_to_iframe()
        _fr_bills_payable.send()
        time.sleep(1)
        try:
            _fr_bills_payable.click_order()
            if _fr_bills_payable.decide_dialog_boolean("查看运单"):
                _fr_bills_payable.click_dialog_close()
        except Exception:
            traceback.print_exc()
            self._driver.save_screenshot("D:\python\WebAutoTesting\pic\\bi_bills_payable.png")
        finally:
            self._driver.refresh()

    def bill_lists(self):
        _frame_bill_list = frame_bill_lists.BillLists(self._driver)
        _fr_bill_lists = bill_list.HandleFrameBillLists(_frame_bill_list)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(1, 1)
        self.hd_wrapper.switch_to_iframe()
        _fr_bill_lists.send()
        try:
            _fr_bill_lists.click_order_num()
            self.hd_wrapper.switch_to_default_frame()
            self.hd_wrapper.switch_to_layui_frame()
            _fr_bill_lists.click_toggle_order()
            time.sleep(1)
            if _fr_bill_lists.decide_order_info("主运单号"):
                self.hd_wrapper.switch_to_parent_frame()
                _fr_bill_lists.click_dialog_close()
            else:
                self._driver.save_screenshot("D:\python\WebAutoTesting\pic\\bi_bill_lists.png")
        except Exception:
            traceback.print_exc()
        finally:
            self._driver.refresh()

    def my_carrier(self):
        _frame_my_carrier = frame_my_carrier.MyCarrier(self._driver)
        _fr_my_carrier = my_carrier.HandleMyCarrier(_frame_my_carrier)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(2, 0)
        self.hd_wrapper.switch_to_iframe()
        _fr_my_carrier.send()
        try:
            self._check_dialog(_fr_my_carrier.click_remove, "确认要移除我的承运商吗?")
            self._check_dialog(_fr_my_carrier.click_op_view, "查看承运商")
        except Exception:
            traceback.print_exc()
        finally:
            self._driver.refresh()

    def carriers_warehouse(self):
        _frame_carriers_warehouse = frame_carriers_warehouse.CarriersWarehouse(self._driver)
        _fr_carriers_warehouse = carriers_warehouse.HandleCarriersWarehouse(_frame_carriers_warehouse)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(2, 1)
        self.hd_wrapper.switch_to_iframe()
        _fr_carriers_warehouse.send()
        try:
            self._check_dialog(_fr_carriers_warehouse.click_add, "确认要加入到我的承运商吗?")
            self._check_dialog(_fr_carriers_warehouse.click_op_view, "查看承运商")
        except Exception:
            traceback.print_exc()
        finally:
            self._driver.refresh()

    def release_info(self):
        _frame_release_info = frame_release_info.ReleaseInfo(self._driver)
        _fr_release_info = release_info.HandleReleaseInfo(_frame_release_info)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(3, 0)
        self.hd_wrapper.switch_to_iframe()
        _fr_release_info.send()
        try:
            self._check_dialog(_fr_release_info.click_op_edit, "编辑发货人信息")
            self._check_dialog(_fr_release_info.click_op_delete, "确认要删除选中的记录么?")
            self._check_dialog(_fr_release_info.click_icon_add, "添加发货人信息")
            self._check_dialog(_fr_release_info.click_icon_del, "确认要删除选中的记录么?")
            self._check_dialog(_fr_release_info.click_icon_edit, "编辑发货人信息")
        except Exception:
            traceback.print_exc()
        finally:
            self._driver.refresh()

    def receive_info(self):
        _frame_receive_info = frame_receive_info.ReceiveInfo(self._driver)
        _fr_receive_info = receive_info.HandleReceiveInfo(_frame_receive_info)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(3, 1)
        self.hd_wrapper.switch_to_iframe()
        _fr_receive_info.send()
        try:
            self._check_dialog(_fr_receive_info.click_op_edit, "编辑发货人信息")
            self._check_dialog(_fr_receive_info.click_op_delete, "确认要删除选中的记录么?")
            self._check_dialog(_fr_receive_info.click_icon_add, "添加发货人信息")
            self._check_dialog(_fr_receive_info.click_icon_del, "确认要删除选中的记录么?")
            self._check_dialog(_fr_receive_info.click_icon_edit, "编辑发货人信息")
        except Exception:
            traceback.print_exc()
        finally:
            self._driver.refresh()

    def tax_info(self):
        _frame_tax_info = frame_tax_info.TaxInfo(self._driver)
        _fr_tax_info = tax_info.HandleTaxInfo(_frame_tax_info)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(3, 2)
        self.hd_wrapper.switch_to_iframe()
        _fr_tax_info.send()
        try:
            self._check_dialog(_fr_tax_info.click_op_edit, "编辑发货人信息")
            self._check_dialog(_fr_tax_info.click_op_delete, "确认要删除选中的记录么?")
            self._check_dialog(_fr_tax_info.click_icon_add, "添加发货人信息")
            self._check_dialog(_fr_tax_info.click_icon_del, "确认要删除选中的记录么?")
            self._check_dialog(_fr_tax_info.click_icon_edit, "编辑发货人信息")
        except Exception:
            traceback.print_exc()
        finally:
            self._driver.refresh()

    def loop(self):
        self.save_order()
        self.handle_orders()
        self.all_orders()
        self.bills_payable()
        self.bill_lists()
        self.my_carrier()
        self.carriers_warehouse()
        self.release_info()
        self.receive_info()
        self.tax_info()