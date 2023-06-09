from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self,value):
        self.container.append(value)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size (self):
        return len(self.container)
    
s = Stack()

empty = s.is_empty()
print(empty)

s.push(10)
s.push(30)
s.push(40)


print("peek" , s.peek())
print(s.container)
print()
