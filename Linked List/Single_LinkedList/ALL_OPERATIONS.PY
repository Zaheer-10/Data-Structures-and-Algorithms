class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Single_Linked_List:
    def __init__(self) :
        self.head = None
        
    # 1. Insert at beginning
    
    def insert_beginning  (self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
        
    # 2. Insert at end 
      
    def insert_end (self,data):
        ne = Node(data)
        temp = self.head
        while temp.next :
            temp = temp.next
        temp.next = ne
        
    # 3. Insert at specific position

    def insert_pos (self,position,data):
        if position < 0 :
            print("Invalid Position")
            
        new_node = Node(data)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            
        else:
            temp = self.head
            previous = None
            count = 0
            
            while count<position:
                previous = temp
                temp = temp.next
                count +=1
                   
            new_node.next = temp
            previous.next = new_node
            
    # 4. Delete from Beginning

    def delete_from_beginning(self):
        if self.head is None :
            print("oops! , List is Empty ")
        
        temp = self.head
        self.head = temp.next 
        
    # 5. Delete from  End
 
    def delete_from_end(self):
        if self.head is None :
            print('List is Empty')
        
        temp = self.head.next
        prev = self.head 
        
        while temp.next != None:
            temp = temp.next
            prev = prev.next
        prev.next = None 
        
    # 6. Delete from specific Position
            
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
        
    # Traverse through the elements
    
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

Sl.insert_beginning(500)
Sl.insert_beginning(55500)
Sl.insert_beginning(50560)

Sl.insert_end(500)

Sl.insert_pos(3,898)


Sl.delete_from_beginning()
Sl.delete_from_end()
Sl.delete_from_specific_position(2)
Sl.Traverse()