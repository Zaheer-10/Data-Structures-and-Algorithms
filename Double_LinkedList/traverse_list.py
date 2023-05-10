class Node :
    def __init__ (self,data):
        self.data = data    
        self.next = None
        self.previous = None
        
class Double_linked_list:
    def __init__ (self):
        self.head = None
        
    def traverse (self):
        if self.head is None:
            print("Empty list ")
        
        else:
            
            temp = self.head
            while temp:
                print(temp.data ,'-->',end='')
                temp = temp.next
                
                
n = Node(101)
n1 = Node(102)
n2= Node(103)
n3= Node(10644)
n4= Node(1454)
n5 = Node(451)

L = Double_linked_list()

L.head = n

n.next = n1

n1.next = n2
n1.previous = n

n2.next = n3
n2.previous = n1

n3.next = n4
n3.previous = n2

n4.next = n5
n4.previous = n3

L.traverse()
# 101 -->102 -->103 -->10644 -->1454 -->451 -->