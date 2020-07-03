n=int(input("Enter the number : "))
print("Enter the element in array")
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)
temp=0
for i in range(n):
    for j in range(i+1,n):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("After sorting : ")
print(arr)

