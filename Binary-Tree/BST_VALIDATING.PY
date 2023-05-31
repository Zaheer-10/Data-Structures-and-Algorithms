class Node:
    def __init__ (self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

min_value = None
max_value = None
def is_BST(node , min_value , max_value ):
    if node is None:
        return True
    
    if (min_value is not None and  node.data < min_value) or (max_value is not None and node.data > max_value):
        return False
    
    left = is_BST(node.lchild , min_value , node.data)
    right = is_BST(node.rchild , node.data , max_value)
    
    return left and  right



# Example of a BST
root = Node(10)
root.lchild = Node(5)
root.rchild = Node(15)
root.lchild.lchild = Node(3)
root.lchild.rchild = Node(7)
root.rchild.lchild = Node(12)
root.rchild.rchild = Node(17)

# Example of a non-BST
root2 = Node(10)
root2.lchild = Node(5)
root2.rchild = Node(15)
root2.lchild.lchild = Node(3)
root2.lchild.rchild = Node(7)
root2.rchild.lchild = Node(8) # This violates the BST property
root2.rchild.rchild = Node(17)

# Test the function on the examples
print(is_BST(root, min, max)) # True
print(is_BST(root2, min, max)) # False
