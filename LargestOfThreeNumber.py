## program to print largesst of three number
a=int(input("Enter the number 1 : "))
b=int(input("Enter the number 2 : "))
c=int(input("Enter the number 3 : "))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
