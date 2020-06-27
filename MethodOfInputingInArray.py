import numpy as np
n=int(input("Enter the range of array : "))
arr=np.array([input().split(' ') for i in range(n)],int)
print(arr)
