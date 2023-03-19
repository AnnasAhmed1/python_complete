a=[]
s_score=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    a.append([name,score])
    s_score.append(score)
print(s_score)
s_score.sort()
s_score=set(s_score)
s_score=list(s_score)
c=[]
for i in range(len(a)):
    if(a[i][1]==s_score[-2]):
        c.append((a[i][0]))
c.sort()    
for i in range(len(c)):
    print(c[i])
print(c,a,s_score,s_score[-2])
