""" 

Search an element in a Linked List

Problem Statement: Given the head of a linked list and an integer value, find out whether the integer is present in the linked list or not. Return true if it is present, or else return false.

"""

class Node:
    def __init__(self, node):
        self.data = node
        self.next = None
        

def search_an_element(node , target):
    temp = node
    while temp is not None : 
        print(f"Checking node with data {temp.data}")
        if temp.data == target: 
            return 1
        else : 
            temp = temp.next
        
    return 0


def main ():
    target= 3
    arr = [1,2,3]
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    result = search_an_element(head , target)
    if result:
        print(f"The element {target} is present in the linked list.")
    else:
        print(f"The element {target} is not present in the linked list.")

main()