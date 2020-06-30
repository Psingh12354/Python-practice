def halfDiamond(n):
    for i in range(n):
        for j in range(0,i+1):
            print('*',end="")
        print()
    for i in range(1,n):
        for j in range(i,n):
            print('*',end="")
        print()
n=int(input("Enter the number : "))
halfDiamond(n)
