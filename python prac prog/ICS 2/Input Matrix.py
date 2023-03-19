
#INPUT MATRIX
nr=3
nc=4
m=[]
for r in range(nr):
   r=[]
   for c in range(nc):
        element=float(input("enter any num"))
        r.append(element)
   m.append(r)

    
#DISPLAY MATRIX
nr=len(m)
nc=len(m[0])
for r in range(nr):
    for c in range(nc):
        print((m[r][c]),end="\t")
    print()

pr=int(input("enter pivot row"))
pc=int(input("enter pivot column"))
pivotelement=m[pr][pc]
for c in range(nc):
    m[pr][c]=m[pr][c]/pivotelement

nr=len(m)
nc=len(m[0])
for r in range(nr):
    for c in range(nc):
        print((m[r][c]),end="\t")
    print()
