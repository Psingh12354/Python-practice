n=[]
for i in range(1,1000):
    if i%5==0 and i%7==0:
        n.append(str(i))
print(','.join(n))
