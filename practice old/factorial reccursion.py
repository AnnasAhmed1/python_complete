def factorial(a):
    if a==1 or a==0:
        return(1)
    elif a>0:
        return (a*(factorial (a-1)))

a=int(input("enter positive number"))
print(factorial(a))
