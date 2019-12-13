
# python 学习Day_01
# 基础语法
# 注释：单行注释使用"#",多行注释使用''' 或者 """
# python使用缩进来表示代码块 不需要使用｛｝
# 使用反斜杠\来实现多行语句，使用(){}[]包含的代码块不需要使用反斜杠也能多行
# 同一行书写多行语句可使用;分号分隔
import sys  # 导入模块
from sys import argv,path  # 导入特定的成员
print('\n python路径为', sys.path)
x = "a"
y = "b"
print(x)  # 默认输出，换行
print(y, end='')  # 默认输出，不换行

# 基本数据类型
counter = 100   # 整型变量
miles = 120.00  # 浮点型变量
name = "erick"  # 字符串
print(counter)
print(miles)
print(name)

a = b = c = 1   # 多变量赋值
d, e, f = 1, 2, "erick"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 标准数据类型

"""
Number（数字）
Python3 支持 int、float、bool、complex（复数）。
"""
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

print(2**5)  # 乘方

'''
String（字符串）
Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 "\"转义特殊字符。
Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。
'''
str = 'python'
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "Study")  # 连接字符串
print('python\nStudy')  # \转义特殊字符
print(r'python\nStudy')  # 在字符串前添加r表示不做转义

'''
List（列表）
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
列表中的数据类型可不相同，列表中的单个元素可被赋值修改
'''
list = ['abcd', 786, 2.23, 'python', 70.2]
tiny = [123, 'python']

print('输出完整列表:', list)  # 输出完整列表
print('输出列表第一个元素', list[0])  # 输出列表第一个元素
print('从第二个开始输出到第三个元素', list[1:3])  # 从第二个开始输出到第三个元素
print('输出从第三个元素开始的所有元素', list[2:])  # 输出从第三个元素开始的所有元素
print('输出两次列表', tiny * 2)  # 输出两次列表
print('连接列表', list + tiny)  # 连接列表

'''
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。
虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
string、list 和 tuple 都属于 sequence（序列）。
'''
tuple = ('abcd', 786, 2.23, 'python', 70.2)
tinytuple = (123, 'python')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

'''
Set（集合）
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式：
parame = {value01,value02,...}
或者
set(value)
'''
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素

'''
Dictionary（字典）
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
字典类型也有一些内置的函数,例如clear()、keys()、values()等。
'''
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print(dict['one'])       # 输出键为 'one' 的值
print(dict[2])           # 输出键为 2 的值
print(tinydict)          # 输出完整的字典
print(tinydict.keys())   # 输出所有键
print(tinydict.values())  # 输出所有值

'''
算术运算符
Python支持 +，-，*，/（数学意义除，结果可以带小数），//（整除，结果为向下取整），%（取模），**（幂运算）
'''
a = 5; b = 2
print("a/b=", a / b)
print("a//b=", a // b)
print("a%b=", a % b)
print("a**b=", a ** b)

'''
比较运算符
Python比较运算符与java相同，支持==，！=，>,<,>=,<=
'''
if (a == b):
    print("a==b")
elif(a != b):
    print("a!=b")
if(a > b):
    print("a>b")
elif(a < b):
    print("a<b")
if(a >= b):
    print("a>=b")
else:
    print("a<=b")

'''
赋值运算符
Python比较运算符与java相同，支持=，+=，-=，*=，**=，/=，//=，%=
Python 3.8 新增海象运算符，可在表达式内部为变量赋值。
'''
c = "asdfgasdfgh"
if (n := len(c)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")

'''
Python位运算符
Python比较运算符与java相同，支持&,|,^,~(按位取反)，<<,>>
'''
print(~a)  # ~对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1

'''
Python逻辑运算符
Python 逻辑运算符包含 and，not ，or，与java的&&，||，！相同
'''
a = 10
b = 20
if (a and b):
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")
# 修改变量 a 的值
a = 0
if (a and b):
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")
if (a or b):
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")
if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")

'''
Python成员运算符
Python支持成员运算符，返回成员是否属于指定的序列，包括字符串，列表或元组。
'''
a = 10
b = 20
list = [1, 2, 3, 4, 5]
if (a in list):
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")
if (b not in list):
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")
# 修改变量 a 的值
a = 2
if (a in list):
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")

'''
Python身份运算符
身份运算符用于比较两个对象的存储单元
x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
注： id() 函数用于获取对象内存地址。
is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
'''
if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")
# 修改b的值
b = 2
if ( a is b ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")




