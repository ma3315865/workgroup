# coding = utf-8
from InterfaceTest_jzy.BaseInf import write_decide_ini


class WriteIni(object):
    def __init__(self):
        self.wr = write_decide_ini.WriteDecideIni()

    def write_carrier(self):
        self.wr.write_carrier_ini()

    def write_consignor(self):
        self.wr.write_consignor_ini()


if __name__ == '__main__':
    main = WriteIni()
    # main.write_carrier()
    main.write_consignor()