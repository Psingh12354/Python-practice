def DecToBin(n):
    if n>1:
        DecToBin(n//2)
    print(n%2,end=' ')
n=eval(input('Enter number to convert : '))
print('Decimal = {}'.format(DecToBin(n)))
