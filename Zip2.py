#The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

#If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")
print(tuple(zip(a,b)))
