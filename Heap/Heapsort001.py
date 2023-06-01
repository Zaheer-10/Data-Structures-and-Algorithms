def heapify_down(heap , index):
    left = 2*index+1
    right = 2*index + 2
    largest = index
    
    if left < len(heap) and heap[largest] < heap[left]:
        largest = left
    elif right < len(heap) and heap[largest] < heap[right]:
        largest = right
    
    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        heapify_down(heap, largest)
        
def heap_sort(array):
    sorted_list= []
    temp = array.copy()
    for i in range(len(array)//2-1,-1,-1):
        heapify_down(temp, i)
        
        sorted_list.insert(0,temp[0])
        temp[0] , temp[-1] = temp[-1] , temp[0]
        temp.pop()
    return sorted_list