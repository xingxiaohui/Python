"""
Flask_Script 学习
Flask Script扩展提供向Flask插入外部脚本的功能，包括运行一个开发用的服务器，一个定制的Python shell，
设置数据库的脚本，cronjobs，及其他运行在web应用之外的命令行任务；使得脚本和系统分开；
Flask Script和Flask本身的工作方式类似，只需定义和添加从命令行中被Manager实例调用的命令；
官方文档：http://flask-script.readthedocs.io/en/latest/
"""
from flask_script import Manager
from Advance import flask_demo
manager = Manager(flask_demo)


# 可以在本插件中自定义命令
# 通过在控制台使用 python manage.py command_demo xxx 来调用
@manager.command
def command_demo(name):
    print('hello' + name)


# 初始化数据库
@manager.command
def initialize_database():
    '初始化数据库'
    print('初始化数据库')


# 带有变量的命令
@manager.option('-n', '-name', dest='name', default='hello')
def option_demo(name):
    print('hello', name)


if __name__ == '__main__':
    manager.run()