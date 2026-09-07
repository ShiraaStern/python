# 1
str = input("insert a string")
i = 0
j = len(str)-1
bool = True
while i < j:
    if str[i] != str[j]:
        bool = False
        break
    i += 1
    j -= 1
if bool:
    print("the str is palindrome")
else:
    print("the str is not palindrome")


#2
count = 0
str2 = input("insert a string")
index=0
while ' ' in str2:
         index = str2.index(' ')
         str2 = str2[index+1:]
         count+=1
print(count)

#3
str2 = input("insert a string")
substring =  str2[:1]
while ' ' in str2:
        index = str2.index(' ')
        str2 = str2[index+1:]
        substring +=  str2[:1]
print (substring)