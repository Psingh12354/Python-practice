n=int(input("Enter the range of first list : "))
m=int(input("Enter the range of second list : "))
lst1=[]
lst2=[]
print("Enter list 1 value : ")
for i in range(m):
    s1=int(input())
    lst1.append(s1)
print(lst1)
print("Enter list 2 value : ")
for i in range(m):
    s=int(input())
    lst2.append(s)
print(lst2)
lst=lst1+lst2
print("List 1 + List 2 : ",lst)

