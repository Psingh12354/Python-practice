def string(str1):
    if len(str1)<2:
        return ''
    return str1[0:2] + str1[-2:]
str1=input("Enter the string : ")
print(string(str1))
