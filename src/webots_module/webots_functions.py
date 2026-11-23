import pyautogui as pg
import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()

the_post = f'http://{os.getenv("my_HOST")}:{os.getenv("my_API_PORT")}'


def focus_webots():
    win = pg.getWindowsWithTitle('.wbt')[0]
    if win.isMinimized:
        win.restore()
        time.sleep(0.1)

    pg.click(win.left + (win.width // 2), win.top + 15)
    time.sleep(0.05)


def play_webots():
    focus_webots()
    requests.post(f'{the_post}/{41}')


def pause_webots():
    focus_webots()
    requests.post(f'{the_post}/{39}')


def reset_webots_sim():
    focus_webots()
    requests.post(f'{the_post}/{60}')
