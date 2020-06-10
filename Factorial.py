n=int(input("Enter the number to find fact : "))
factorial=1
if n<0:
    print("Input is wrong")
elif n==0:
    print("Factorial is 1")
else:
    for i in range(1,n+1):
        factorial=factorial*i
print("factorial is " + str(factorial))
