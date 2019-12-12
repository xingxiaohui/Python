"""
一个简单的python web应用栗子
"""
from wsgiref.simple_server import make_server


def simple_web(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello Python Web!</h1>']


if __name__ == '__main__':
    a = 8000
    httpd = make_server('', a, simple_web)
    httpd.serve_forever()