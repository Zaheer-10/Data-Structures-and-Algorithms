""" 
Delete Head Node of Linked List
Problem Statement: Given a linked list, delete the head of the linked list and print the linked list with the updated head.
"""

class Node:
    def __init__(self, node):
        self.data = node
        self.next = None

def delete_head(head):
    if not head:
        return 
    head = head.next
    return head

def print_ll(head):
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next
        
        

if __name__ == "__main__":
    arr = [2, 5, 8, 7]
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])
    head = delete_head(head)
    print_ll(head)
    