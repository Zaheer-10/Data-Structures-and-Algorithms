class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        
class SLL :
    def __init__(self) :
        self.head = None 


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

s.insert_pos(3,13)
s.insert_pos(4,33300)

s.traverse()
        