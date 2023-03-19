a=[2,23,42,11,4,0,9,0,0,0,1,2,0,11]
b=0
while(b<len(a)):
    n=a[b]
    count=0
    ##for j in (a):
    ##    n=j
    c=0
    ##while(c<len(a)):
    ##    n=a[c]
    ##    count=0
    for i in range(0,len(a)):
            if(a[i]==n):
                    count+=1
    c+=1
    print (count)
b+=1
