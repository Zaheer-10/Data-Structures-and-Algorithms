class MinHeap:
    def __init__(self):
        self.heap = []
        
#  ----------------------------------------------------------------------------------------------------------

    def heapify_up(self, index): # comparing with the parent Index
        while index > 0:   
            parent_index = (index - 1) // 2
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

#  ----------------------------------------------------------------------------------------------------------

    def heapify_down(self, index):
        while index < len(self.heap): # Comparing with the Children
            left_child_index = 2 * index + 1  
            right_child_index = 2 * index + 2
            smallest = index
            
                #left 1st
            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index
                
                # It has right child                    #right index value              
            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
            
#  ----------------------------------------------------------------------------------------------------------

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

#  ----------------------------------------------------------------------------------------------------------

    def delete(self, value):
        if value not in self.heap:
            return

        index = self.heap.index(value)
        self.heap[index], self.heap[-1] = self.heap[-1], self.heap[index]
        self.heap.pop()
        self.heapify_down(index)
        
#  ----------------------------------------------------------------------------------------------------------

    def extract_min(self):
        if not self.heap:
            return None

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_value = self.heap.pop(0)
        self.heapify_down(0)
        return min_value

#  ----------------------------------------------------------------------------------------------------------

    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]
    
#  ----------------------------------------------------------------------------------------------------------
   
    def build_heap(self, numbers):
        self.heap = numbers
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)  
            
#  ----------------------------------------------------------------------------------------------------------

    def print_heap(self):
        for i in range(len(self.heap)):
            print(self.heap[i])
  
#  ----------------------------------------------------------------------------------------------------------

minHeap = MinHeap()
minHeap.insert(15)
minHeap.insert(7)
minHeap.insert(9)
minHeap.insert(4)
minHeap.insert(13)

h = [15,
     7,9,4,13]
minHeap.build_heap(h)
minHeap.delete(7)
minHeap.print_heap()