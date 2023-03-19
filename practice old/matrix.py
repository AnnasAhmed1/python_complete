print("    1   2   3   4   5   6   7   8")

for j in range(8):
    print("  ",end='')
    for i in range(8):
        print("+---",end="")
    print()
    print("  ",end=""),print("|   "*9)
    print(j,end=" "),print("|   "*9)
    print("  ",end=""),print("|   "*9)
print(end="  ")
for i in range(8):
    print("+---",end="")
print()


nr=8
nc=8
board=[]
for i in range(nr):
    r=[]
    for j in range(nc):
        r.append('*')
    board.append(r)



for x in range(8):
    for y in range(8):
        board[x][y] = '*'
# Starting pieces:
board[3][3] = 'X'
board[3][4] = 'O'
board[4][3] = 'O'
board[4][4] = 'X'


for i in range(nr):
    for j in range(nc):
        print(board[i][j],end="  ")
    print()











