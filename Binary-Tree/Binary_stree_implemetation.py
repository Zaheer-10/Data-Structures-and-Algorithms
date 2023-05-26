
class BST:
    def __init__(self, data):
        self.data = data
        self.rchild = None
        self.lchild = None
# ------------------------------------------------------------------------------------------------
      
    def insert(self,data):
        if self.data is None:
            self.data = data
            
        if self.data == data:
            return
        
        if self.data > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
                
        else:
            
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
# ------------------------------------------------------------------------------------------------
             
                
    def search(self,data):
        if self.data is None:
            return None
        
        if self.data == data:
            print("Search element is Found")
            return self.data
        
        if data < self.data:
            if self.lchild:
                return self.lchild.search(data)
            else:
                print("Sorry! Element is Not found ")
                
        else :
            
            if self.rchild:
                return self.rchild.search(data)
            else:
                print("Not found")
                
# ------------------------------------------------------------------------------------------------
      
    def preorder(self):
        # Root --> Left --> Right
        if self.data is None:
            return []
        print(self.data, "  ",end='')
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
        return ''
    
# ------------------------------------------------------------------------------------------------
    def inorder(self):
        # Left --> Root --> Right
        if self.lchild:
            self.lchild.inorder()
        print(self.data, "  ",end='')
        if self.rchild:
            self.rchild.inorder()
        return ''
# ------------------------------------------------------------------------------------------------
    def postorder(self):
        # Left --> Right --> Root
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.data,"  ", end='')
        return ''
# ------------------------------------------------------------------------------------------------

 
      
      
# ------------------------------------------------------------------------------------------------
          
root = BST(10)
values = [6,3,1,7,98]
for i in values:
    root.insert(i)
    
# print(root.search(321))
print("In-Order")
print(root.inorder())
print("Pre-Order")
print(root.preorder())
print("Post-Order")
print(root.postorder())