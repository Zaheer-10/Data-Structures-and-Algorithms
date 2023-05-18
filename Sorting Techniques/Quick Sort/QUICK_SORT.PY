def quick_sort(array):
    length = len(array)
    
    if length <= 1:
        return array
    pivot = array.pop()
    
    items_greater = []
    items_lower = []
    
    for item in array:
        if item > pivot :
            items_lower.append(item)
        else :
            items_greater.append(item)
    
    return quick_sort(items_greater) + [pivot] +quick_sort(items_lower)

array= [63,2,2,5,242,634,45234,45,425,54,35,565,23,3,3,6,43]

print(quick_sort(array))