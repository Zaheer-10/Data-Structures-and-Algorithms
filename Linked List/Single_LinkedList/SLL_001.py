class Node:
    
    def __init__(self , data):
        self.data = data
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
        
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        
        temp =self.head
        
        while temp is not None:
            print("Linked list :" , temp.data)
            temp = temp.next
            
            
SL = SLL()

# print(SL.display())

n = Node(10)
# print(n.data)
n1 = Node(20)
n3 = Node(30)
n4 = Node(40)
n4 = Node(50)

SL.head = n

SL.head.next = n1

print(SL.display())