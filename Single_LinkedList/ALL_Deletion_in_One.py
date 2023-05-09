class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Single_Linked_List:
    def __init__(self) :
        self.head = None
    
    def delete_from_beginning(self):
        if self.head is None :
            print("oops! , List is Empty ")
        
        temp = self.head
        self.head = temp.next 
        
    def delete_from_end(self):
        if self.head is None :
            print('List is Empty')
        
        temp = self.head.next
        prev = self.head 
        
        while temp.next != None:
            temp = temp.next
            prev = prev.next
        prev.next = None 
            
    def delete_from_specific_position(self,position):
        if self.head is None :
            print('List is empty')
        
        temp = self.head.next
        previous = self.head
        for i in range (1,position-1):
            temp = temp.next
            previous = previous.next
            
        previous.next = temp.next
        temp.next = None
        
        
    def Traverse(self):
        if self.head is None :
            print("oops! , List is Empty ")
        temp = self.head
        while temp is not None :
            print(temp.data)
            print()
            temp = temp.next
            
            
n = Node(10)
n1 = Node(104)
n2 = Node(103)
n3 = Node(120)
n4 = Node(110)

Sl = Single_Linked_List()
Sl.head = n
n.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

#Elements : 10 ,104,103,120 , 110

Sl.delete_from_beginning()
#Elements : 104 , 103 , 120 , 110

Sl.delete_from_end()
#Elements : 104 , 103 , 120 

Sl.delete_from_specific_position(1)
#Elements : 104 ,  120 

Sl.Traverse()