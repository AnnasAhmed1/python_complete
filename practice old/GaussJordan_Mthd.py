def DisplayMatrix(matrix):
    print(" ------------------ ")
    nr=len(matrix)
    nc=len(matrix[0])
    for a in range(nr):
        for b in range(nc):
            print(' %10.6f' % (M[a][b]), end="\t")
            print(" ")
    print("---------------------")

#input Augmented Matrix

nr = int(input(" Enter No. of rows: "))
nc = int(input(" Enter No. of columns: "))

M = [ ]
for r in range(nr):
    R = [ ]
    for c in range(nc):
        element = float(input(" Enter Element: "))
        R.append(element)
    M.append(R)

#Display matrix

DisplayMatrix(M)

#print("\n")
pr = int(input(" Enter row number of pivot element: "))
pc = int(input(" Enter column number of pivot element: "))
pc-=1
pr-=1

#Make pivot element = 1 and other values = 0

while(pr>=0 or pc>=0):
    
    pivotElement = M[pr][pc]
    for c in range(nc):
        M[pr][c] = M[pr][c] / pivotElement 
    DislpayMatrix(M)

    for r in range(nr):
        if(r == pr):
            continue
        pivotValue = M[r][pc]
        for c in range(nc):
            M[r][c] = M[r][c] - M[pr][c] * pivotValue
    DisplayMatrix(M)
    pr = int(input(" Enter row number of pivot element: "))
    pc = int(input(" Enter column number of pivot element: "))
    pc-=1
    pr-=1

print("The Final Ans is: ")
for i in M:
    print(i[-1])
          

    
            
        

