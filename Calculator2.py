def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        a=int(input('Enter the value of first number : '))
        b=int(input('Enter the value of second number : '))
        if input=='add' or '+':
            print(a,"+",b,"=",add(a,b))
        elif input=='subtract' or '-':
            print(a,"-",b,"=",subtract(a,b))
        elif input=='multiply' or '*':
            print(a,"*",b,"=",multiply(a,b))
        elif input=='divide' or '/':
            print(a,"/",b,"=",divide(a,b))
        break
    else:
        print('invalid input')
