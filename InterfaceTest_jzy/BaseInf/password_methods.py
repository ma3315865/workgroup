# coding = utf-8
import ast
import base64
import configparser
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
from InterfaceTest_jzy.TestCommon import Common_20000


class PassMethods(object):
    def __init__(self):
        self.config_file_path = 'D:\python\InterfaceTest_jzy\Config\config.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path)
        common = Common_20000.Common20000()
        common_str = common.interface_20000().text
        self.common_results = ast.literal_eval(common_str)

    def get_rsaid(self):
        rsaid_str = self.common_results.get('data').get('rsaKeyID')
        return rsaid_str

    def get_rsakey(self):
        rsakey_str = self.common_results.get('data').get('rsaKey')
        return base64.b64decode(rsakey_str)

    def write_rsaid(self):
        self.config.set('common', 'common_rsakeyid', self.get_rsaid())
        self.config.write(open(self.config_file_path, "r+"))

    # 加密 python只可以用PKCS1加密，java用的是PKCS8
    def pw_encrypt(self, msg):
        self.write_rsaid()
        msg_byt = msg.encode(encoding='utf-8')
        pub_key = RSA.import_key(self.get_rsakey())
        # cipher = PKCS1_OAEP.new(pub_key)
        cipher = PKCS1_v1_5.new(pub_key)
        cipher_encrypt = cipher.encrypt(msg_byt)
        password_byt = base64.b64encode(cipher_encrypt)
        return password_byt.decode('utf-8')


if __name__ == '__main__':
    main = PassMethods()
    print(main.pw_encrypt('123456'))
