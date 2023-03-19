# decimal to binary
a=int(input("deimcal num"))
b=[]
while a//2!=0:
    c=a
    a=a//2
    d=c%2
    b.append(d)
b.insert(0,a)
print(b)

#1's complement
c=[]
for i in b:
    d=1-i
    c.append(d)
print(c)
#2's complement
i=-1
while c[i]==1:
    i=i-1
c[i]+=1
print(c)
