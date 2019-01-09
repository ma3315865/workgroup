# coding = utf-8
import configparser


class ReadIni(object):
    # _default_path = r"D:\python\WebAutoTesting\config\LoginPageIni.ini"

    def __init__(self, ini_path):
        """
        :param ini_path: 为配置文件绝对路径
        """
        self.config = configparser.ConfigParser()
        self.config.read(ini_path, encoding="utf-8")

    def get_data(self, section, option):
        """
        :param section: section为[]内部变量
        :param option: option为=前变量
        :return: 返回为一个元祖，需要两个数据接收
        """
        raw_list = self.config.get(section, option).split(">")
        return raw_list[0], raw_list[1]

    def get_data_list(self, section, option):
        """
        :param section: section为[]内部变量
        :param option: option为=前变量
        :return: 返回为一个列表,用于两个以上数据读取
        """
        return list(self.config.get(section, option).split(">"))

    def get_options(self, section):
        return self.config.options(section)
