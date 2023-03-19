from tkinter import *
import math

root= Tk()
root.geometry("401x288")
root.title("Scientific_Calculator")
root.configure(bg="Grey")

h=Entry(root,font="TimesNewRoman 15", width=35,borderwidth=7)
h.grid(row=0, column=0,columnspan=5)

def button_click(number):
    current = h.get()
    h.delete(0, END)
    h.insert(0,str(current)+str(number))

def Del():
    length=len(h.get())
    h.delete(length-1, 'end')
    
def button_clear():
	h.delete(0, END)

def add():  
    a=h.get()
    global f_num
    global function
    function="add"
    f_num= float(a)
    h.delete(0, END)

def sub():  
    a=h.get()
    global f_num
    global function
    function="sub"
    f_num= float(a)
    h.delete(0, END)
    
def multi():  
    a=h.get()
    global f_num
    global function
    function="multi"
    f_num= float(a)
    h.delete(0, END)
    
def div():  
    a=h.get()
    global f_num
    global function
    function="div"
    f_num= float(a)
    h.delete(0, END)

def pwr():
    a=h.get()
    global f_num
    global function
    function="pwr"
    f_num= float(a)
    h.delete(0, END)

def sqrt():
    a=h.get()
    global f_num
    f_num=float(a)
    h.delete(0, END)
    h.insert(0, f_num**0.5)
    
def power2():
    a=h.get()
    global f_num
    f_num=float(a)
    h.delete(0, END)
    h.insert(0, f_num**2)

def sin():
    a=h.get()
    global f_num
    f_num= float(a)
    h.delete(0, END)
    b=math.radians(f_num)
    h.insert(0,math.sin(b))

def fact():
    a=h.get()
    global f_num
    f_num= int(a)
    h.delete(0, END)
    h.insert(0,math.factorial(f_num))
    
def cos():
    a=h.get()
    global f_num
    f_num= float(a)
    h.delete(0, END)
    b=math.radians(f_num)
    h.insert(0,math.cos(b))

def tan():
    a=h.get()
    global f_num
    f_num= float(a)
    h.delete(0, END)
    b=math.radians(f_num)
    h.insert(0,math.tan(b))

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


# Buttons

button_Root= Button(root,font="TimesNewRoman 12", text="√", padx=30, pady=10, command=sqrt).grid(row=1, column=0)
button_Pwr2= Button(root,font="TimesNewRoman 12", text="^2", padx=27, pady=10, command=power2).grid(row=1, column=1)
button_Sin= Button(root,font="TimesNewRoman 12", text="Sin", padx=23, pady=10, command=sin).grid(row=1, column=2)
button_Cos= Button(root,font="TimesNewRoman 12", text="Cos", padx=20, pady=10, command=cos).grid(row=1, column=3)
button_Tan= Button(root,font="TimesNewRoman 12", text="Tan", padx=19.5, pady=10, command=tan).grid(row=1, column=4)

button_9= Button(root,font="TimesNewRoman 12", text="9", padx=30, pady=10, command=lambda:button_click(9)).grid(row=2, column=0)
button_8= Button(root,font="TimesNewRoman 12", text="8", padx=30, pady=10, command=lambda:button_click(8)).grid(row=2, column=1)
button_7= Button(root,font="TimesNewRoman 12", text="7", padx=30, pady=10, command=lambda:button_click(7)).grid(row=2, column=2)
button_Del= Button(root,font="TimesNewRoman 12", text="Del", padx=22, pady=10, command=Del).grid(row=2, column=3)
button_AC= Button(root,font="TimesNewRoman 12", text="AC", padx=21, pady=10, command=button_clear).grid(row=2, column=4)

button_6= Button(root,font="TimesNewRoman 12", text="6", padx=30, pady=10, command=lambda:button_click(6)).grid(row=3, column=0)
button_5= Button(root,font="TimesNewRoman 12", text="5", padx=30, pady=10, command=lambda:button_click(5)).grid(row=3, column=1)
button_4= Button(root,font="TimesNewRoman 12", text="4", padx=30, pady=10, command=lambda:button_click(4)).grid(row=3, column=2)
button_Multi= Button(root,font="TimesNewRoman 12", text=" x ", padx=26, pady=10, command=multi).grid(row=3, column=3)
button_Divide= Button(root,font="TimesNewRoman 12", text="÷", padx=28, pady=10, command=div).grid(row=3, column=4)

button_3= Button(root,font="TimesNewRoman 12", text="3", padx=30, pady=10, command=lambda:button_click(3)).grid(row=4, column=0)
button_2= Button(root,font="TimesNewRoman 12", text="2", padx=30, pady=10, command=lambda:button_click(2)).grid(row=4, column=1)
button_1= Button(root,font="TimesNewRoman 12", text="1", padx=30, pady=10, command=lambda:button_click(1)).grid(row=4, column=2)
button_Add= Button(root,font="TimesNewRoman 12", text=" + ", padx=25, pady=10, command=add).grid(row=4, column=3)
button_Sub= Button(root,font="TimesNewRoman 12", text=" - ", padx=26, pady=10, command=sub).grid(row=4, column=4)

button_Dot= Button(root,font="TimesNewRoman 12", text=".", padx=32, pady=10, command=lambda:button_click(".")).grid(row=5, column=0)
button_0= Button(root,font="TimesNewRoman 12", text="0", padx=30, pady=10, command=lambda:button_click(0)).grid(row=5, column=1)
button_Equlas= Button(root,font="TimesNewRoman 12", text="=", padx=30, pady=10, command=equals).grid(row=5, column=2)
button_Pwrn= Button(root,font="TimesNewRoman 12", text="^n", padx=26, pady=10, command=pwr).grid(row=5, column=3)
button_Factorial= Button(root,font="TimesNewRoman 12", text="!", padx=30, pady=10, command=fact).grid(row=5, column=4)

root.mainloop()






















# import PIL 
# from PIL import Image, ImageTk
# import os

# Size

# Width x Height
# Hamza_root.minsize(500, 100)
# Hamza_root.maxsize(800,200)
# photo=PhotoImage(file="2.png")
# hamza=Label(image=photo)
# hamza.pack()