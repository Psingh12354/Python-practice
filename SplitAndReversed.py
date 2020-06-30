n=int(input("Enter the raanage of list : "))
lst=[]
for i in range(n):
    m=int(input("Enter the number : "))
    lst.append(m)
print("List : "lst)
lst.reverse()
print("list reverse : ",lst)
