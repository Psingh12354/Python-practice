a = [1, 3, 4, 6, 8] 
b = [4, 5, 6, 2, 10]
print("Orignal List 1 : "+str(a))
print("Orignal List 2 : "+str(b))
resultant=[]
for i in range(0,len(a)):
    resultant.append(a[i]+b[i])
print("Resultant List is : "+str(resultant))
