def bubble_sort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swapped:
            break
    return array 
    
a = [4,6,2,1,5,7,0]
print(bubble_sort(a))
