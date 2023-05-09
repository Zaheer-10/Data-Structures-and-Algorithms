# Import deque from collections module
from collections import deque

# Create an empty stack
stack = deque()

# Push items to the stack
stack.append("A")
stack.append("B")
stack.append("C")

# Print the stack
print(stack) # deque(['A', 'B', 'C'])

# Pop items from the stack
item = stack.pop()
print(item) # C
print(stack) # deque(['A', 'B'])

item = stack.pop()
print(item) # B
print(stack) # deque(['A'])

item = stack.pop()
print(item) # A
print(stack)