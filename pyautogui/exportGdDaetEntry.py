from asyncio.windows_utils import BUFSIZE
import pyautogui as pg
import time
containerNumbers=int(input("Enter number of containers: "))

pg.FAILSAFE= True
time.sleep(10)

for i in range(0,containerNumbers-1):
    pg.hotkey('ctrl', 'c')
    pg.keyDown("alt")
    pg.press("tab")
    pg.keyUp("alt")

    pg.hotkey('ctrl', 'v')
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("space")
    pg.press("tab")

    pg.keyDown("alt")
    pg.press("tab")
    pg.keyUp("alt")

    time.sleep(0.5)

    pg.press("down")
    time.sleep(0.5)
