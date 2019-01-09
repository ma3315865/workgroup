# coding = utf-8
import datetime


class TimeName(object):
    @staticmethod
    def time_to_string():
        time = datetime.datetime.now()
        return time.strftime("%Y%m%d%H%M%S")


if __name__ == '__main__':
    test = TimeName()
    print(test.time_to_string())