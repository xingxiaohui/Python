"""
基于网易aircv的图片操作小栗子
SIFT 算法已经申请专利不能用了，本模块中仅模版匹配可以正常使用
"""
import aircv as ac

img_sou = ac.imread('E:/image/source.png')  # 源图图像
img_tar = ac.imread('E:/image/target.png')  # 目标图像


# SIFT算法匹配：匹配特征点和描述，不受缩放影响
def find_sift(source, target):
    result = ac.find_sift(source, target)
    print(1, 'SIFT匹配结果：')
    print(result)


# SIFT算法匹配：匹配特征点和描述，不受缩放影响
def find_all_sift(source, target, max=0):
    """

    """
    result = ac.find_all_sift(source, target, max=max)
    print(2, 'SIFT匹配结果：')
    print(result)


# 直接匹配查找图像：直接匹配模版，受缩放影响严重
def find_template(source, target):
    result = ac.find_template(source, target)
    print(3, '直接模版匹配结果：')
    print(result)


if __name__ == '__main__':
    # find_sift(img_sou, img_tar)
    find_template(img_sou, img_tar)
