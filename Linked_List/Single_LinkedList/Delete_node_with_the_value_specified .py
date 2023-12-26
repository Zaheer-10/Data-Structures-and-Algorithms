class Node :
    def __init__(self ,data):
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self):
        self.head = None 
        
    def add_node(self,data):
        n = Node(data)
        n.next = self.head 
        self.head = n
        
    def delete_node(self, value ):
        temp = self.head 
        prev = None
        
        while temp :
            if temp.data == value:
                if prev:
                    prev.next = temp.next
                else :
                    self.head = temp.next 
                    
                del temp
                return
            prev = temp
            temp = temp.next 
            
    def traverse (self):
        temp  = self.head
        while temp:
            print(temp.data)
            temp = temp.next 
l = LinkedList() # create a linked list object
l.add_node(1) # add some nodes
l.add_node(2)
l.add_node(3)

l.delete_node(2)

l.traverse()

