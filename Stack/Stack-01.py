class Stack :
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        if len(self.stack) == 0:
             print('Stack is Empty')
    
    def push (self,item):
        self.stack.append(item)
        
    def pop (self):
        if self.is_empty():
            print('Empty')
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.stack ==0 :
            print('Empty')
        else:
            print(self.stack[-1])
            
    def size(self):
        return len(self.stack)
    
s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)

print(s)