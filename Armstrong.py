n=int(input("Enter the number: "))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+digit**3
    temp//=10
if n==sum:
    print(str(n),' is an armstrong number')
else:
    print('not an armstrong number')
