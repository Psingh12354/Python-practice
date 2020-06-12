lst=[]
n=int(input('Enter the number of elements : '))
for i in range(0,n):
    element=int(input())
    lst.append(element)
print(sorted(lst))
