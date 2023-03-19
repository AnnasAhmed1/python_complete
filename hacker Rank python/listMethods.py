
n=int(input());

a=[]


for i in range(0,n):
    command=input().split()

    if command[0]=="insert":
        a.insert(int(command[1]),int(command[2]))
    elif command[0]=="append":
        a.append(int(command[1]))
    elif command[0]=="remove":
        a.remove(int(command[1]))
    elif command[0]=="print":
        print(a)
    elif command[0]=="pop":
        if (len(command)==2):
            a.pop(int(command[1]))
        elif(len(command)==1):
            a.pop()
    elif command[0]=="index":
        a.index(int(command[1]))
    elif command[0]=="remove":
        a.remove(int(command[1]))
    elif command[0]=="count":
        a.count(int(command[1]))
    elif command[0]=="reverse":
        a.reverse()
    elif command[0]=="sort":
        a.sort()
    elif command[0]=="clear":
        a.clear()

