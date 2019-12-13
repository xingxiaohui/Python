"""
Python3 模块
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能
"""
# 一个引入模块的例子  文件名: using_sys.py
import sys

print('命令行参数如下:')
for i in sys.argv:
    print(i)
print('Python 路径为：', sys.path, '\n')

"""
import 语句
想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：
import module1[, module2[,... moduleN]
"""

"""
from … import 语句
Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：
from modname import name1[, name2[, ... nameN]]
"""
"""
from … import * 语句
把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
from modname import *
"""
"""
__name__属性
一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，
我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
"""
# Filename: using_name.py
if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')

"""
dir() 函数
内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
"""
print(dir(sys))
# 如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:
print(1, "当前定义的名称：")
print(dir())

"""
包
包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。
在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。
用户可以每次只导入一个包里面的特定模块，比如:

import sound.effects.echo
这将会导入子模块:sound.effects.echo。 他必须使用全名去访问:

sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
还有一种导入子模块的方法是:

from sound.effects import echo
这同样会导入子模块: echo，并且他不需要那些冗长的前缀，所以他可以这样使用:

echo.echofilter(input, output, delay=0.7, atten=4)
还有一种变化就是直接导入一个函数或者变量:

from sound.effects.echo import echofilter
同样的，这种方法会导入子模块: echo，并且可以直接使用他的 echofilter() 函数:

echofilter(input, output, delay=0.7, atten=4)
注意当使用 from package import item 这种形式的时候，对应的 item 既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。
"""

