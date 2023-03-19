a = [[8,1,6],[3,5,7],[4,9,2] ]

def displayMatrix(matrix):
    print('-------------------------------')
    nr=len(matrix)
    nc=len(matrix[0]) 
    for r in range(nr):
        for c in range(nc):
            print((matrix[r][c]),end='\t')
        print('')

displayMatrix(a)

for r in range(len(a)):
    sum_row=sum(a[r])
    print("the sum of row",r,":",sum_row)
for c in range(len(a[0])):
    sum_column=0
    for i in range(len(a)):
        sum_column+=a[i][c]
    print("the sum of column",c,":",sum_column)
sum_diagonal_1=0
for d in range(len(a)):
    sum_diagonal_1+=a[d][d]
print("the sum of diagonal 1:",sum_diagonal_1)
sum_diagonal_2=0
for d in range(len(a)):
    for i in range(len(a)-1,0,-1):
        sum_diagonal_2+=a[d][i]
print("the sum of diagonal 2:",(sum_diagonal_2)/2)

if(sum_row==sum_column==sum_diagonal_1==(sum_diagonal_2/2)):
    print("this is a magic square matrix")
else:
    print("this is not a magic square matrix")
