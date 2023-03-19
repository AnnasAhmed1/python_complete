a=[2,23,42,11,4,0,9,0,0,0,1,2,0]
a=sorted(a)
n=int(input("enter the num you want to find: "))
s=0
e=(len(a)-1)
m=((s+e)//2)
while(a[m]!=n):
    if(n>a[m]):
        s=m+1
    else:
        e=m-1
    m=((s+e)//2)
print(a)
print("the number",n,"is at",m)
