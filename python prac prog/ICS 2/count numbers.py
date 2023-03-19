a=[23,45,98,9,98,45,10]
b=set(a)
##for x in a:
##    b.add(x)
for i in b:
    count=0
    for j in range(len(a)):
        if(i==a[j]):
            count+=1
    print("{} = {} times".format(i,count))
