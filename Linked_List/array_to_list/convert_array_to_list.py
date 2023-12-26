# Define a node class
class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Define a function to convert an array to a linked list
def array_to_linked_list(array):
    
    # If the array is empty, return None
    if not array:
        return None
    # Create a head node with the first element of the array
    head = Node(array[0])
    
    # Keep track of the temp node
    temp = head 
    
    # Loop through the rest of the array elements
    for i in range (1,len(array)):
        new_node = Node(array[i]) # Create a new node with the temp element
        temp.next = new_node # Link the current node to the new node
        temp = new_node  # Update the current node to the new node
        
    return head    # Return the head node of the linked list

array = [1,2,3,4,5]

linked_list = array_to_linked_list(array)

while linked_list :
    print(linked_list.data)
    linked_list = linked_list.next

