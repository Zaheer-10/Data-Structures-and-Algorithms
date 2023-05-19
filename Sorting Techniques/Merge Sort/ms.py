def merge_sort(array):
	if len(array)<=1:
		return array
	
	mid = len(array)//2
	
	left = merge_sort(array[:mid])
	right = merge_sort(array[mid:])

	return merge(left , right)

def merge(left , right ):
result = []
    left_index = 0
    right_index = 0 
    
    while len(left) < left_index and len(right) < right_index:
        if left[left_index] < right[right_index]:
              result.append(left[left_index])
			left_index +=1
		else:
			result.append(right[right_index])
			right_index +=1
	
	if len(left) == left_index :
		result.extend(right[right_index:])
	else:
		result.extend(left[left_index:])

	return result

list = [9,6,2,54,8,42,4534536543537,2,-43215324667534,-5,3,0,31,5,14]
print(merge_sort(list))