from array import *
def dupli(n):
    n_set=set()
    n_dupli=-1
    for i in range(len(n)):
        if n[i] in n_set:
            return n[i]
        else:
            n_set.add(n[i])
    return n_dupli
n=array('i',[1,3,5,4,32,65,53,243,3])
print(dupli(n))
