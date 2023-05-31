class MinHeap:
  def __init__(self):
    self.heap = []

  def heapify_Up(self,index):
    while index > 0 :
      parent = (index-1)//2
      if self.heap[parent] > self.heap[index]:
        self.heap[parent] , self.heap[index] = self.heap[index], self.heap[parent]
        index = parent

      else:
        break 






  def heapify_down(self, index):
    l = len(self.heap)
    while index < l :
      Left_child_index = 2*index+1
      Right_child_index = 2*index+2
      smallest = index 

      if Left_child_index < l and self.heap[Left_child_index] < self.heap[smallest]:
        # self.heap[Left_child_index] , self.heap[smallest] = self.heap[smallest] , self.heap[Left_child_index]
        smallest = Left_child_index

      if Right_child_index < l and self.heap[Right_child_index] < self.heap[smallest]:
        # self.heap[Right_child_index] , self.heap[smallest] = self.heap[smallest] , self.heap[Right_child_index]
        smallest = Right_child_index

      if smallest != index :
        self.heap[index] , self.heap[smallest] = self.heap[smallest] , self.heap[index]
        index = smallest 

      else : 
        break

  def insert(self,value):
    self.heap.append(value)
    self.heapify_down(len(self.heap)-1)
    
    
  def build_heap(self,numbers):
    self.heap = numbers
    for i in range(len(self.heap)//2-1,-1,-1):
      self.heapify_down(i)

  def delete(self,value):
    if value not in self.heap:
      return 

    index = self.heap.index(value)
    self.heap[index] , self.heap[-1] = self.heap[-1] , self.heap[index]
    self.heap.pop()
    self.heapify_down(index)

  def get_min(self):
    if self.heap is not None:
      return self.heap[0]

  def display(self):
    for i in range(len(self.heap)):
      # print("Root Node is - {i} | Child1 - {2*i+1} | Child2 {2*i+2}".format)
      print(self.heap[i])


min_heap = MinHeap()
min_heap.insert(15)
min_heap.insert(7)


numbers = [15,7,9,4,13]
min_heap.build_heap(numbers)

min_heap.display()


