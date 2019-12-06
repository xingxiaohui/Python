
# python 学习01
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












