class BST:
    def __init__(self, data):
        self.data = data
        self.rchild = None
        self.lchild = None
# ------------------------------------------------------------------------------------------------
      
    def insert(self,data):
        if self.data is None:
            self.data = data
            
        if self.data == data: # Dealing with Duplicates
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
                return None
                
        else :
            
            if self.rchild:
                return self.rchild.search(data)
            else:
                print("Not found")
                return None
                
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
        return 
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
    
    def delete(self, data , curr):
        if self.data is None:
            print("Tree is Empty")
            return None
        
        if data < self.data:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            # else:
                # print("Given Data is Not Found")
                
        elif data > self.data:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            # else:
                # print("Given data is Not Found")
                
        else: 
            
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.data = temp.data
                    self.lchild = temp.lchild 
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            
            if self.rchild is None:
                temp = self.lchild
                
                if data == curr:
                    self.data = temp.data
                    self.lchild = temp.lchild 
                    self.rchild = temp.rchild
                    temp = None
                    return

                self = None
                return temp
            
            #2child scenario
             
            # lowest node from right sub tree = lw_node
            lw_node = self.rchild
            while self.lchild:
                lw_node = lw_node.lchild
                # replace lw_node with rchild
                self.data = lw_node.data
                self.rchild = lw_node.rchild
            return self
# ------------------------------------------------------------------------------------------------
            
 
      
      
# ------------------------------------------------------------------------------------------------
def counts(no_of_Nodes):
    if no_of_Nodes is None:
        return 0
    
    return 1 + counts(no_of_Nodes.lchild)+counts(no_of_Nodes.rchild)
          
root = BST(100)
values = [55,58,63,10,110,120,105,164,145]
for i in values:
    root.insert(i)
print(counts(root))
# print(root.search(321))

# print("In-Order")
# print(root.inorder())
# print("Pre-Order")
# print(root.preorder())
# print("IN-Order")
# root.delete(5,root.data)
print(root.inorder())

print(root.delete(58 ,root.data))
print(root.inorder())
