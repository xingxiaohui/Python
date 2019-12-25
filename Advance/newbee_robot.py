"""
一个能解决一切难题的机器人，只会说关你屁事和关我屁事
"""


def robot(word):
    if '你' in word:
        print('关你屁事~')
    elif '我' in word:
        print('关我屁事~')
    else:
        print('这事跟你我无关~')


if __name__ == '__main__':
    while True:
        ask = input('请输入你遇到的问题')
        robot(ask)
