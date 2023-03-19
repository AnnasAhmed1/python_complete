# n = int(input())
# integer_list = map(int, input().split())
# print(integer_list)
# print(hash(integer_list))

if __name__ == '__main__':
    n = int(input())
    integer_list = input().split()
    for i in range(0,len(integer_list)):
        integer_list[i]=int(integer_list[i])
    print(integer_list)
    t=tuple(integer_list)
    print(t)
    print(hash(t))