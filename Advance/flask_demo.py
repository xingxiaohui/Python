"""
Flask 框架的学习
"""
from flask import Flask, render_template, request, make_response, redirect, flash, get_flashed_messages
# log 需要的库
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
# flash massage 使用的时候需要添加该属性，用于生成session的标志，通常为随即字符串
app.secret_key = 'khalfhoshflhal'


# app.route(agrs)用于控制路径，类似于Java的controller
@app.route('/index/')
@app.route('/')
def index():
    # 打印log的地方
    app.logger.warn('用户访问了路径')
    res = ''
    for msg, category in get_flashed_messages(with_categories=True):
        res = res + category + ':' + msg + '<br>'
    return 'hello world<br>' + res


# '<>'用于传递参数，可以标明类型 eg:<int:uid>
@app.route('/profile/<int:uid>', methods=['post', 'get'])
def profile(uid):
    color = ['red', 'blue', 'yellow', 'black']
    return render_template('profiles.html', uid=uid, color=color)


# request 与 response
@app.route('/request')
def request_demo():
    # 获取参数
    name = request.args.get('name', 'defaultkey')
    req = request.args.get('name', 'defaultkey') + '<br>'
    req += request.url + '--path:' + request.path + '<br>'
    for property in dir(request):
        req += str(property) + '--'+str(eval('request.' + property)) + '<br>'
    response = make_response(req)
    res = '--------------------------<br>'
    for property in dir(response):
        res +=str(property) + '--' + str(eval('response.' + property))
    response = make_response(req+res)
    # 设置cookie
    response.set_cookie('name', name)
    # 设置返回的状态
    response.status = '404'
    # 设置header
    response.headers['username'] = 'xxh'
    return response


@app.route('/redirect/<code>')
def redirect_demo(code):
    # redirect(重定向的路径, 重定向的码：301永久、302临时)
    return redirect('/', code=code)


# flash massage示例
# flash(msg) 发送 get_flash_massages  获取
@app.route('/flash_test')
def flash_demo():
    flash('登录成功', 'info')
    return 'ok'


# 统一页面处理
@app.errorhandler(404)
def errorhandler_demo(error):
    return render_template('404.html', url=request.url), 404


@app.errorhandler(500)
def error_500(error):
    return render_template('404.html', url=request.url), 500


# 统一日志处理接口
@app.route('/log/<level>/<msg>')
def log_demo(level, msg):
    dict = {'warn': logging.WARN, 'error': logging.ERROR, 'info': logging.INFO}
    if level in dict:
        app.logger.log(dict[level], msg)

    return 'logged success' + msg


# log 的应用，配置log文件与级别
def set_logger():
    info_file_handler = RotatingFileHandler('D:/python/logs/info.txt')
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)

    warn_file_handler = RotatingFileHandler('D:/python/logs/warn.txt')
    warn_file_handler.setLevel(logging.WARN)
    app.logger.addHandler(warn_file_handler)

    error_file_handler = RotatingFileHandler('D:/python/logs/error.txt')
    error_file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_handler)


if __name__ == '__main__':
    set_logger()
    app.run(debug=True, port=5000)
