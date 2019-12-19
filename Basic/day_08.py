"""
python 学习第八天 GUI 与网络编程
"""
import threading
import tkinter as tk
import socket
import time

on_hit = False


def gui_demo():
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()

    # 第2步，给窗口的可视化起名字
    window.title('Python窗口')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('600x400')  # 这里的乘是小x

    # 第4步，在图形界面上设定标签
    var = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
    l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
    # 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
    l.pack()

    # 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名

    def hit_me():
        global on_hit
        if not on_hit:
            on_hit = True
            var.set('请点击按钮')
        else:
            on_hit = False
            var.set('')

    # 第5步，在窗口界面设置放置Button按键
    b = tk.Button(window, text='点我试试', font=('Arial', 12), width=10, height=1, command=hit_me)
    b.pack()
    b2 = tk.Button(window, text='开启服务器', font=('Arial', 12), width=10, height=1, command=server_demo)
    b2.pack()

    # 第6步，主窗口循环显示
    window.mainloop()


def server_demo():
    # 创建一个基于IPv4和TCP协议的Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 监听端口:
    s.bind(('127.0.0.1', 9999))
    # 开始监听
    s.listen(5)
    print('Waiting for connection...')
    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


# 客户端与服务端需要在不同的文件运行，这里为了方便写在一个文件
def client_demo():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('127.0.0.1', 9999))
    # 接收欢迎消息:
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()


if __name__ == '__main__':
    #gui_demo()
    server_demo()
    #client_demo()
