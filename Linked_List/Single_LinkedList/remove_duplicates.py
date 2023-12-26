class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None
        
class SLL:
    def __init__(self) :
        self.head = None
        
        
    def insert_beginning  (self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
        
        
    # def remove_duplicates(self):
        # temp = self.head
        # 
        # while temp and temp.next :
            # if temp.data == temp.next.data:
                # temp.next = temp.next.next 
            # else :
                # temp = temp.next
 # Remove duplicates from an unsorted list using hashing
    def remove_duplicates(self):
        # Create an empty set to store the visited elements
        visited = set()
        # Initialize a pointer to the head node
        current = self.head
        # Initialize a pointer to the previous node as None
        prev = None
        # Traverse the list until the end
        while current:
          # If the current node's data is already in the set, it means it is a duplicate
          if current.data in visited:
            # Remove the current node by updating the previous node's next pointer to point to the current node's next node
            prev.next = current.next
          else:
            # Otherwise, add the current node's data to the set and update the previous node to point to the current node
            visited.add(current.data)
            prev = current
          # Move to the next node
          current = current.next
                
    def traverse (self):
        if self.head is None:
            print("Empty list")
            return
        
        temp = self.head
        while temp !=None:
            print(temp.data)
            temp = temp.next
            
n = Node(1565)
n1 = Node(13)
n2 = Node(2)
n3= Node(3445)
n4= Node(13)

sl = SLL()

sl.head = n
n.next = n1
n1.next = n2
n2.next = n3
n3.next= n4

sl.insert_beginning(13)
sl.insert_beginning(1)

sl.remove_duplicates()
sl.traverse()
        
        

'''# Initial list: 10 -> 3 -> 5 -> 7 -> 8 -> 3 -> 10 -> 3 -> None
# Initial set: {}
# Current points to the head node (10)
# Prev points to None

current
  |
  V
10 -> 3 -> 5 -> 7 -> 8 -> 3 -> 10 -> 3 -> None
prev

# Check if current.data (10) is in the set, it is not
# Add current.data (10) to the set
# Update prev to point to current

       current
         |
         V
10 -> 3 -> 5 -> 7 -> 8 -> 3 -> 10 -> 3 -> None
prev

# Set becomes: {10}

# Move current to the next node (3)

       prev   current
         |      |
         V      V
10 -> 3 ->'''

'''
Sure, I'll try to write a code to remove duplicates from an unsorted list. I'll use the hashing method, which is one of the possible methods. Here is a possible code:

```python
# Define a node class
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Define a linked list class
class LinkedList:
  def __init__(self):
    self.head = None

  # Add a node at the end of the list
  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    current = self.head
    while current.next:
      current = current.next
    current.next = new_node

  # Remove duplicates from an unsorted list using hashing
  def remove_duplicates(self):
    # Create an empty set to store the visited elements
    visited = set()
    # Initialize a pointer to the head node
    current = self.head
    # Initialize a pointer to the previous node as None
    prev = None
    # Traverse the list until the end
    while current:
      # If the current node's data is already in the set, it means it is a duplicate
      if current.data in visited:
        # Remove the current node by updating the previous node's next pointer to point to the current node's next node
        prev.next = current.next
      else:
        # Otherwise, add the current node's data to the set and update the previous node to point to the current node
        visited.add(current.data)
        prev = current
      # Move to the next node
      current = current.next

  # Print the list
  def print_list(self):
    current = self.head
    while current:
      print(current.data, end=" ")
      current = current.next
    print()

# Test the program
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(2)
llist.append(3)
llist.append(3)
llist.append(4)
llist.print_list() # 1 2 2 3 3 4 
llist.remove_duplicates()
llist.print_list() # 1 2 3 4 
```

'''