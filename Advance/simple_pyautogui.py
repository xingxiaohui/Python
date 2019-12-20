"""
python 第三方模块库 pyautogui 的小栗子
"""
import pyautogui


def pyautogui_move_demo():
    x, y = pyautogui.size()

    print('屏幕分辨率为：%d，%d' % (int(x), int(y)))
    # 该模块默认屏幕的原点在左上角，位置为（0, 0）
    # px, py = pyautogui.position()
    # print('当前鼠标的位置为：%d，%d' % (px, py))
    # 判断某个位置是否在屏幕上
    print('(-1, 100)的点判断结果：', pyautogui.onScreen(-1, 100))
    print('(1000, 100)的点判断结果：', pyautogui.onScreen(1000, 100))
    # 延迟几秒之后执行，全部的pyautogui都将延迟之后执行
    # pyautogui.PAUSE = 5
    # 移动鼠标
    pyautogui.moveTo(x/2, y/2)
    # 带有延迟的鼠标移动
    pyautogui.moveTo(100, 200, 2)
    # 带有延迟的鼠标移动,且移动速度带有变化，None表示当前该坐标不变
    pyautogui.moveTo(1000, None, 2, pyautogui.easeInQuad)  # 开始慢，越来越快
    print_position()
    # 相对位置的移动鼠标
    pyautogui.move(50, 100)
    pyautogui.move(-50, 100)
    # None表示当前该坐标不变
    pyautogui.move(None, 100)
    print_position()

    '''# 画图  需要打开画图板软件
    distance = 100
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.5)  # move right
        distance -= 10
        pyautogui.dragRel(0, distance, duration=0.5)  # move down
        pyautogui.dragRel(-distance, 0, duration=0.5)  # move left
        distance -= 10
        pyautogui.dragRel(0, -distance, duration=0.5)  # move up
    '''


def click_demo():
    pyautogui.moveTo(1920/2, 1080/2)
    # ‘左键’点击当前位置
    pyautogui.click()
    # 移动到指定位置后点击
    pyautogui.click(x=920, y=580)
    # clicks设置点击多次，interval设置点击间隔/秒
    pyautogui.click(button='left', clicks=3, interval=0.25)
    # 鼠标滚动
    pyautogui.scroll(40)
    # 移动到某个位置开始滚动
    pyautogui.scroll(20, x=920, y=580)
    # 传递'left'，'middle'或 'right'给
    pyautogui.click(button='right')


def key_press():
    # 打出指定的字符串 可设置每个字符的间隔
    pyautogui.typewrite('Hello world!')
    pyautogui.typewrite('Hello world!', interval=0.25)  #
    # 同时按下多个键
    pyautogui.press(['0', '1', '2'])
    # 组合键函数，以先按后放的顺序按下指定按键达到快捷键的效果
    pyautogui.hotkey('ctrl', 'shift', 'del')


# 一个发送消息的小栗子，移动到微信或者QQ的消息框，敲出指定的文字后回车发送，拼音加空格能敲出汉字
def test():
    # 带有延迟的鼠标移动
    pyautogui.moveTo(1142, 704, 5)
    # ‘左键’点击当前位置
    pyautogui.click()
    # 打出指定的字符串 可设置每个字符的间隔
    pyautogui.typewrite('zhe shi wo yong chengxu zai fa xinxi!', interval=0.25)
    # 按下回车
    pyautogui.press('enter')


# 屏幕截图功能
def screenshot_demo():
    img = pyautogui.screenshot('D://my_screenshot.png')
    # 不需要全部截图的时候传入参数，坐标、长宽
    im = pyautogui.screenshot(region=(0, 0, 300, 400))


# 获取某个按钮的位置并点击
def test_location_click():
    # 查找小图片在屏幕上的位置 grayscale开启灰度匹配加速,region限制范围加速
    location = pyautogui.locateOnScreen('E://button.png', grayscale=True, region=(0, 0, 1900, 1000))
    print(1, location)
    print(2, "x", location[0])
    # 获取匹配图的中心点，一个x、y的坐标
    center = pyautogui.center(location)
    print(3, center, "  x", center[0], "  y", center[1])
    x, y = center
    # pyautogui.click(x, y)

    # locateCenterOnScreen 可以直接获取图象匹配位置的中点
    x1, y1 = pyautogui.locateCenterOnScreen('E://button.png')
    print(4, "x1", x1, "  y1", y1)
    pyautogui.click(x1, y1)


# 打印当前鼠标的位置
def print_position():
    px, py = pyautogui.position()
    # 该模块默认屏幕的原点在左上角，位置为（0, 0）
    print('当前鼠标的位置为：%d，%d' % (px, py))


if __name__ == '__main__':
    # pyautogui_move_demo()
    # click_demo()
    # test()
    # screenshot_demo()
    test_location_click()
