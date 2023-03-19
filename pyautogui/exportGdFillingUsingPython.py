import pyautogui as pg
import time
containerNumbers=int(input("Enter number of containers: "))
time.sleep(5)
for i in range (0,containerNumbers*2,2):
    # Adding container numbers
    lastDigit=i
    lastDigit=lastDigit+2
    lastDigit=lastDigit//2
    lastDigit=str(lastDigit)
    if(len(lastDigit)==1):
        pg.write("AAAA000000"+lastDigit)
    elif(len(lastDigit)==2):
        pg.write("AAAA00000"+lastDigit)
    pg.press('tab')
    # add quantity
    pg.write("28000")
    pg.press('tab')
    # add packages numbers
    pg.write("1")
    pg.press('tab')
    # add packages
    pg.write("bu")
    # saving the container
    pg.keyDown("shift")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.keyUp("shift")
    pg.press("enter")
    # time for updating/saving the caontainer
    time.sleep(1)
    # new container
    n=int(i)
    lastCheck=(n+2)//2
    if (lastCheck!=containerNumbers):
        # break
        for j in range(0,n+3):
            pg.press("tab")
        pg.press("enter")
        time.sleep(1)
        n=int(i)
        for k in range(0,n+5):
            pg.press("tab")