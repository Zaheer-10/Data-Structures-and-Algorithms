class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Function to print the linked list
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

# Function to insert a new node at position k in the linked list
def insertAtK(head, val, k):
    # If the linked list is empty and k is 1, insert the new node as the head
    if head is None:
        return Node(val) if k == 1 else head
    # If k is 1, insert the new node at the beginning of the linked list
    if k == 1:
        return Node(val, head)

    cnt = 0
    temp = head

    # Traverse the linked list to find the node at position k-1
    while temp is not None:
        cnt += 1
        if cnt == k - 1:
            # Insert the new node after the node at position k-1
            new_node = Node(val, temp.next)
            temp.next = new_node
            break
        temp = temp.next

    return head

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
    head = insertAtK(head, val, k)

    # Printing the linked list
    printLL(head)
