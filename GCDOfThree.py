def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("Enter the number"))
e=gcd(a,b)
f=gcd(b,c)
g=gcd(e,f)
print(g)
