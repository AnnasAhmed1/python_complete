import random

import pyautogui as pg

import time

#apran_khunger

animal = ('How are you all? Welcome back', 'Ramzan hai sharam kr lo roza hai', 'Ramzan Aaya roza rkho gi roza rkho', 'Asad bahi aap yahn kese aa gaye ' , 'Ali bhai aap tou bohot busy bndy hain' )

time.sleep(10)

#apran_khunger

for i in range (100):

    a  = random.choice(animal)


    pg.write(a)
    time.sleep(2)

    pg.press('enter')
