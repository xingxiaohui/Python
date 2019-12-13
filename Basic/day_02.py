# python 学习Day_02
# 标准数据类型的应用
# Python 数字类型转换
import math
import random

a = 1.0
b = 2
print(1, int(a))  # 转换成int
print(2, float(a))  # 转换成float
print(3, complex(a))  # 转换成虚部为零的复数
print(4, complex(a, b))  # 转换成实部为a虚部为b的复数

# Python 数学函数
a = -12.3
print(1, abs(a))
print(2, math.ceil(a))
print(3, math.exp(1))
print(4, math.fabs(a))
print(5, math.floor(a))
print(6, math.log(100, 10))
print(7, math.log10(100))
print(8, max(5, 7, 4, 2, 3, -5, 0))
print(9, min(5, 7, 4, 2, 3, -5, 0))
print(10, math.modf(-12.5))
print(11, pow(2, 5))
print(12, round(1.25, 1))
# 返回浮点数x的四舍五入值，如给出第二个参数，则代表舍入到小数点后的位数
# 注意：Python采用的舍弃原则为 4舍6入5看齐,奇进偶不进
print("round(10.5)", round(10.5))
print("round(11.5)", round(11.5))
print(13, math.sqrt(16))

# Python 随机数函数
print(1, random.choice(range(10)))  # 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数
print(2, random.randrange(1, 100, 2))  # 从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
print(3, random.random())  # 随机生成下一个实数，它在[0,1)范围内
print(4, random.uniform(8, 10))  # 随机生成下一个实数，它在[x,y]范围内。

# Python 数学常量
print(1, math.pi)
print(2, math.e)

# Python 字符串
# Python字符串运算符 +（连接），*（重复输出），[]（通过索引取），[a:b](截取范围a到b的，左闭右开)
# in (是否包含)，not in（是否不包含），r（原始字符串），%（格式化）
a = "python study"
print(1, a + "Day_02")
print(2, a*3)
print(3, a[5])
print(4, a[2:5])
print(5, "p" in a)
print(6, "p" not in a)
print(7, "hello\n", r"hello\n")
print(8, "hello %s,day %d" % ("python", 2))

a = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(a)

# f-string f-string 格式话字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来
# 它会将变量或表达式计算后的值替换进去
a = 1
print(f"{a + 1}")
print(f"{a + 1 =}")

# 字符串常用函数
a = "hello python"
b = "-"
c = ("a", "b", "c")
d = " "
print(1, len(a))
print(2, b.join(c))
print(3, d.isspace())
e = a.replace("h", "H", 1)
print(4, e)
f = a.split(" ")
print(5, f)
print(6, e.lower())
print(7, e.upper())

# Python 列表list
'''
序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
Python有6个序列的内置类型，但最常见的是列表和元组。
序列都可以进行的操作包括索引，切片，加，乘，检查成员。
此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
列表的数据项不需要具有相同的类型
'''
lista = ["hello", "python", "day", 1, 2.5]
print(1, lista[2])
lista[2] = "lista2"
print(1, lista[2])
print(2, lista*2)
print(3, lista + lista)
lista.append("append")
print(4, lista)
del lista[4]
print(5, lista)
print(6, len(lista))
print(7, 1 in lista)
print(8, "aa" not in lista)
print(9, lista[1:])
for x in lista:print("for", x)

# 嵌套列表 使用嵌套列表即在列表里创建其它列表
listb = [lista, "listb", "2333"]
print(10, listb)
listc = [8, 5, 2, 4, 6, 1]
print(11, max(listc))
print(12, min(listc))
lista.insert(1, "insert1")
print(13, lista)
print(14, lista.count("day"))
lista.pop()
print(15, lista)
lista.remove("hello")
print(16, lista)
lista.reverse()
print(17, lista)
lista.clear()
print(18, lista)

"""
Python 的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
"""
tupa = ("aaa", 2, "hello", "python")
tupb = ()  # 创建空元组
tupc = (50)  # 创建只有一个元素的元组时需要在元素后面添加逗号
tupd = (50,)
print(1, tupa[2])
print(2, type(tupc))
print(3, type(tupd))
# 其他方法类似于列表

"""
Python3 字典
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
"""
dicta = {"a" : 1, "b" : "bbbb", 1 : [2,"list"]}
print(1, dicta["b"])
print(2, dicta[1])

del dicta['a']  # 删除键 'Name'
print(3, dicta)
print(4, len(dicta))
print(5, "b" in dicta)  # return key in dic
dicta.clear()     # 清空字典
print(6, dicta)
del dicta  # 删除字典

"""
Python3 集合
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""
seta = {"ab", "cb", "c", "d", 1}
print(1, "a" in seta)
# 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')
print(2, a - b)                              # 集合a中包含而集合b中不包含的元素
print(3, a | b)                              # 集合a或b中包含的所有元素
print(4, a & b)                              # 集合a和b中都包含了的元素
print(5, a ^ b)                              # 不同时包含于a和b的元素
seta.add("add")                              # 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
print(6, seta)
# update()也可以添加元素，且参数可以是列表，元组，字典等，可同时添加多个
# s.update( {"字符串"} ) 将字符串添加到集合中，有重复的会忽略。
# s.update( "字符串" ) 将字符串拆分单个字符后，然后再一个个添加到集合中，有重复的会忽略。
seta.update("update1", "update2", (8, "update"))
print(7, seta)
seta.remove("update")                        # 将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
print(8, seta)
seta.discard("add")                          # discard也是移除集合中的元素，且如果元素不存在，不会发生错误
seta.pop()                                   # 也可以设置随机删除集合中的一个元素
print(9, "a" in seta)
print(10, seta)
seta.clear()                                 # 清空集合



