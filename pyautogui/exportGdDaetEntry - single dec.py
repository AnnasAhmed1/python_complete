from asyncio.windows_utils import BUFSIZE
import pyautogui as pg
import time
pg.FAILSAFE= True
containerNumbers=[
    "AMMM0000001",
    "AMMM0000002",
    "AMMM0000003",
    "AMMM0000004",
    "AMMM0000005",
    "AMMM0000006",
    "AMMM0000007",
    "AMMM0000008",
    "AMMM0000009",
    "AMMM0000010",
    "AMMM0000011",
    "AMMM0000012",
    "AMMM0000013",
    "AMMM0000014",
    "AMMM0000015",
    "AMMM0000016",
    "AMMM0000017",
    "AMMM0000018",
    "AMMM0000019",
    "AMMM0000020",
    "AMMM0000021",
    "AMMM0000022",
    "AMMM0000023",
    "AMMM0000024",
    "AMMM0000025",
    "AMMM0000026",
    "AMMM0000027",
    "AMMM0000028",
    "AMMM0000029",
    "AMMM0000030",
    "AMMM0000031",
    "AMMM0000032",
]
input("statr?")

time.sleep(10)

for i in range(0,len(containerNumbers)):

    # if len(containerNumbers[i]<7):
    #     containerNumbers[i]+"00"

    pg.hotkey('ctrl', 'f')
    pg.write("add container")
    pg.press("esc")
    pg.press("enter")
    pg.press("tab")
    pg.press("tab")
    pg.write(containerNumbers[i])
    pg.press("tab")
    pg.write("27000")
    pg.press("tab")
    pg.write("1")
    pg.press("tab")
    pg.write("bulk")
    pg.press("enter")
    pg.press("enter")
    
    time.sleep(1)
    pg.press("enter")
    time.sleep(2)
