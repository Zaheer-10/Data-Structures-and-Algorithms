class Node:
    def __init__(self, node):
        self.data = node
        self.next = None

def delete_kth_ele(head , k):
    if head is None or k <= 0 : return None
    
    
    if k == 1:
        head = head.next
    
    temp = head
    prev = None
    c = 0
    
    while temp:
        c +=1
        if c == k:
            prev.next = prev.next.next
            temp = None
            break
        
        prev = temp
        temp = temp.next
    return head

def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()
    
    
arr = [0, 1, 2]
k = 2
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])

head = delete_kth_ele(head, k)

printLL(head)