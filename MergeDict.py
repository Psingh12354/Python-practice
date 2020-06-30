def merge(dict1,dict2):
    return(dict2.update(dict1))
dict1={1:'Pk',2:'FK'}
dict2={3:'ds',4:'fr'}
print(merge(dict1,dict2))
print(dict2)
