def insertion_sort(array):
    # loop through each element of array
    for i in range(1, len(array)):
        # store the current element as key
        key = array[i]
        # compare key with each element on the left of it until an element smaller than it is found
        # for descending order, change key < array[j] to key > array[j]
        j = i - 1
        while j >= 0 and key < array[j]:
            # shift the element to the right by one position
            array[j + 1] = array[j]
            j = j - 1
        # insert key at after the element just smaller than it
        array[j + 1] = key
# example 1
data = [10,7,3,1,5]
insertion_sort(data)
print('Sorted Array in Ascending Order:')
print(data)

# example 2
data = ['d', 'a', 'c', 'b', 'e']
insertion_sort(data)
print('Sorted Array in Ascending Order:')
print(data)
