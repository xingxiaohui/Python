"""
python 学习第七天 高阶函数
在Python 3里，reduce() 函数已经被从全局名字空间里移除了，它现在被放置在 fucntools 模块里
使用前需要先引用
"""
from functools import reduce


# 内建函数 map(func, iterable)：map() 将传入的可迭代的数据按序参与func函数的运算，并返回原序对应的结果
def func(x):
    return x * x


# reduce作用的函数必须能接受两个参数
def func_add(x, y):
    return x + y


# filter作用的函数必须返回布尔值
def even_num(x):
    return x % 2 == 0


def map_demo():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = map(func, a)
    print(1, list(b))
    # 另一个栗子，把a中的所有元素转换成字符串
    print(2, list(map(str, a)))


# reduce(func, iterable): reduce 将传入的可迭代的数据按序参与func函数运算，并将结果作为参数之一参与下一次计算
def reduce_demo():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = reduce(func_add, a)
    print(3, int(b))


# Python内建的filter()函数用于过滤序列 filter()把传入的函数依次作用于每个元素，根据返回值是True、False决定保留还是丢弃该元素
def filter_demo():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = filter(even_num, a)
    print(4, list(b))


# Python内置的sorted(list, key, reverse)函数就可以对list进行排序,其排序结果是按照key函数计算的结果排序的,reverse是否逆序
def sorted_demo():
    a = [12, -1, -22, 35, 34, 25, 16, -7, 8, -9]
    # 按照绝对值函数对a进行排序，key参数需要指名
    b = sorted(a, key=abs)
    print(5, list(b))


# lambda 表达式 定义方式 lambda args : expression
# lambda 表达式可以赋值给一个变量，通过该变量来调用，也可以直接作为参数传递给高阶函数
def lambda_demo():
    f = lambda x, y: x * y
    print(6, f(5, 3))
    a = [12, -1, -22, 35, 34, 25, 16, -7, 8, -9]
    b = map(lambda x: x * x, a)
    print(7, list(b))


if __name__ == '__main__':
    map_demo()
    reduce_demo()
    filter_demo()
    sorted_demo()
    lambda_demo()
