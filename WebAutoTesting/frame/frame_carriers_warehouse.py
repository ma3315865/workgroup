# coding = utf-8
from tools import find_element


class CarriersWarehouse(object):
    def __init__(self, driver):
        self.driver = driver
        self.path = r"D:\python\WebAutoTesting\config\CarriersWarehouseFrameIni.ini"
        self.element = find_element.Element(self.driver, self.path)

    @property
    def ele_company_name(self):
        return self.element.get_ele("send", "companyName")

    @property
    def ele_location_name(self):
        return self.element.get_ele("send", "locationName")

    @property
    def ele_primary_from(self):
        return self.element.get_ele("send", "primaryPathFrom")

    @property
    def ele_primary_to(self):
        return self.element.get_ele("send", "primaryPathTo")

    @property
    def ele_op_add(self):
        return self.element.get_ele("click", "op_add")

    @property
    def ele_op_view(self):
        return self.element.get_ele("click", "op_view")

    @property
    def ele_search(self):
        return self.element.get_ele("click", "search")

    @property
    def ele_reset(self):
        return self.element.get_ele("click", "reset")

    @property
    def ele_prev_pager(self):
        return self.element.get_ele("click", "prev_jqGridPager")

    @property
    def ele_next_pager(self):
        return self.element.get_ele("click", "next_jqGridPager")

    @property
    def ele_dialog_close(self):
        return self.element.get_eles("other", "dialog_close")[0]

    @property
    def dialog_text(self):
        return self.element.get_ele("other", "dialog_text").text

    @property
    def ele_nowrap(self):
        return self.element.get_ele("other", "nowrap")
