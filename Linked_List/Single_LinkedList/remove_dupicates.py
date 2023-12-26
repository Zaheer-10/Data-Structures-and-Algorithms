class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def remove_duplicates(head) :
    if not head:
        return head

    temp = head
    while temp and temp.next:
        if temp.val == temp.next.val:
            temp.next = temp.next.next
        else:
            temp = temp.next

    return head
# Create a sorted singly linked list with duplicates
head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(2)
head.next.next.next.next = Node(3)

# Call the remove_duplicates function to remove duplicates
head = remove_duplicates(head)

# Print the updated linked list
while head:
    print(head.val, end=" ")
    head = head.next
