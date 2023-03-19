#Program for gauss jordan method of simultaneous solution of linear equations.

def displayMatrix(matrix):
    print('-------------------------------')
    nr=len(matrix)
    nc=len(matrix[0]) 
    for r in range(nr):
        for c in range(nc):
            print('%10.6f' % (m[r][c]),end='\t')
        print('')

def matinp(nr,nc):
    m=[]
    for r in range(nr):
        R=[]
        for c in range(nc):
            element=float(input("Enter element: "))
            R.append(element)
        m.append(R)
    return(m)

#Input augmented matrix

nr=int(input("Enter number of rows: "))
nc=int(input("Enter number of columns: "))

m=matinp(nr,nc)

#Display Matrix
displayMatrix(m)

#selection of pivot element
##pr=int(input("Enter row number of pivot element: "))
##pc=int(input("Enter column number of pivot element: "))
##pc-=1
##
##pr-=1
s=0
for i in range(len(m[0])):
   if(m[0][i]<m[0][s]):
       s=i
print(m[0][s])


#making pivot element 1 and value 0
while pr>=0 or pc>=0:
    pivotElement=m[pr][pc]
    for c in range(nc):
        m[pr][c]=m[pr][c]/pivotElement
    displayMatrix(m)

    for r in range(nr):
        if r==pr:
            continue
        pivotValue=m[r][pc]
        for c in range(nc):
            m[r][c]=m[r][c]-m[pr][c]*pivotValue
    displayMatrix(m)
    pr=int(input("Enter row number of pivot element: "))
    pc=int(input("Enter column number of pivot element: "))
    pc-=1
    pr-=1
print("The final answers are: ")
for i in m:
    print(i[-1])
