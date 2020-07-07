#1. append() :- This function is used to insert the value in its argument to the right end of deque.

#2. appendleft() :- This function is used to insert the value in its argument to the left end of deque.

#3. pop() :- This function is used to delete an argument from the right end of deque.

#4. popleft() :- This function is used to delete an argument from the left end of deque.

import collections
de=collections.deque([1,2,3])
de.append(4)
print("Append element is : "+str(de))
de.appendleft(5)
print("Append left element is : "+str(de))
de.pop()
print("Pop element is : "+str(de))
de.popleft()
print("Pop left element is : "+str(de))
