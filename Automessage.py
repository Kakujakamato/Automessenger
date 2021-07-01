import time

import pyautogui


def SendScript():
    time.sleep(6)
    with open('script.txt') as flow:
        lines = flow.readlines()
    for line in lines:
        pyautogui.typewrite(line.strip())
        pyautogui.press('enter')


SendScript()
