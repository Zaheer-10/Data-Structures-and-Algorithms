'''
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linked_list :
    def __init__(self) : 
        self.head = None
        
    def mid_value(self):
        slow ,fast = self.head , self.head 
        
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
    
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
            
n = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)
n5 = Node(5)
n6 = Node(6)

l = linked_list()

l.head = n
n.next = n1
n1.next = n2
n2.next = n3
n3.next = n5
n5.next = n6
print("Values : ")
l.traverse()
print('\n')
print("Middle value is : ")
l.mid_value()