class Node:
    def __init__(self, node):
        self.data = node
        self.next = None

def delete_tail(head):
    if not head:
        return 
    
    temp = head
    while temp.next.next:
        temp = temp.next
        
    temp.next = None
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
    head = delete_tail(head)
    print_ll(head)
    