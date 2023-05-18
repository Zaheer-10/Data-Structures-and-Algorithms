def merge_sort(list):
    # base case: if list has one or zero things, it is already sorted
    if len(list) <= 1:
        return list
    
    # recursive case: split list into two parts and sort them
    mid = len(list) // 2 # find middle place
    left = merge_sort(list[:mid]) # sort left part
    right = merge_sort(list[mid:]) # sort right part
    
    # return joined result of left and right parts
    return merge(left, right)

def merge(left, right):
    # make an empty list to store sorted things
    sorted_list = []
    
    # use two pointers to keep track of current thing in each list
    left_index = 0
    right_index = 0
    
    # loop until one of the lists is empty
    while left_index < len(left) and right_index < len(right):
        # compare things at pointers and add smaller one to sorted list
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1 # move pointer forward in left list
        else:
            sorted_list.append(right[right_index])
            right_index += 1 # move pointer forward in right list
    
    # add remaining things of non-empty list to sorted list
    if left_index == len(left): # left list is empty
        sorted_list.extend(right[right_index:]) # add all things of right list
    else: # right list is empty
        sorted_list.extend(left[left_index:]) # add all things of left list
    
    # return sorted list
    return sorted_list


list = [12, 11, 13, 5, 6, 7]
print("Given list is", list)
sorted_list = merge_sort(list)
print("Sorted list is", sorted_list)
