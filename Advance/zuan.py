import datetime
import time

import pyperclip
import pyautogui


def battle():
    print('十秒后开始问候')
    time.sleep(10)
    for word in open("D://zuan.txt"):
        pyperclip.copy(word)
        # pyperclip.paste()
        pyautogui.hotkey('ctrlleft', 'v')
        pyautogui.press('enter')
        time.sleep(0.8)


if __name__ == "__main__":
    battle()