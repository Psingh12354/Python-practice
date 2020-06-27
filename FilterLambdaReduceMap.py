from functools import reduce
nums=[3,2,6,8,4,6,2,9]
evens=list(filter(lambda n: n%2==0,nums))
print("Filter : "+str(evens))
doubles=list(map(lambda n: n*2,evens))
print("Map : "+str(doubles))
sum1=reduce(lambda a,b: a+b,doubles)
print("Reduce : "+str(sum1))
