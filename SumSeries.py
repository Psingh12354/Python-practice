print("Enter the number to find the sum")
n=list(map(int,input().split(' ')))
sum=0
for i in range(0,len(n)):
    sum+=n[i]
print(sum)
