"""
Flask 框架的学习
"""
from flask import Flask, render_template

app = Flask(__name__)


# app.route(agrs)用于控制路径，类似于Java的controller
@app.route('/index/')
@app.route('/')
def index():
    return 'hello world'


# '<>'用于传递参数，可以标明类型 eg:<int:uid>
@app.route('/profile/<int:uid>', methods=['post', 'get'])
def profile(uid):
    color = ['red', 'blue', 'yellow', 'black']
    return render_template('profiles.html', uid=uid, color=color)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
