def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print('Select operator')
print('1 . addition')
print('2 . subtract')
print('3 . multiply')
print('4 . divide')
while True:
    choice=input('Enter number is from 1,2,3,4 : ')
    if choice in('1','2','3','4'):
        num1=float(input('Enter number 1'))
        num2=float(input('Enter number 2'))
        if choice=='1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice=='2':
            print(num1,"-",num2,"=",sub(num1,num2))
        elif chice=='3':
            print(num1,"*",num2,"=",mul(num1,num2))
        elif choice=='4':
            print(num1,"/",num2,"=",div(num1,num2))
            break;
    else:
        print('Invalid input')
