n=int(input("enter binary number"))
a=[n]
state='s0'
if n==1 or n==0:
    if n==0:
        state="s1"
        parity=1
    else:
        state="s2"
        parity=0
    print(state,parity)
    while(n>=0):
        n=int(input("enter binary number"))
        if(n==0 or n==1):
            a.append(n)
            if n==1:                
                if state=="s1":
                    state="s2"
                    parity=0

                else:
                    state="s1"
                    parity=1
            print(state,parity)
print("the parity of the given binary list",a,"is",parity)
print("prog ends")
