import requests
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

shangzheng_url = 'http://hq.sinajs.cn/list=s_sh000001'
shencheng_url = 'http://hq.sinajs.cn/list=s_sz399001'
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


def send_email(shangzheng, shencheng):
    from_addr = 'moe_noreply@163.com'
    password = 'moemoe961753'
    to_addr = '1559237979@qq.com'
    smtp_server = 'smtp.163.com'
    text = '今日上证指数：' + shangzheng[1] + '，涨跌值：' + shangzheng[2] + '，涨跌幅：' + shangzheng[3]+'<br/>'
    text += '今日深成指数：' + shencheng[1] + '，涨跌值：' + shencheng[2] + '，涨跌幅：' + shencheng[3]
    msg = MIMEText(text, 'HTML', 'utf-8')
    msg['From'] = _format_addr('指数自动提醒 <%s>' % from_addr)
    msg['To'] = _format_addr('投资者 <%s>' % to_addr)
    msg['Subject'] = Header('今日指数数据简报', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


if __name__ == '__main__':
    shangzheng = download_page(shangzheng_url).split(",")
    shencheng = download_page(shencheng_url).split(",")
    send_email(shangzheng, shencheng)
