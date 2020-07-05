n=int(input("Enter the number : "))
arr=[]
temp=0
print("Enter array element : \n")
for i in range(n):
    x=int(input())
    arr.append(x)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print("After sorting : \n")
print(arr)
