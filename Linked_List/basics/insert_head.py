class Node:
    def __init__(self, node , next=None):
        self.data = node
        self.next = None



def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

def insert_beginning(head , val):
    temp = Node(val, head)
    return temp

if __name__ == "__main__":
    # Sample array and value for insertion
    arr = [12, 8, 5, 7]
    val = 100

    # Creating a linked list with initial elements from the array
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

    # Inserting a new node at the head of the linked list
    head = insert_beginning(head, val)

    # Printing the linked list
    printLL(head)