import heapq as hq
num=[25, 35, 22, 85, 14, 65, 75, 22, 58]
print('Original list : ',str(num))
largest=hq.nlargest(3,num)
print("\nThree largest numbers are : ",largest)
