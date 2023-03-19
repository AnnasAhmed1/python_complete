
a=[]
namesli=[]
scoresli=[]
namesliSort=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    li=[name,score]
    namesli.append(name)
    scoresli.append(score)
    a.append(li)

scoresli.sort()

for i in range(0,len(a)):
    if i+1<len(a):
        
        if(scoresli[i]!=scoresli[i+1]):
            j=i+1
            break

for i in range(j,len(a)):
    namesliSort.append(scoresli[i])
    if i+1<len(a):
        if(scoresli[i+1]!=scoresli[i]):
            break

finalList=[]

for i in namesliSort:
    for j in range(0,len(a)):
        if i == a[j][1]:
            finalList.append(i)

lowestScore2=finalList[0]
finalList1=[]
fset=set(finalList)

for i in range(0,len(a)):
    if a[i][1]==lowestScore2:
        finalList1.append(a[i][0])

finalList1.sort()


for i in finalList1:
    print(i)
