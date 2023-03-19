a=int(input("enter first number: "))
b=int(input("enter second number: "))
for i in range(a,b+1):
    for c in range(1,11):
        p=i*c
        print (i,"x",c,"=",p,"\n")
