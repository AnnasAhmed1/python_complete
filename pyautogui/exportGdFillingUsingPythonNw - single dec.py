from asyncio.windows_utils import BUFSIZE
import pyautogui as pg
import time
containerNumbers=int(input("Enter number of containers: "))
# firstNumber=input("Enter first container number:")

pg.FAILSAFE= True
if(len(firstNumber)==0):
    firstNumber="ABCD0000000"
else:
    alphaCheck=0
    for i in range(0,4):    
        if firstNumber[i].isalpha()==False:
            alphaCheck=1
    numCheck=0
    for i in range(4,len(firstNumber)):    
        if firstNumber[i].isalpha():
            numCheck=1
    if alphaCheck==1:
        firstNumber="ABCD0000000"
                
    elif numCheck==1:
        firstNumber="ABCD0000000"
    elif(len(firstNumber)!=11):
        firstNumber=firstNumber[0:4]+"0000000"
    firstNumber=firstNumber[0:-1]+"0"
time.sleep(5)
for i in range (0,containerNumbers*2,2):
    # Adding container numbers
    lastDigit=i
    lastDigit=lastDigit+2
    lastDigit=lastDigit//2
    lastDigit=str(lastDigit)
    if(len(lastDigit)==1):
        pg.write(firstNumber[0:-1]+lastDigit)
    elif(len(lastDigit)==2):
        pg.write(firstNumber[0:-2]+lastDigit)
    
    pg.press('tab')
    # add quantity
    pg.write("27000")
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
    pg.hotkey('ctrl', 'f')
    time.sleep(1)
    n=int(i)
    lastCheck=(n+2)//2
    if (lastCheck!=containerNumbers):
        pg.write("add")
        time.sleep(0.5)
        pg.press("esc")
        pg.press("enter")
        time.sleep(0.5)
        pg.hotkey('ctrl', 'f')
        time.sleep(0.5)
        pg.write("save")
        time.sleep(0.5)
        pg.press("esc")
        pg.press("tab")
        pg.press("tab")
pg.press("esc")

