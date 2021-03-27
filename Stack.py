from collections import deque
from queue import LifoQueue
stack1=LifoQueue(maxsize=2)
stack=deque()
stack=[]
stack.append('a')
stack.append('b')
print(stack)
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()
print(stack)

print("Size ",stack1.qsize())
stack1.put('a')
stack1.put('b')
print("Full : ",stack1.full())
print("Size : ",stack1.qsize())
print("Element popped")
print(stack1.get())
