import math

print("operations\n + - * / ** factorial\nsin sinh cos cosh tan tanh\n")
operation=input("type operation you want to perform: ")

if operation== "/" or operation=="*" or operation=="**" or operation=="+" or operation=="-":
    a=float(input("enter first number"))
    b=float(input("enter second number"))
    if operation=="/":
        if b!=0:
            c=a/b
    elif operation=="*":
        c=a*b
    elif operation=="+":
        c=a+b
    elif operation=="-":
        c=a-b
    elif operation=="**":
        c=a**b
if operation=="sin" or operation== "cos" or operation== "tan" or operation== "sinh" or operation== "cosh" or operation== "tanh" or operation== "factorial":
    a=float(input("enter number"))
    if operation=="sin":
        a=math.radians(a)
        c=math.sin(a)
    if operation=="cos":
        a=math.radians(a)
        c=math.cos(a)
    if operation=="tan":
        a=math.radians(a)
        c=math.tan(a)
    if operation=="sinh":
        a=math.radians(a)
        c=math.sinh(a)
    if operation=="cosh":
        a=math.radians(a)
        c=math.cosh(a)
    if operation=="tanh":
        a=math.radians(a)
        c=math.tanh(a)
    if operation=="factorial":
        c=math.factorial(a)
print(c)
print("**program end**")
