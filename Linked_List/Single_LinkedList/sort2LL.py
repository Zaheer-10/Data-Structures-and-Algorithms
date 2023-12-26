# Node class to represent a node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to sort a linked list in ascending order
def sort_linked_list(head):
    if head is None or head.next is None:
        return head

    # Split the linked list into two halves
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half = slow.next
    slow.next = None

    # Recursively sort the two halves
    first_half = sort_linked_list(head)
    second_half = sort_linked_list(second_half)

    # Merge the sorted halves
    sorted_list = merge(first_half, second_half)
    return sorted_list

# Function to merge two sorted linked lists
def merge(first, second):
    if first is None:
        return second
    if second is None:
        return first

    if first.data <= second.data:
        result = first
        result.next = merge(first.next, second)
    else:
        result = second
        result.next = merge(first, second.next)

    return result

# Create the first linked list: 4 -> 2 -> 1 -> 3
head1 = Node(4)
head1.next = Node(2)
head1.next.next = Node(1)
head1.next.next.next = Node(3)

# Create the second linked list: 9 -> 6 -> 7 -> 5
head2 = Node(9)
head2.next = Node(6)
head2.next.next = Node(7)
head2.next.next.next = Node(5)

# Sort the first linked list
sorted_head1 = sort_linked_list(head1)

# Sort the second linked list
sorted_head2 = sort_linked_list(head2)

# Print the sorted linked lists
curr = sorted_head1
while curr:
    print(curr.data, end=" ")
    curr = curr.next
# Output: 1 2 3 4

print()

curr = sorted_head2
while curr:
    print(curr.data, end=" ")
    curr = curr.next
# Output: 5 6 7 9