""" 
Find the Length of a Linked List

Algorithm:

1. Start by initializing a pointer to the head that will be used for traversing and initializing a cnt variable to 0.
2. Traverse the linked list using the pointer, and at every node, increment cnt.
3. After reaching the end of the linked list, return cnt, this will be your total number of nodes which is the length of the linked list.


"""

class Node:
    def __init__(self, node):
        self.data = node
        self.next = None

def count_length(head):
    temp = head
    cnt = 0 
    while temp:
        temp = temp.next
        cnt += 1
    return cnt

def main():
    arr = [10, 20, 30]
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    print("Length of the given linked list is:", count_length(head))

main()

    
'''  
Time Complexity: 

Since we are iterating over the entire list,  time complexity is O(N).

Space Complexity:

We are not using any extra space, thus space complexity is O(1) or constant.

'''