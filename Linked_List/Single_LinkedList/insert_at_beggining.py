class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None
        
class SLL:
    def __init__(self) :
        self.head = None
        
        
    def insert_beginning  (self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
        
                
    def traverse (self):
        if self.head is None:
            print("Empty list")
            return
        
        temp = self.head
        while temp !=None:
            print(temp.data)
            temp = temp.next
            
n = Node(10)
n1 = Node(102)
n2 = Node(1022)
n3= Node(93)
n4= Node(7870)

sl = SLL()

sl.head = n
n.next = n1
n1.next = n2
n2.next = n3
n3.next= n4

sl.insert_beginning(13)
sl.insert_beginning(33300)


sl.traverse()
        
        
