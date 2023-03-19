from tkinter import *
from math import *

problem=""
top=Tk()
h=Entry(top,font="TimesNewRoman 15", width=35,borderwidth=7)
h.grid(row=0, column=0,columnspan=5)

def button_click(number):
    current = h.get()
    h.delete(0, END)
    h.insert(0,str(current)+str(number))

def add():  
    a=h.get()
    global f_num
    global function
    function="add"
    f_num= float(a)
    h.delete(0, END)

def equals():
    s_num=h.get()
    h.delete(0, END)
    global function
    if function=="add":
        h.insert(0,f_num + float(s_num))
    elif function=="sub":
        h.insert(0,f_num - float(s_num))
    elif function=="multi":
        h.insert(0,f_num * float(s_num))
    elif function=="div":
        h.insert(0,f_num / float(s_num))
    elif function=="pwr":
        h.insert(0, f_num ** float(s_num))

button_6= Button(top,text="6", command=lambda:button_click(6)).grid(row=3, column=0)
button_5= Button(top, text="5", command=lambda:button_click(5)).grid(row=3, column=1)
button_4= Button(top, text="4", command=lambda:button_click(4)).grid(row=3, column=2)
button_Add= Button(top,text="+", command=add).grid(row=4, column=3)
button_Equlas= Button(top,text="=", command=equals).grid(row=5, column=2)

top.mainloop()



# def onclick(number):
#     global problem
#     global equation
#     problem += str(number)
#     equation = StringVar()
#     equation.set(problem)

# def equalPress():
#     global equation
#     global problem
#     ans = str(eval(problem))
#     equation.set(ans)
#     problem = ''






