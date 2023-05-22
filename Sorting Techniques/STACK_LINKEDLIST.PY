class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        
    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
            
            
    def pop(self):
        if self.top is None:
            print("OOPS stack is empty")
            return None
        else:
            popped_node = self.top
            self.top = self.top.next 
            popped_node.next = None
            return popped_node.data
      
    def is_empty(self):
         return self.top is None 
       
    def peek(self):
        if self.is_empty():
            print("OOPS stack is empty")
            return None
        else:
            return  self.top.data
        
    def display(stack):
        temp = stack.top
        print("Stack :")
        while temp:
            print(temp.data)
            temp = temp.next 
        
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)


stack.display()

top_ele = stack.peek()
print(top_ele)

popped_ele = stack.pop()
print(popped_ele)

print('*'*12)

stack.display()