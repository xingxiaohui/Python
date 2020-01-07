"""
学习算法与数据结构入门的迷宫栗子
搞了一中午没弄懂怎么生成地图，还是再去看看数据结构的知识吧，先不搞了
"""


def build_map(x, y):
    # 此处二维数组初始化有坑 若使用 maze = [[0] * n] * m 方式初始化则修改会混乱，此方式为错误的初始化二维数组方式
    maze = [['0' for i in range(x+2)] for i in range(y+2)]
    for i in (0, x):
        for j in range(0, y+2):
            maze[i][j] = 1
            maze[j][i] = 1
    print(maze)
    maze[1][1] = 0
    maze_map = build_wall(maze, 1, 1)
    print(maze_map)


def build_wall(maze_map, x, y):
    return maze_map


def cross_maze():
    pass


if __name__ == '__main__':
    build_map(6, 6)
