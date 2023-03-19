from ast import Expression
from dis import dis
from doctest import master
from re import I
from tkinter import  *
from math import *
from webbrowser import get

top = Tk()

e=Entry(top)
e.grid(row=0, column=0,columnspan=5)

def button_click(number):
    equation = e.get()
    e.delete(0, END)
    e.insert(0,str(equation)+str(number))

def equalPress():
    global e

    ans = str(eval(e))
    equation.set(ans)

    e = ''

buttonEqual =  Button(top, text=' = ', fg='black', bg='white', command = equalPress, height=1, width=7)
buttonEqual.grid(row = 7, column = 4)



button1 = Button(top, text = '1', fg = 'black', bg = 'white', command = lambda: button_click(1), height = 1, width = 7)
button1.grid(row = 6, column = 0)

button2 = Button(top, text = '2', fg = 'black', bg = 'white', command = lambda: button_click(2), height = 1, width = 7)
button2.grid(row = 6, column = 1)

buttonPlus =  Button(top, text=' + ', fg='black', bg='white', command = lambda: button_click("+"), height=1, width=7)
buttonPlus.grid(row = 6, column = 3)







# def sum():  
#     a=e.get()
#     global f_num
#     global function
#     function="add"
#     f_num= float(a)
#     e.delete(0, END)











top = Tk()

i=1
for r in range (3):
    for c in range(3):
        b= Button(top, text='%s'%(i),width=2)
        b.grid(row=r, column=c)
        i+=1
b= Button(top, text="0",width=2)
b.grid(row=3, column=0)
b= Button(top, text=".",width=2)
b.grid(row=3, column=1)
b= Button(top, text="=",width=2)
b.grid(row=3, column=2)
ba= Button(top, text="+",width=2)
ba.grid(row=3, column=4, columnspan=5)



top.mainloop()
