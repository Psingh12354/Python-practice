n=int(input("Enter the number 1 : "))
y=int(input("Enter the number 2 : "))
sum1=0
sum2=0
for i in range(1,n):
    if(n%i==0):
        sum1+=i
for j in range(1,y):
    if(y%j==0):
        sum2+=j
if(sum2==n and sum1==y):
    print("Amicable !")
else:
    print("Not Amicable !")
