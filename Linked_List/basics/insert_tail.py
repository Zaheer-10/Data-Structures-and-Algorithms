class Node:
    def __init__(self, node , next=None):
        self.data = node
        self.next = None


def insert_tail(head, val):
    n = Node(val)
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = n
    n.next = None
    return head

def printLL(head):
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next
        


if __name__ == "__main__":
    # Sample array and value for insertion
    arr = [12, 8, 5, 7]
    val = 111

    # Creating a linked list with initial elements from the array
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

    # Inserting a new node at the tail of the linked list
    head = insert_tail(head, val)

    # Printing the linked list
    printLL(head)