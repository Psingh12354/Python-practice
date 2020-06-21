from collections import Counter
array1=[4,5,64,1,6,9,5]
x=5
d=Counter(array1)
print('{} has occured {} times'.format(x,d[x]))
