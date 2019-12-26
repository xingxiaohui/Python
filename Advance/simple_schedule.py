"""
第三方模块实现的简单定时任务
"""
import schedule
import time
import datetime
import calendar


def job():
    print("job I'm working...")


def job1():
    print("job1 I'm working...")


def job2():
    print("job2 I'm working...")


# 设置定时计划
schedule.every(1).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

# 每分钟的第多少秒执行
schedule.every().minute.at(":17").do(job1)
schedule.every().minute.at(":18").do(job2)


chinese_map = {'1': '一', '2': '二', '3': '三', '4': '四', '5': '五', '6': '六', '7': '七', '8': '八', '9': '九',
               '10': '十', '11': '十一', '12': '十二', '13': '十三', '14': '十四', '15': '十五', '16': '十六',
               '17': '十七','18': '十八', '19': '十九', '20': '二十', '21': '二十一', '22': '二十二', '23': '二十三',
               '24': '二十四', '25': '二十五', '26': '二十六', '27': '二十七', '28': '二十八', '29': '二十九',
               '30': '三十'}


# 能够根据今天的日期生成对应问候语
def greetings():
    # 获取月份和日期
    month = datetime.datetime.now().strftime('%m')
    day = datetime.datetime.now().strftime('%d')
    # 获取每月的天数
    today = datetime.datetime.today()
    monthRange = calendar.monthrange(today.year, today.month)[1]
    
    day_str = '第' + chinese_map[day] + '天了'
    if day == monthRange:
        day_str = '最后一天了'
    greeting = '早上好啊，今天是' + chinese_map[month] + '月的' + day_str
    print(greeting)


schedule.every().day.at("08:00").do(greetings)


if __name__ == '__main__':
    # greetings()

    while True:
        schedule.run_pending()
        time.sleep(1)
