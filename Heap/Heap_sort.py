def heapify_down(heap , index):
    Left = (2*index)+1
    Right = Left + 1
    
    large = index 
    if Left < len(heap) and heap[large] < heap[Left]:
        large = Left
        
    if Right < len(heap) and heap[large] < heap[Right]:
        large = Right
        
    if large != index:
        heap[index] , heap[large] = heap[large],  heap[index] 
        heapify_down(heap , large)
    return heap

def heap_sort(array):
    sorted_list = []
    temp = array.copy()
    while temp :
        for i in range(len(temp)//2-1,-1,-1):
            heapify_down(temp , i)
            
        sorted_list.insert(0 , temp[0])
        temp[0] , temp[-1] =  temp[-1]  , temp[0] 
        temp.pop()
    return sorted_list

a = [5,2,7,4,1,8,6,8]

print(heap_sort(a))