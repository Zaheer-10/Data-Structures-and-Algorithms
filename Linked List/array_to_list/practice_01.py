class Node :
    def __init__(self ,data):
        self.data = data
        self.next = None
        
def array_cnv(array):
    if not array :
        print("NOne")
    
    
    head = Node(array[0])
    temp = head 
    
    for i in range (1,len(array)):
        n = Node(array[i])
        temp.next = n
        temp = n
    return head 

array = [5,5,2,5662,3,865]

l = array_cnv (array)

while l:
    print(l.data ,"-->", end='')
    l = l.next 
    

