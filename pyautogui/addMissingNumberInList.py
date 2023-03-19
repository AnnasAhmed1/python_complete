a=[1, 3, 5, 9, 7, 56, 95, 83, 82, 95, 100, 72]
for j in range(0,101):
    for i in range(0,len(a)):
        if (a[i] != j):
            counter=0
        else:
            counter=1
    if(counter==0):
        print(j)
print(a)