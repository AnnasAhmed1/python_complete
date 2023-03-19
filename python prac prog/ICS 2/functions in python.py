def inputmatrix():
    nr=int(input("enter no of rows"))
    nc=int(input("enter no of colums"))
    m=[]
    for r in range(nr):
       r=[]
       for c in range(nc):
            element=float(input("enter any num"))
            r.append(element)
       m.append(r)
    return(nr,nc,m)
print(inputmatrix())
