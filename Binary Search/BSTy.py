# BST

class Bst:
    def __init__(self,data):
        self.data = data 
        self.lchild = None
        self.rchild = None
        
    def insert(self,data):
        if self.data is None:
            self.data = data
            return 
        
        if self.data == data:
            return
        if data < self.data :
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = Bst(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = Bst(data)
                
    def search(self , data ):
        if self.data is None:
            return None
        if data < self.data and self.lchild:
            return self.lchild.search(data)
        elif data> self.data and self.rchild:
            return self.rchild.search(data)
        else:
            print("Search Element is not found")
            return ''
        
    def preorder(self):
        if self.data is None:
            return None
        
        print(self.data , end= ' ')
        if self.lchild:
            self.lchild.preorder()
            
        if self.rchild:
            self.rchild.preorder()
        return ''
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.data , ' ',end=' ')
        if self.rchild:
            self.rchild.inorder()
        return ' '
    
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.data, ' ', end= ' ')
        return ' '
    
    def delete(self,data):
        if self.data is None:
            return None
        
        if data < self.data and self.lchild:
           self.lchild = self.lchild.delete(data)
        elif data > self.data and self.rchild:
            self.rchild = self.rchild.delete(data)
        else:
            if not self.lchild:
                return self.rchild
            elif not self.rchild:
                return self.lchild
            else :
                min_node = self.rchild.find_min()
                self.data = min_node.data
                self.rchild = self.rchild.delete(min_node)
                return 
        
                
    def find_min(self):
        temp = self
        while temp.lchild :
            temp = temp.lchild
        return temp.data
    
    def find_max(self):
        temp = self
        while temp.rchild :
            temp = temp.rchild
        return temp.data
    
    
bst = Bst(10)
a = [ 1,11,22,2,3,33,4,44,5,55]
for i in a:
    bst.insert(i)
    
print(bst.inorder())
print("post order")
print(bst.postorder())
print()
print('preorder')
print(bst.preorder())