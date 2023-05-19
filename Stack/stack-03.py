class Stack :
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0 
    
    def push(self,item):
       self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return 'Empty stack'
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return 'Empty stack'
        return self.stack[-1]
        
    def display(self):
        if self.is_empty():
            return 'Empty stack'
        else:
            for i in self.stack:
                print(i)


s = Stack()
empty = s.is_empty()
print(empty)

s.push(100)
s.push(236)
s.push(313)
s.push(46)
s.push(12)
s.push(13)



top= s.peek()
print("TOP element",top)

s.pop()
top= s.peek()
print("TOP element",top)
s.pop()
s.display()

empty = s.is_empty()
print(empty)