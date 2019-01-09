# coding : utf-8
import traceback


# 判断是否正确
class BaseJudge(object):

    def __init__(self, input_str, result_str):
        self.input_str = input_str
        self.result_str = result_str

    def judge(self):
        if self.input_str not in self.result_str:
            print(traceback.print_exc())
        else:
            print("success")
