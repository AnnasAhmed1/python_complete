a=[98,50,48,48,5,50,98,0,0,98,5,40]
b=set(a)
for i in b:
    count=0
    for j in range(len(a)):
        if(i==a[j]):
            count+=1
    print(i,"=",count,"times")
