class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
        
def to_ll(array):
        if not array:
            return None
        head = Node(array[0])
        
        temp = head 
        for i in range(1,len(array)):
            n = Node(array[i])
            temp.next = n
            temp = n
            
        return head 

a = [1,2,2,3]

ll = to_ll(a)

while ll :
    print(ll.data)
    ll = ll.next 
            
print(a)