n=int(input())
a=[n]
state='s0'
if n==00:
    sum=0
if n==0o1 or n==10:
    sum=1
print(sum,state)
if n==11:
    sum=0
    state="s1"
if n==10 or 0o1 and state=="s1":
    sum=0
if n==11 and state=="s1":
    sum=0
if n==00 and state=="s1":
    sum=1
    state="s0"
print(sum,state)















##
##
##
##if n==1 or n==0:
##    if n==0:
##        state="s1"
##        parity=1
##    else:
##        state="s2"
##        parity=0
##    print(state,parity)
##    while(n>=0):
##        n=int(input())
##        if(n==0 or n==1):
##            a.append(n)
##            if n==1:                
##                if state=="s1":
##                    state="s2"
##                    parity=0
##
##                else:
##                    state="s1"
##                    parity=1
##            print(state,parity)
##print("the parity of the given binary list",a,"is",parity)
##print("prog ends")
