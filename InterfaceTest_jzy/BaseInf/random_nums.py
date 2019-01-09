# coding = utf-8
import uuid


class RandomNumb(object):
    @staticmethod
    def random_string(str_len):
        random = str(uuid.uuid4()).upper()
        random_str = random.replace("-", "")
        return random_str[0:str_len]