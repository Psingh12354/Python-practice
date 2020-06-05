import cmath
a=int(input('enter the number : '))
b=int(input('enter the number : '))
c=int(input('enter the number : '))
d=(b**2)-(4*a*c)
q1=(-b+(cmath.sqrt(d)))/2*a
q2=(-b-(cmath.sqrt(d)))/2*a
print('Quadratic equation are q1 = {} and q2 = {}'.format(q1,q2))
