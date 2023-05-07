import pyautogui
from time import sleep

time = 2


def do_full(x, y):
    i = 0
    sleep(time)
    while i < 20:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        pyautogui.moveTo(944, 813)
        pyautogui.click()
        i = i + 1


def raze_full():
    return do_full(792, 1008)


def phoenix_full():
    return do_full(704, 1005)


def neon_full():
    return do_full(541, 1007)


def jett_full():
    return do_full(1212, 927)


def reyna_full():
    return do_full(887, 990)


def yoru_full():
    return do_full(1297, 1006)
