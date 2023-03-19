
a=int(input("Enter integer number for lenght of list"))
arr=input("Enter list element space seperated").split()
for i in range(0,a):
    arr[i]=int(arr[i])
i=0
j=0
while(j<len(arr)):
    i=j
    s=arr[j]
    while(i<len(arr)):
        if(arr[i]<s):
            s=arr[i]
            ps=i
            arr[j],arr[ps]=arr[ps],arr[j]
        i+=1
    j+=1
for i in range(len(arr)-1,-1,-1):
    if (arr[i]!=arr[i-1]):
        print(arr[i-1])
        break
