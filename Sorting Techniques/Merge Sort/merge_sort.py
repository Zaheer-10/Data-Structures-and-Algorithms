def merge_sort(array):
    if len(array)<= 1:
        return array
    
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    
    return merge(left, right)

def merge(left,right):
    sorted_list = []
    left_index = 0
    right_index = 0 
    
    while left_index < len(left) and right_index < len(right):
        
        if left[left_index] <=  right[right_index]:
            sorted_list.append(left[left_index])
            left_index +=1
        else :
            sorted_list.append(right[right_index])
            right_index +=1
            
    if len(left) == left_index :
        sorted_list.extend(right[right_index:])
    else :
        sorted_list.extend(left[left_index:])
        
    return sorted_list

list = [12, 11, 13, 5, 6, 7]
print("Given list is", list)
sorted_list = merge_sort(list)
print("Sorted list is", sorted_list)
