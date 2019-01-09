# coding : utf-8
import pymysql
import configparser


class GetToken(object):
    def __init__(self):
        self.host = '118.190.115.95'
        self.username = 'wangyuhui'
        self.password = 'WenshiAPP1'
        self.db_name = 'wenshi'
        # 创建游标
        self.config_file_path = 'D:\python\InterfaceTest_jzy\Config\config.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path)

    def consignor_token(self):
        conn = pymysql.connect(host=self.host, user=self.username, password=self.password, db=self.db_name)
        cursor = conn.cursor()
        get_consignor_token = "SELECT login_credentials FROM jzt2.uc_user_consignor WHERE phone = 13400000000"
        cursor.execute(get_consignor_token)
        consignor_token = cursor.fetchone()
        conn.close()
        return str(consignor_token).strip().strip('(,\')')

    def carrier_token(self):
        conn = pymysql.connect(host=self.host, user=self.username, password=self.password, db=self.db_name)
        cursor = conn.cursor()
        get_carrier_token = "SELECT login_credentials FROM jzt2.uc_user_carrier WHERE phone = 13400000000"
        cursor.execute(get_carrier_token)
        carrier_token = cursor.fetchone()
        conn.close()
        return str(carrier_token).strip().strip('(,\')')

    def driver_token(self):
        conn = pymysql.connect(host=self.host, user=self.username, password=self.password, db=self.db_name)
        cursor = conn.cursor()
        get_driver_token = "SELECT login_credentials FROM jzt2.uc_user_driver WHERE phone = 13400000000"
        cursor.execute(get_driver_token)
        driver_token = cursor.fetchone()
        conn.close()
        return str(driver_token).strip().strip('(,\')')

    def write_token(self):
        self.config.set('driver', 'driver_token', value=self.driver_token())
        self.config.set('carrier', 'carrier_token', value=self.carrier_token())
        self.config.set('consignor', 'consignor_token', value=self.consignor_token())
        self.config.write(open(self.config_file_path, "r+"))


if __name__ == '__main__':
    main = GetToken()
    main.write_token()
    print(main.consignor_token())
    print(main.carrier_token())
    print(main.driver_token())

