# coding = utf-8
from tools import find_element


class ReleaseInfo(object):
    def __init__(self, driver):
        self.driver = driver
        self.path = r"D:\python\WebAutoTesting\config\ReleaseInfoFrameIni.ini"
        self.element = find_element.Element(self.driver, self.path)

    @property
    def ele_organization(self):
        return self.element.get_ele("send", "organization")

    @property
    def ele_username(self):
        return self.element.get_ele("send", "userName")

    @property
    def ele_location_name(self):
        return self.element.get_ele("send", "locationName")

    @property
    def ele_op_edit(self):
        return self.element.get_ele("click", "op_edit")

    @property
    def ele_op_delete(self):
        return self.element.get_ele("click", "op_delete")

    @property
    def ele_cb_jqgrid(self):
        return self.element.get_ele("click", "cb_jqGrid")

    @property
    def ele_icon_add(self):
        return self.element.get_ele("click", "icon_add")

    @property
    def ele_icon_del(self):
        return self.element.get_ele("click", "icon_del")

    @property
    def ele_icon_edit(self):
        return self.element.get_ele("click", "icon_edit")

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
