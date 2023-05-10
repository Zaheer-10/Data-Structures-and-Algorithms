class Node :
    def __init__ (self,data):
        self.data = data
        self.next = None
        self.previous = None
        
class DLL:
    def __init__(self):
        self.head = None
    
    def Insert_end (self,data):
        n = Node(data)
        
        temp = self.head
        
        while temp.next != None:
            temp = temp.next 
            
        temp.next = n
        n.previous = temp
        
        
                
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

L =DLL()

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

L.Insert_end(313)
# 101 -->102 -->103 -->10644 -->1454 -->451 -->313 -->

L.Insert_end(466)
# 101 -->102 -->103 -->10644 -->1454 -->451 -->313 -->466 -->
L.traverse()
# 101 -->102 -->103 -->10644 -->1454 -->451 -->