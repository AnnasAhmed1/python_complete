firstNumber="wxyz00000g"
alphaCheck=0
for i in range(0,4):    
    if firstNumber[i].isalpha()==False:
        alphaCheck=1
numCheck=0
for i in range(4,len(firstNumber)):    
    if firstNumber[i].isalpha():
        numCheck=1
if alphaCheck==1:
    firstNumber="ABCD0000000"
elif numCheck==1:
    firstNumber="ABCD0000000"
elif(len(firstNumber)!=11):
    firstNumber=firstNumber[0:4]+"0000000"
firstNumber=firstNumber[0:-1]+"0"
print(firstNumber)
