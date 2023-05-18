def merge_sort(array):
	if len(array)<=1:
		return array
	
	mid = len(array)//2
	
	left = merge_sort(array[:mid])
	right = merge_sort(array[mid+1:])

	return array 

def merge(left , right):
	result = []
	left_index , right_index = 0 , 0
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
