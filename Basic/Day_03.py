# Python 学习第三天
# 简单的条件控制与函数
import math
import random


def fibonacci():
    a, b = 0, 1
    while b < 1000:
        a, b = b, a + b
        print(b, end=",")


def dog_age():
    age = int(input("请输入你家狗狗的年龄: "))
    print("")
    if age <= 0:
        print("你是在逗我吧!")
    elif age == 1:
        print("相当于 14 岁的人。")
    elif age == 2:
        print("相当于 22 岁的人。")
    elif age > 2:
        human = 22 + (age - 2) * 5
        print("对应人类年龄: ", human)
    input("点击 enter 键退出")


def guess_number():
    print("猜数字游戏")
    target = random.choice(range(100))
    guess = -1
    while target != guess:
        guess = int(input("请输入一百以内的数字！"))
        if guess > target:
            print("猜大了，换个小的试试")
        else:
            print("猜小了，换个大的试试")
    print("恭喜你，猜对了，答案是%d" % target)


def multiplication():
    print("九九乘法表：")
    for i in range(1, 10, 1):
        for j in range(1, i + 1, 1):
            print("%d*%d=%d" % (j, i, i * j), end=" ")
        print("")


if __name__ == '__main__':
    # fibonacci()
    # dog_age()
    # guess_number()
    multiplication()
