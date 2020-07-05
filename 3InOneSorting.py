print("Program that perform three type of sorting they are \n Selection \n Insertion \n Bubble\n")
y=int(input("Enter your choice. \n 1->Selection \n 2->Insertion \n 3-> Bubble \n 4->quit\n"))
while(True):
    if(y==1):
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
    elif(y==2):
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
    elif(y==3):
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
    else:
        quit
print("you are out of the condition: ")


    


                    

        

