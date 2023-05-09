class Stack:
    def __init__(self):
        self.items=[]

    def push(self , item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


    def is_empty(self):
        return self.items==[]


    def size(self):
        return len(self.items)
    
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

print(stack.items)
#[10, 20, 30, 40, 50]

stack.pop()
print(stack.items)
#[10, 20, 30, 40]

print(stack.size())
#4

print(stack.is_empty())
#False