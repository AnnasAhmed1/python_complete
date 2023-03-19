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
def inputpivot():
   pr=int(input("enter pivot row"))
   pc=int(input("enter pivot column"))
   pr-=1
   pc-=1
   return(pr,pc)
def makezero():
   for r in range (nr):
      if(r==pr):
         continue
      pivotvalue=m[r][pc]
      for c in range (nc):
         m[r][c]=m[r][c]-m[pr][c]*pivotvalue
def makeone():
   pivotelement=m[pr][pc]
   for c in range(nc):
       m[pr][c]=m[pr][c]/pivotelement
   displaymatrix()      
def displaymatrix():
   nr=len(m)
   nc=len(m[0])
   for r in range(nr):
       for c in range(nc):
           print((m[r][c]),end="\t")
       print()
   print("--------------------------------")

nr,nc,m=inputmatrix()
displaymatrix()
pr,pc=inputpivot()
while(pr>=0):
   makeone()
   makezero()
   displaymatrix()
   pr,pc=inputpivot()
