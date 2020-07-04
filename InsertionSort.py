n=int(input("Enter the size of array : "))
temp=0
arr=[]
print("Enter array element : ")
for i in range(n):
    arr.append(int(input()))
for i in range(1,n):
    temp=arr[i]
    j=i-1
    while((temp<arr[j]) and (j>=0)):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=temp
print("After Sorting : ")
print(arr)
    
