# coding = utf-8
import time
import threading
from selenium import webdriver
from frame import frame_handle_orders
from selenium.webdriver.support.select import Select


class Test(threading.Thread):
    def run(self):
        print("ssssssss")

    def func0(self):
        for i in range(10):
            print("aaa")

    def func1(self):
        for i in range(5):
            print("bbb")

    def main(self):
        pass


if __name__ == '__main__':
    test = Test()
    test.start()
