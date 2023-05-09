class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        
class SLL :
    def __init__(self) :
        self.head = None 
        
    def insert_end (self,data):
        ne = Node(data)
        temp = self.head
        while temp.next :
            temp = temp.next
        temp.next = ne
      
      
        
    def traverse (self):
        if self.head == None :
            print('Empty list ')
        temp = self.head
         
        while temp != None:
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

s.insert_end(13)
s.insert_end(33300)

s.traverse()
        