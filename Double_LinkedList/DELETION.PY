class Node :
    def __init__(self , data):
        self.data = data
        self.next = None
        self.previous = None
        
class DLL:
    def __init__(self):
        self.head = None
        
    def delete_at_beginning(self):
        temp = self.head 
        self.head = temp.next
        temp.next = None
        self.head.previous = None
        
    def delete_at_end(self):
        temp = self.head.next
        before = self.head
        while temp.next !=None:
            temp = temp.next
            before = before.next
        temp.previous = None 
        before.next = None
    
    def delete_from_specific_position(self , position):
        temp = self.head.next
        before = self.head
        for i in range(1,position-1):
            temp = temp.next
            before = before.next 
        before.next = temp.next
        temp.next.previous = before
        temp.previous = None
        temp.next = None
    
    def traverse(self):
        temp = self.head
        while temp :
            print(temp.data , "-->" , end="")
            temp = temp.next
        print()
        
n = Node(10)
n1 = Node(20)
n2 = Node(30)
n3 = Node(40)
n4 = Node(50)
n5 = Node(60)
n6 = Node(70)

l = DLL()

l.head = n
n.next = n1
n1.previous = n
n1.next = n2

n2.next= n3
n2.previous = n1

n3.next= n4
n3.previous = n2

n4.next= n5
n4.previous = n3

n5.next= n6
n5.previous = n4

l.delete_at_beginning()
# 20 -->30 -->40 -->50 -->60 -->70 -->

l.delete_at_end()
# 20 -->30 -->40 -->50 -->60 -->

l.delete_from_specific_position(3)
# 20 -->30 -->50 -->60 -->

l.traverse()