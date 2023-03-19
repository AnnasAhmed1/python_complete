a=[]
x=0
while(x!="end"):
    x=input("enter any num")
    if(x=="end"):
        continue
    x=int(x)
    a.append(x)
b=set(a)
c=[]
for i in b:
    count=0
    for j in range(len(a)):
        if(i==a[j]):
            count+=1
    c.append(count)
    print(i,"=",count,"times")
print(c)
