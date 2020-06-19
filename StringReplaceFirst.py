def chara(str1):
    char=str1[0]
    str1=str1.replace(char,'$')
    str1=char+str1[1:]
    return str1
str1=input("Enter the string : ")
print(chara(str1))
