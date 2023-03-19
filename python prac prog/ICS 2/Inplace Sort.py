
a=[22, 44, 23, 32, 99, 77,22,10,15]
print(a)
j=0
n=len(a)

while(j<n):
    i=j
    s=a[j]
    while(i<n):
        if(a[i]<s):
            s=a[i]
            ps=i
        i+=1
    a[j],a[ps]=a[ps],a[j]
    j+=1

print(a)
