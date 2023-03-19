# arr=[26,56,45,31,96,12,43]
# i=0
# n=len(arr)-1
# greatest=arr[0]

# def maxNum(i,greatest,arr):
#     if greatest<arr[i+1]:
#         greatest=arr[i+1]
#     if (i==n-1):
#         return greatest
#     else:
#         return maxNum(i+1,greatest,arr)   

# max=maxNum(i,greatest,arr)
# print(max)

num2=12
num1=18
factor=1
i=1

if num1<num2:
    smaller=num1
else:
    smaller=num2

def GCD( smaller, num1, num2, i, factor):
    if (num1 % i==0 and num2 % i ==0):
        factor=i
    if i==smaller:
        return factor
    else:
        return GCD( smaller, num1, num2, i+1, factor )

result=GCD( smaller, num1, num2, i, factor)
print(result)