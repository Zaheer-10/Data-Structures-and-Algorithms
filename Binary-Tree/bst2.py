class BST:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
        
        
    def insert(self , data):
        if self.data is None:
            self.data = data
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
        return
    
    
    def search(self,data):
        if self.data is None:
            return None
        if self.data == data:
            return self.data
        if data < self.data:
            if self.lchild:
                return self.lchild.search(data)
            else:
                return None
        else:
            if self.rchild:
                return self.rchild.search(data)
            else:
                return None
            
    def __str__(self):
        if self.data is None:
            return "Empty BST"
        if self.lchild:
            return "{} -> {}".format(self.data,self.lchild)
        else:
            return "{} -> None".format(self.data)
        
tree = BST(5)
tree.insert(2)
tree.insert(8)
tree.insert(1)
tree.insert(3)

print(tree)
