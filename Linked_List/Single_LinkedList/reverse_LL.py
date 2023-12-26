class Node:
    def __init__(self , data , next=None):
        self.data = data
        self.next = None
 
stack = []        
        
def reverse(head):
    if head is None or head.next is None:
        return head
    
    rest = reverse(head.next)
    head.next.next = head
    head.next = None
    return rest



def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next



if __name__ == "__main__":
    # Sample array, value, and position for insertion
    arr = [12, 8, 5, 7]
    val = 100
    k = 3

    # Creating a linked list with initial elements from the array
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

    # Inserting a new node at position k in the linked list
    head = reverse(head=head)

    # Printing the linked list
    printLL(head)
