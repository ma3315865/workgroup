# coding = utf-8
import time
from page import wrapper_carrier_page
from frame.frame_handle_orders import FrameTabParent
from frame.frame_releasing import ReleaseOrdersFrame
from frame.frame_biding_central import FrameBidingCentral
from frame.frame_carrier_orders_handle import CarrierHandleOrders
import handle.handle_wrapper as wrapper
import handle.handle_frame_orders as handle_orders
import handle.handle_frame_releasing as release
import handle.handle_frame_biding_central as biding
import handle.handle_frame_carrier_orders as carrier_orders


class WrapperCarrier(object):
    def __init__(self, driver):
        self._driver = driver
        _pg_wrapper = wrapper_carrier_page.WrapperPage(self._driver)
        self.hd_wrapper = wrapper.HandleWrapper(_pg_wrapper)
        _frame_tab_parent = FrameTabParent(self._driver)
        self._fr_orders_parent = handle_orders.HandleFrameOrders(_frame_tab_parent)

    # noinspection PyBroadException
    def _check_dialog(self, func, msg):
        while True:
            try:
                self.hd_wrapper.switch_to_iframe()
                func()
                time.sleep(0.5)
                self._fr_orders_parent.decide_dialog_boolean(msg)
                self.hd_wrapper.switch_to_iframe()
            except Exception:
                print(msg)
                self.hd_wrapper.switch_to_iframe()
                self._fr_orders_parent.click_next_pager()
            else:
                self.hd_wrapper.switch_to_iframe()
                self._fr_orders_parent.click_dialog_close()
                time.sleep(0.5)
                break

    def _check_order(self, func, msg):
        func()
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.switch_to_layui_frame()
        self._fr_orders_parent.click_toggle_order()
        if self._fr_orders_parent.decide_order_info(msg):
            self.hd_wrapper.switch_to_parent_frame()
            self._fr_orders_parent.click_dialog_close()
            time.sleep(0.5)
        else:
            self._driver.save_screenshot("D:\python\WebAutoTesting\pic\\bi_check_order.png")
        self.hd_wrapper.switch_to_default_frame()

    def logout(self):
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.click_dropdown_menu()
        self.hd_wrapper.click_logout()

    def biding_central(self):
        frame_biding_central = FrameBidingCentral(self._driver)
        fr_biding = biding.HandleFrameBidingCentral(frame_biding_central)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.click_biding_central()
        self.hd_wrapper.switch_to_iframe()
        fr_biding.send()
        self._check_dialog(fr_biding.click_op_bid, "报价")
        self._check_dialog(fr_biding.click_op_view, "查看运单")
        self._driver.refresh()

    def releasing_order(self):
        frame_release_order = ReleaseOrdersFrame(self._driver)
        fr_release = release.HandleReleaseOrdersFrame(frame_release_order)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(0, 0)
        self.hd_wrapper.switch_to_iframe()
        fr_release.input()
        fr_release.send()
        fr_release.click()
        fr_release.release_order()
        if fr_release.dialog_boolean:
            fr_release.click_dialog()
        else:
            self._driver.save_screenshot("D:\python\WebAutoTesting\pic\\bi_releasing_order.png")
        self._driver.refresh()

    def handle_orders(self):
        frame_handle_order = CarrierHandleOrders(self._driver)
        fr_carrier_orders = carrier_orders.HandleCarrierOrders(frame_handle_order)
        self.hd_wrapper.switch_to_default_frame()
        self.hd_wrapper.iframe_click(0, 1)
        self.hd_wrapper.switch_to_iframe()
        num = 0
        while num <= 6:
            fr_carrier_orders.click_tab(num)
            fr_carrier_orders.input()
            if num <= 1:
                self.hd_wrapper.switch_to_iframe()
                fr_carrier_orders.click_op(num)
                fr_carrier_orders.click_view_order()
                fr_carrier_orders.decide_dialog_boolean("查看运单")
                fr_carrier_orders.click_dialog_close()
            else:
                self._check_order(fr_carrier_orders.click_view_order, "主运单号")
                self.hd_wrapper.switch_to_iframe()
            if num == 3 or num == 6:
                fr_carrier_orders.click_signed_receipt()
                self.hd_wrapper.switch_to_parent_frame()
                if fr_carrier_orders.decide_dialog_boolean("查看签收单"):
                    fr_carrier_orders.click_dialog_close()
                    time.sleep(0.5)
                self.hd_wrapper.switch_to_iframe()
            num += 1
