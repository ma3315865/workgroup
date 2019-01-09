# coding = utf-8
import time


class TimeProjectName(object):
    def __init__(self):
        self.customize_order_no = self.time_pro_date()[0]
        self.project_name = self.time_pro_date()[1]
        self.load_name = self.time_pro_date()[2]

    @staticmethod
    def time_pro_date():
        local_time = time.localtime()
        date_year = time.strftime('%y', local_time) + '年'
        date_month = time.strftime('%m', local_time) + '月'
        date_day = time.strftime('%d', local_time) + '日'
        date_hour = time.strftime('%H', local_time) + '时'
        date_min = time.strftime('%M', local_time) + '分'
        date_sec = time.strftime('%S', local_time) + '秒'
        date_name = date_year + date_month + date_day + date_hour + date_min + date_sec
        customize_order_no = '测试货主订单号' + date_name
        project_name = '测试项目名称' + date_name
        load_name = '测试品名' + date_name
        return customize_order_no, project_name, load_name


if __name__ == '__main__':
    main = TimeProjectName()
    print(main.customize_order_no)
    print(main.load_name)