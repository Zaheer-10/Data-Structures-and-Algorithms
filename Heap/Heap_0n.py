class Heap:
    def __init__(self):
        self.heap = []
        
    def heapify_up(self , index):
        while index > 0:
            parent = (index- 1) // 2
            if self.heap[parent] > self.heap[index]:
                self.heap[parent] , self.heap[index] = self.heap[index] , self.heap[parent]
                index = parent  
            else:
                break
        
    def heapify_down (self, index):
        while index < len(self.heap):
            Left = 2 * index + 1
            Right = 2*index + 2
            smallest = index 
            
            if Left < len(self.heap) and self.heap[Left] < self.heap[smallest] :
                smallest = Left 
                
            if Right < len(self.heap) and self.heap[Right] < self.heap[smallest] :
                smallest = Right 
            
            if smallest != index :
                self.heap[index] , self.heap[smallest] = self.heap[smallest] ,self.heap[index] 
                index = smallest 
                
            else:
                break
            
            
    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
    
    def delete(self,data):
        index = self.heap.index(data)
        self.heap[index] , self.heap[-1] = self.heap[-1] , self.heap[index]
        self.heap.pop()
        self.heapify_down(index)
    
    def build_heap(self, numbers):
        self.heap = numbers
        for i in range(len(self.heap)//2-1 , -1 ,-1):
            self.heapify_down(i)
            
    def display(self):
        for i in range(len(self.heap)):
            print(self.heap[i] , end=' ')
    
    def heap_sort(self):
        pass
    
h = Heap()
n = [1,64,234,63,54,425]
# h.insert(50)
# h.insert(100)
# h.insert(65)
# h.insert(40)
# h.display()
# h.delete(65)
# h.display()

h.build_heap(n)
h.display