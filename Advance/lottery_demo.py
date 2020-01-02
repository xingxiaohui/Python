import random


# 简单的模拟双色球的方法
def double_ball():
    ball_set = set()
    while True:
        red_num = random.randint(1, 33)  # random.randint(1, 33) 生成红球
        ball_set.add(red_num)  # add()方法用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作
        if len(ball_set) == 6:
            # 将集合进行排序，彩票就是这样的，前６个数字从小到大
            _set = sorted(ball_set)
            #  将集合转为列表的形式，方便向该数字中增加蓝色数值
            all_ball = list(_set)
            blue_num = random.randint(1, 16)
            #  组合成双色球，蓝色球数字和前六个红色球的数字之间没有关系
            all_ball.append(blue_num)
            return all_ball


# 阴阳师抽卡模拟 R卡概率79%，SR概率20%，SSR概率1%
def onmyoji(n):
    list1 = ['R'] * 7900 + ['SR'] * 2000 + ['SSR'] * 100
    for i in range(int(n)):
        L = (random.choices(list1, k=10))
        print('第' + str(i+1) + '次十连抽：', L)


if __name__ == '__main__':
    # for i in range(20):
    #     res = double_ball()
    #     print(res)
    onmyoji(10)


