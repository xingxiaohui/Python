#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 正则表达式类库
import re

"""
Python 学习第六天 面向对象与正则表达式
"""


class User:
    type = "USER"

    def __init__(self, uid, username):
        self.uid = uid
        self.username = username

    def __repr__(self):
        return '  用户id:' + str(self.uid) + '  用户名:' + self.username


class Admin(User):
    type = "ADMIN"

    def __init__(self, uid, username, group):
        User.__init__(self, uid, username)
        self.group = group

    def __repr__(self):
        return '  用户名:' + self.username + '  用户uid:' + str(self.uid) + '  用户组:' + self.group


def demo_re():
    # 正则表达式
    # \d\D  数字 非数字
    # \s\S  空格 非空格
    # \w\W  单词(0-9,a-zzA-Z) 非单词
    # +  1次或1次以上
    # *  0次或0次以上
    # ?  0或1次
    # {num}  重复num次
    # | ^  或  取反
    # \\ 转义
    str1 = 'abcdef123456ghijkl78'
    pa = re.compile('[\d]+')
    pb = re.compile('[\d]')
    print(1, pa.findall(str1))
    print(2, pb.findall(str1))

    str2 = 'abc@163.com,15364@qq.com,def@outlok.com,678@qq.com,aaa@163.com'
    pc = re.compile('[\w]+@[163|qq]+\.com')
    print(3, pc.findall(str2))

    str3 = '<html><title>正则表达式</title><body>内容</body></html>'
    pd = re.compile('<title>[^<]+</title>')  # 包含全部匹配内容
    pf = re.compile('<title>([^<]+)</title><body>([^<]+)</body>')  # 仅包含括号中匹配的内容
    print(4, pd.findall(str3))
    print(4, pf.findall(str3))

    str4 = '创建日期：2019-12-13'
    pg = re.compile('[\d]{4}-[\d]{2}-[\d]{2}')
    print(5, pg.findall(str4))


if __name__ == '__main__':
    '''
    user = User(1111, '用户a')
    print(1, user)
    admin = Admin(1112, 'admin', '管理员')
    print(2, admin)
    '''
    demo_re()
