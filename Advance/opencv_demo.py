"""
opencv-python 的学习
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


# 基于opencv 的orb检测算法实现
def func_orb():
    img = cv.imread('E:/image/target.png', 0)
    # Initiate ORB detector
    orb = cv.ORB_create()
    # find the keypoints with ORB
    kp = orb.detect(img, None)
    # compute the descriptors with ORB
    kp, des = orb.compute(img, kp)
    # draw only keypoints location,not size and orientation
    img2 = cv.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)
    plt.imshow(img2), plt.show()


# 角点检测算法
def func_corners():
    img = cv.imread('E:/image/target.png')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    corners = cv.goodFeaturesToTrack(gray, 25, 0.01, 10)
    corners = np.int0(corners)
    for i in corners:
        x, y = i.ravel()
        cv.circle(img, (x, y), 3, 255, -1)
    plt.imshow(img), plt.show()


if __name__ == '__main__':
    func_orb()
    # func_corners()
