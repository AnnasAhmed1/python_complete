# def count_substring(string, sub_string):

#     return

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)


string="ABCDCDC"
subString="CDC"
for i in range(0, len(string)):
    for j in range (0,len(subString)):
        if(string[i]!=subString[j]):
            break



 