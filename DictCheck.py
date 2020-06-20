d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def isKey(x):
    if x in d:
        print('Key is present in dictionary')
    else:
        print('Key is not present in dictionary')
x=int(input('Enter the numbers to check : '))
print(isKey(x))
