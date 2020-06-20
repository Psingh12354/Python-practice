dict1= {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for i in zip(*([key]+(value) for key,value in sorted(dict1.items()))):
    print(*i)
