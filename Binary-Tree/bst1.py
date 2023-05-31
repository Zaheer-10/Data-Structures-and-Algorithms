class BST:

    # -------------------------------Initialization-------------------------------------
    def __init__(self, data):
        self.data = data
        self.rchild = None
        self.lchild = None


# ------------------------------------Insertion----------------------------------------------------


    def insert(self, data):
        if self.data is None:
            self.data = data
            return

        if self.data == data:  # duplicate
            return

        if data < self.data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

# --------------------------Search--------------------------------------------------------------
    def search(self, data):
        if self.data is None:
            return None

        if self.data == data:
            print("Search element is found")
            return self.data

        if data < self.data and self.lchild:
            return self.lchild.search(data)
        elif data > self.data and self.rchild:
            return self.rchild.search(data)

        print("Sorry! Element is not found")
        return None

# ------------------------Pre-Order----------------------------------------------------------------

    def preorder(self):
        if self.data is None:
            return

        print(self.data, "  ", end='')
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

# -------------------------Inorder---------------------------------------------------------------

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()

        print(self.data, "  ", end=' ')

        if self.rchild:
            self.rchild.inorder()

# -------------------Post-Order---------------------------------------------------------------------

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()

        if self.rchild:
            self.rchild.postorder()

        print(self.data, "  ", end='')

# ----------------------Deletion------------------------------------------------------------------

    def delete(self, data):  # Check if the current node is empty
        if self.data is None:
            print("Tree is Empty")
            return None

        if data < self.data and self.lchild:  # left subtree.
            self.lchild = self.lchild.delete(data)
        elif data > self.data and self.rchild:
            self.rchild = self.rchild.delete(data)  # right SubTree
        else:
            # If data is equal to the current node's data,

            if not self.lchild:
                return self.rchild
            # If the current node has no left child (not self.lchild), return its right child.

            elif not self.rchild:
                return self.lchild
            # If the current node has no right child (not self.rchild), return its left child.

            else:
                # If the current node has both left and right children
                # So we need to find the minimum node in the Ryt St
                min_node = self.rchild.find_min()
                self.data = min_node
                self.rchild = self.rchild.delete(min_node)

        return self


# -------------------------Find Minimum value -------------------------------------


    def find_min(self):
        current = self
        while current.lchild:
            current = current.lchild
        return current.data


# -------------------------------Find max  value--------------------------------


    def find_max(self):
        current = self
        while current.rchild:
            current = current.rchild
        return current.data


# -------Count of Total Node in the tree -------------------------------------------(Outside the class)
def counts(node):
    if node is None:
        return 0

    return 1 + counts(node.lchild) + counts(node.rchild)


# --------------------------------------------------------------------------------------------
root = BST(10)
values = [8, 9, 11, 12]
for i in values:
    root.insert(i)

print(counts(root))
# root.search(58)

print("In-Order")
root.inorder()

print("\nDeleting root node 100")
root = root.delete(9)
print("In-Order after deleting root node")
root.inorder()

print("Minimum value is : ", root.find_min())
print("Maximum  value is : ", root.find_max())
