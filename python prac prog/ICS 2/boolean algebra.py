##
###INPUT MATRIX
nr=3
nc=4
m=[[2,6,-3,5],[3, 2,-5,7],[-4,1,1,-4]]
##for r in range(nr):
##   r=[]
##   for c in range(nc):
##        element=float(input("enter any num"))
##        r.append(element)
##   m.append(r)
##
    
def makezero():
   for r in range (nr):
      if(r==pr):
         continue
      pivotvalue=m[r][pc]
      for c in range (nc):
         m[r][c]=m[r][c]-m[pr][c]*pivotvalue
      
def displaymatrix():
   nr=len(m)
   nc=len(m[0])
   for r in range(nr):
       for c in range(nc):
           print((m[r][c]),end="\t")
       print()
   print("--------------------------------")
displaymatrix()
#make pivot elment 1
##def makepivotelement():
##   pr=int(input("enter pivot row"))
##   pc=int(input("enter pivot column"))
##   pr-=1]
##   pc-=1]
   
pr=int(input("enter pivot row"))
pc=int(input("enter pivot column"))
pr-=1
pc-=1
while(pr>=0):
   pivotelement=m[pr][pc]
   for c in range(nc):
       m[pr][c]=m[pr][c]/pivotelement
##   # display matrix
##   nr=len(m)
##   nc=len(m[0])
##   for r in range(nr):
##       for c in range(nc):
##           print((m[r][c]),end="\t")
##       print()
##   print("--------------------------------")
   displaymatrix()
   #make other elments of pivot row 0
   makezero()
##   # display matrix
##   nr=len(m)
##   nc=len(m[0])
##   for r in range(nr):
##       for c in range(nc):
##           print((m[r][c]),end="\t")
##       print()
##   print("--------------------------------")
   displaymatrix()
   pr=int(input("enter pivot row"))
   pc=int(input("enter pivot column"))
   pr-=1
   pc-=1

##   pr=int(input("enter pivot row"))
##   pc=int(input("enter pivot column"))
##   pr-=1
##   pc-=1

