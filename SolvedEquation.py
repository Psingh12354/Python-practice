print("Enter the value of a, b, c, d, e, f:")
a,b,c,d,e,f=map(float,input().split(" "))
n=a*e-b*d
print("Value of x and y is :")
if n!=0:
    x=(c*e-b*f)/n
    y=(a*f-c*d)/n
    print("{:.3f} {:.3f}".format(x+0,y+0))
