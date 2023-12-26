class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class  SLL:
    def __init__(self):
        self.head = None
    
    def delete_end(self):
        if self.head is None:
            print ('empty list')
        temp = self.head.next
        prev = self.head
        while temp.next !=  None:
            temp = temp.next
            prev = prev.next
        prev.next = None # break the link of previous
        
    def traverse(self):
        if self.head is None:
            print('list is empty')
        temp = self.head 
        while temp != None :
            print(temp.data)
            
            temp = temp.next
            
n = Node(10)
n1 = Node(104)
n2 = Node(103)
n3 = Node(120)
n4 = Node(110)

s = SLL()
s.head = n
n.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

s.delete_end()
s.traverse()

# Output
# 10
# 104
# 103
# 120       
