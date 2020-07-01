#Question:
#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
##ETTERS 10
#DIGITS 3
s=input()
print("Enter the string : ")
d={"DIGITS":0,"LETTERS":0}
for i in s:
    if i.isdigit():
        d["DIGITS"]+=1
    elif i.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("Letters",d["LETTERS"])
print("DIGITS",d["DIGITS"])
