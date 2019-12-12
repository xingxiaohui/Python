"""
Python 学习第五天输入输出与文件流
输出格式美化
Python 两种输出值的方式：表达式语句和print()函数
第三种方法是使用文件对象的wirte()方法，标准输出文件可以用sys.stdout引用
如果你希望输出的样式更加多样，可以使用str.format()函数来格式化输出值
如果你希望将输出的值转换成字符串可以使用repr()或str()函数来实现
    str():函数返回一个用户易读的表达式形式
    repr():产生一个解释器易读的表达式形式
"""
import math


def basic():
    s = "Hello, Python"
    print(str(s))
    print(repr(s))
    print(str(1 / 7))
    x = 10 * 3.25
    y = 200 * 200
    s = "x 的值为：" + repr(x) + ", y 的值为：" + repr(y) + "..."
    print(s)
    # repr()函数可以转义字符串中的特殊字符
    s = "hello Python\n"
    t = repr(s)
    print(t)
    # repr()函数的参数可以是Python的任何对象
    print(repr((x, y, ("hello", "python"))))


def square():
    for x in range(1, 11):
        # rjust()方法将字符串靠右并在左边填充空格 ljust()同
        # 另有 center()居中和zfill()在数字的左边填充0
        print(repr(x).rjust(2), repr(x * x).rjust(3), end="  ")
        print(repr(x*x*x).rjust(4))

    for x in range(1, 11):
        print("{0:2d} {1:3d} {2:4d}".format(x, x*x, x*x*x))


def str_format():
    # str.format() 基本用法
    print("{}喜欢'{}'!".format("小明", "Python编程"))
    """
    括号及其里面的字符（称作格式化字段）将会被format()中的参数替换
    在括号中的数字用于只想传入对象在format()中的位置，
    如果使用了关键字参数，那么他们的值会指向使用该名字的参数，如下
    """
    print("{0}和{1}是兄弟".format("刘备", '关羽'))
    print("{1}和{0}是兄弟".format("刘备", '关羽'))
    print("{first}和{second}是兄弟".format(first='刘备', second='关羽'))
    # 位置和关键字参数可以随意的组合
    print("{0}和{1}还有{third}是兄弟".format('刘备', '关羽', third='张飞'))
    # !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
    print('常量 PI 的值近似为： {!r}。'.format(math.pi))
    # 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。
    print('常量PI的近似值为{0:.3f}'.format(math.pi))
    # 在:后传入一个整数可以保证该域至少有这么多的宽度，用于美化表格
    table = {'hello': 1, 'python': 2, 'world': 3}
    for name, number in table.items():
        print('{0:10}--{1:10d}'.format(name, number))
    '''
    旧式字符串格式化% 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符
    串, 而将右边的代入, 然后返回格式化后的字符串
    因为 str.format() 比较新的函数， 大多数的 Python 代码仍然使用 % 操作符。但是因为这种旧式的格式化
    最终会从该语言中移除, 应该更多的使用 str.format()
    '''
    print('常量 PI 的值近似为：%5.3f。' % math.pi)


def key_input():
    s = input('请输入：')
    print('你输入的字符是：', s)


def read_writ_file():
    """
    open() 将会返回一个 file 对象，基本语法格式如下:
    open(filename, mode)
    filename：包含了你要访问的文件名称的字符串值。
    mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。
    这个参数是非强制的，默认文件访问模式为只读(r)。
    """
    f = open('D:/python_test.txt', 'w')
    # w.write(string)将string写入到文件中，然后返回写入的字符数
    num = f.write('Python 是一门非常好的语言\n是的，非常好！！！\n')
    print(0, num)
    # 如果写入的不是字符串，那么需要进行转换
    value = ('python', 111)
    s = str(value)
    num1 = f.write(s)
    print(0, num1)
    f.close()
    '''
    f.read(size)函数可以读取文件一定数目的数据，然后作为字符串或者字节对象返回
    size是一个可选的数字类型的参数，当size被忽略或者为负，那么全部读取文件内容并返回
    '''
    f = open('D:/python_test.txt', 'r')
    s = f.read()
    f.close()
    print(1, s)
    print(2, repr(s))
    '''
    f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 
    说明已经已经读取到最后一行。
    f.readlines()
    f.readlines() 将返回该文件中包含的所有行。
    如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
    '''
    f = open('D:/python_test.txt', 'r')
    s = f.readline()
    f.close()
    print(3, s)

    f = open('D:/python_test.txt', 'r')
    ss = f.readlines()
    f.close()
    print(4, ss)
    f.close()
    # 通过迭代的方式也可以逐行输出文件的内容
    f = open('D:/python_test.txt', 'r')
    for line in f:
        print(5, line)
    f.close()
    '''
    其他方法：
    f.tell() 返回文件对象当前所处的位置，它是从文件开头计算的字节数
    f.seek(offset, from_what) offset表示要移动的字符数，from表示移动的位置：0-文件开头，1-当前位置，2文件结尾
    seek(x,0):表示从文件首行首字符移动x个字符
    seek(x,1):表示从当前位置向后移动x个字符
    seek(-x,2):表示从文件的结尾向前移动x个字符 
    '''
    f = open('D:/python_test.txt', 'wb+')
    f.write(b'0123456789')
    f.seek(5)
    a = f.read(1)
    print(6, a)
    f.seek(-8, 2)
    a = f.read(2)
    print(6, a)
    # 调用 f.close() 来关闭文件并释放系统的资源，关闭后再调用该文件，则会抛出异常
    f.close()

    # 当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。
    with open('D:/python_test.txt', 'r') as f:
        s = f.read()
        print(7, s)


def pickle_mode():
    """
    pickle 模块
    python的pickle模块实现了基本的数据序列和反序列化。
    通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
    通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
    基本接口：
        pickle.dump(obj, file, [,protocol])
    """
    print(8, '栗子不好举，以后再说吧^—^')


if __name__ == '__main__':
    basic()
    square()
    str_format()
    # key_input()
    read_writ_file()
    pickle_mode()