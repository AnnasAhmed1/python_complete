# print times table of given range

a=int(input("enter first num:"))
b=int(input("enter second num:"))
while (a<=b):
    c=0
    while(c<=10):
        p=a*c
        print(a,"x",c,"=",p)
        c+=1
    print("\n")
    a+=1
