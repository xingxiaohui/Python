"""
一个定时任务程序，交易日下午两点四十发送当日指数信息，提供投资参考
"""
import schedule
import time
import requests
import datetime
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

shangzheng_url = 'http://hq.sinajs.cn/list=s_sh000001'
shencheng_url = 'http://hq.sinajs.cn/list=s_sz399001'
xinzhai_url = 'http://data.eastmoney.com/xg/kzz/default.html/em_mutisvcexpandinterface/api/js/get?type=KZZ_LB2.0&token=70f12f2f4f091e459a279469fe49eca5'
shangzheng = []
shencheng = []


def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return str(data, encoding="unicode_escape")


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_email(shangzheng, shencheng, flag):
    from_addr = 'moe_noreply@163.com'
    password = 'moemoe961753'
    to_addr = '1559237979@qq.com'
    smtp_server = 'smtp.163.com'
    text = '投资邮件提醒：<br/>'
    if flag == 'zhishu':
        text += '<br/>&nbsp;&nbsp;&nbsp;&nbsp;今日上证指数：' + shangzheng[1] + '，涨跌值：' + shangzheng[2] + '，涨跌幅：' + shangzheng[3]+'<br/><br/>'
        text += '&nbsp;&nbsp;&nbsp;&nbsp;今日深成指数：' + shencheng[1] + '，涨跌值：' + shencheng[2] + '，涨跌幅：' + shencheng[3]
    if flag == 'xinzhai':
        text += '<br/>&nbsp;&nbsp;&nbsp;&nbsp;系统提醒您，今日有新的可转债申购，请您及时前往投资页面进行申购。<br/><br/>'
        text += '&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://data.eastmoney.com/xg/kzz/default.html">点此查看</a><br/><br/>'
        text += '&nbsp;&nbsp;&nbsp;&nbsp;或复制链接打开： http://data.eastmoney.com/xg/kzz/default.html'
    msg = MIMEText(text, 'HTML', 'utf-8')
    msg['From'] = _format_addr('投资提醒 <%s>' % from_addr)
    msg['To'] = _format_addr('投资者 <%s>' % to_addr)
    msg['Subject'] = Header('今日投资数据提醒', 'utf-8').encode()

    if float(shangzheng[3]) <= -0.8 or float(shencheng[3]) <= -0.8:
        server = smtplib.SMTP_SSL(smtp_server, 465)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()


def task():
    # 获取工作日
    daya = datetime.datetime.now().isoweekday()
    # 判断是否是交易日执行
    if daya <= 5:
        shangzheng = download_page(shangzheng_url).split(",")
        shencheng = download_page(shencheng_url).split(",")
        send_email(shangzheng, shencheng, 'zhishu')


def xinzhai_task():
    # 获取工作日
    daya = datetime.datetime.now().isoweekday()
    res = download_page(xinzhai_url)
    today = datetime.date.today()
    tag = '"STARTDATE":"'+today.strftime('%Y-%m-%d')
    # 判断是否是交易日执行
    if daya <= 5:
        if tag in res:
            send_email(shangzheng, shencheng, 'xinzhai')


# schedule.every().day.at("09:36").do(xinzhai_task)
schedule.every().day.at("14:50").do(task)


if __name__ == '__main__':
    # greetings()
    while True:
        schedule.run_pending()
        time.sleep(1)
