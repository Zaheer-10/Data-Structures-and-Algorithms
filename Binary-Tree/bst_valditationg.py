# Define a class for nodes of the binary tree
class Node:
    def __init__(self, key):
        self.key = key # The value of the node
        self.left = None # The left child of the node
        self.right = None # The right child of the node

# Initialize min and max as None
min = None
max = None

# Define a recursive function to check if a tree is BST
def isBST(node, min, max):
    # If the node is None, return True (base case)
    if node is None:
        return True
    # If the node's key is less than min or greater than max, return False (violation of BST property)
    if (min is not None and node.key < min) or (max is not None and node.key > max):
        return False
    # Recursively check if the left subtree is BST with min as None and max as the node's key, and if the right subtree is BST with min as the node's key and max as None
    left = isBST(node.left, min, node.key)
    right = isBST(node.right, node.key, max)
    # Return the logical AND of the results of the recursive calls
    return left and right

# Example of a BST
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(17)

# Example of a non-BST
root2 = Node(10)
root2.left = Node(5)
root2.right = Node(15)
root2.left.left = Node(3)
root2.left.right = Node(7)
root2.right.left = Node(8) # This violates the BST property
root2.right.right = Node(17)

# Test the function on the examples
print(isBST(root, min, max)) # True
print(isBST(root2, min, max)) # False
