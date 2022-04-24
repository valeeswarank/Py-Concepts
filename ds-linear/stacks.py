s = []
s.append("https://edition.cnn.com/")
s.append("https://edition.cnn.com/world")
s.append("https://edition.cnn.com/india")
s.append("https://edition.cnn.com/europe")

print(s)
# pop will retrive and remove the last element from the list
print(s.pop())
print(s)

# another way to retrive the last element from list is s[-1]. This method will not remove the last element
print(s[-1])


# We can use the above functionality by using the deque
from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)
stack.appendleft(400)
print(stack)
stack.append(500)
print(stack)
