import sys



from collections import deque
d = deque()
for i in range(0,int(input())):
    k = input().split()
    if k[0] == 'append':
        d.append(int(k[1]))
    elif k[0] == 'pop':
        d.pop()
    elif k[0] == 'popleft':
        d.popleft()
    elif k[0] == 'appendleft':
        d.appendleft(int(k[1]))
for i in range(0 ,len(d)):
    print(d[i],end=' ')